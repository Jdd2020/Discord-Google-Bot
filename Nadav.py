import discord
from googlesearch import search 
from urllib.parse import urlparse
from urllib.parse import urlunparse
from urllib.parse import urlencode

client = discord.Client()


@client.event
async def on_ready(): 
    print('We have logged in as {0.user}'.format(client))  # Confirmation of login (from Discord.py API reference)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('_google-Instructions'): #produces the instructions when the help command is inputted
        await message.channel.send('_google (search) - will search the given term and send out three results\n\n' +
                                   '_google-Spec (Search) will return a single result (used for specific searches)\n\n'
                                   + '_google-YT (Search) will return a YouTube results')

    elif message.content.startswith('_google-Spec'): #Produces a single result
        initial_search = message.content
        term = initial_search[12:]
        for i in search(term,
                        tld='com',
                        num=10,
                        lang='en',
                        start=0,
                        stop=1,
                        pause=0.5,
                        ):
            await message.channel.send(i)

    elif message.content.startswith('_google'): #Produces three results
        initial_search = message.content
        term = initial_search[7:]
        for i in search(term,
                        tld='com',
                        lang='en',
                        num=10,
                        start=0,
                        stop=3,
                        pause=0.5,
                        ):
            await message.channel.send(i)

client.run('NzQ4NTIxMDE3MzgyNzk3NDAy.X0eohQ.irpwUj9ASL_GKH0KZLWxlzLbOu8') #Use your own key
