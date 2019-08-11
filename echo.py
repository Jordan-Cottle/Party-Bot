import discord

class PartyBot(discord.Client):
    async def on_ready(self):
        print(f"Successfully logged in as {self.user}")
    
    async def on_message(self, msg):
        content = msg.content
        print(f'Message received: ({msg.author}) {content}')

        if msg.author == self.user:
            return
    
        if content.startswith("echo "):
            await msg.channel.send(content[5:])


if __name__ == "__main__":
    import secretInfo

    bot = PartyBot()
    bot.run(secretInfo.botToken)