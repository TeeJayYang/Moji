from urllib import request
import json
import discord
import os
import random

bot =  discord.Client()

keywordMap = {}
def setup(url, blacklist):
    response = json.loads(request.urlopen(url).read().decode())
    for key in response:
        if key in blacklist:
            continue
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
    if not message.content.startswith('!translate'):
        return
    wordList = message.content.split()[1:]
    response = ''
    for word in wordList:
        response += word
        if word in keywordMap:
            emojis = ''.join([random.choice(keywordMap[word]) for _ in range(random.randint(1,3))])
            response += emojis
        else:
            response += ' '
    await bot.send_message(message.channel, response)

def updateMapping():
    emojilibURL = 'https://raw.githubusercontent.com/muan/emojilib/master/emojis.json'
    blacklist = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"}
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
