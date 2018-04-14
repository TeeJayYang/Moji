# download the word net lemmatizer
import nltk
nltk.download('wordnet')

from urllib import request
import json
import discord
import os
import random
import re
from nltk.stem.wordnet import WordNetLemmatizer

bot =  discord.Client()
lem = WordNetLemmatizer()

keywordMap = {}
def filter_from_blacklist(blacklist, response):
    for key, value in dict(response).items():
        if key in blacklist or value['category'] in blacklist:
            del response[key]
        else:
            for each in value['keywords']:
                if each in blacklist and key in response:
                    del response[key]

def setup(url, blacklist):
    response = json.loads(request.urlopen(url).read().decode())
    filter_from_blacklist(blacklist, response)
    for key in response:
        keywordMap[key] = keywordMap.get(key,[]) + [response[key]['char']]
        for keyword in response[key]['keywords']:
            if keyword in blacklist:
                continue
            keywordMap[keyword] = keywordMap.get(keyword, []) + [response[key]['char']]

@bot.event
async def on_ready():
    print(bot.user.name, bot.user.id)

@bot.event
async def on_message(message):
    if not message.content.startswith('<@{}>'.format(bot.user.id)):
        return
    wordList = message.content.split()[1:]
    response = ''
    for word in wordList:
        response += word
        ## extract the base of the word
        word = re.sub(r'^[^a-zA-z]*|[^a-zA-Z]*$', '' , word.lower())
        base_word = lem.lemmatize(word,'n')
        if word == base_word:
            base_word = lem.lemmatize(word, 'v')

        if base_word in keywordMap:
            emojis = ''.join([random.choice(keywordMap[base_word]) for _ in range(random.randint(1,3))])
            response += emojis
        else:
            response += ' '
    await bot.send_message(message.channel, response)

def updateMapping():
    emojilibURL = 'https://raw.githubusercontent.com/muan/emojilib/master/emojis.json'
    blacklist = {   
                    'words', 'shape', 'flags', 'chinese', 
                    'copyright', 'registered', 'tm', 'alphabet',
                    'numbers'
            }
    setup(emojilibURL, blacklist)
    with open('mapping.json', 'w') as f:
        json.dump(keywordMap, f, ensure_ascii=False)

def loadMapping():
    keywordMap = json.load(open('mapping.json'))

updateMapping()
try:
    bot.run(os.environ['DISCORD_TOKEN'])
except KeyError:
    print('Discord Bot Token not set!') 
    exit(1)
