import discord
class Client(discord.Client):
    async def on_ready(self):
       print(f'Logged in as {self.user} (ID: {self.user.id})')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        if message.content.startswith('!hello'):
            await message.channel.send('Hello!')

intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run('')
