#a bot for dad jokes

import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print("User ready as: {0.user}".format(client))


def remove_prefix(text, prefix):
    return text[text.startswith(prefix) and len(prefix):]


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    else:
        msg = message.content
        triggerWords = ["I'm ", "Im ", "im ", "I am ", "i am ", "IM ", "I AM ", "I is "]
        listOfMatches = [ele in msg for ele in triggerWords]
        if any(listOfMatches):
            indexOfTrigger = listOfMatches.index(True)
            wordThatTriggered = triggerWords[indexOfTrigger]

            response = msg[msg.index(wordThatTriggered):]
            response = remove_prefix(response, wordThatTriggered)

            #print(response)

            await message.channel.send("Hi {}, I'm DadJames".format(response))


my_token = os.environ['TOKEN']
client.run(my_token)
