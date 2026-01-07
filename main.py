import discord
class Client(discord.Client:
  async def on_ready(self):
    print(f'Logged in as {self.user} (ID: {self.user. id})')
    
  async def on_message self, message):
    print f'Message from {message.author}: (message.content}')
    if message.content.startswith ('!hello'):
      await message.channel.send('hello')
    
intents= daicord.Intents.default()
intents.message_content = true

client=Client(intents=intents)
client. run('MTQ10DE4MjExNTMONTgy0TkOMQ.GZxL60.sTw_1PHFw5Jl1NxnWZ5-kTu4LB4vpdu19UY7rE')
