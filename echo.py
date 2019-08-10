import discord
import secretInfo

client = discord.Client()

@client.event
async def on_ready():
    print(f"Successfully logged in as {client}")

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return

    content = msg.content
    print(f'Message received: ({msg.author}) {content}')
    if content.startswith("echo "):
        await msg.channel.send(content[5:])

client.run(secretInfo.botToken)