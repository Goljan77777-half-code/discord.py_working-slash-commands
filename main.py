import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())

@bot.event
async def on_ready():
    print("logged in")                      #prints message if bot is online
    try:
        synced = await bot.tree.sync()
        print("synced commands")            #send message if commands are synced with the bot
    except Exception as e:
        print(e)                            #sends error message if commands are not being synced

@bot.tree.command(name="hello", description="checks if the slash command is working")   #slash command can be called by "/hello"
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("working slash command")                    #response of the bot

@bot.tree.command(name="option_chooser", description="choose an option")
async def option_chooser(interaction, written_message: str):           #you can write a message which the bot can return
  await interaction.response.send_message(written_message)

bot.run(TOKEN)   #replace TOKEN with your bots token if you are not working with a seperate file to protect the token put the token in quotation marks.
