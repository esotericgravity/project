import discord

token = NDUzMzkxODUxMjE5ODQ1MTIw.DfeUGw.FzocAa7Q4UUjfy-FhmwW6e_7BDI
client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if on_message.content.startswith('!hello'):
        m = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
        
@client.event
async def on_ready():
    print('logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(token)

    
