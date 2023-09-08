import discord
from discord.ext import commands
from discord.ui import Button, View
from discord.utils import get


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=discord.Intents.all())

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

@bot.command()
async def 버튼(ctx):
    button1 = Button(label="1번 버튼", style = discord.ButtonStyle.green)
    button2 = Button(label="2번 버튼", style = discord.ButtonStyle.green)
    button3 = Button(label="3번 버튼", style = discord.ButtonStyle.green)
    button4 = Button(label="4번 버튼", style = discord.ButtonStyle.green)
    button5 = Button(label="5번 버튼", style = discord.ButtonStyle.green)

    async def button_callback1(interaction:discord.Interaction):
        await ctx.send("1번 버튼 클릭!")

    async def button_callback2(interaction:discord.Interaction):
        await ctx.send("2번 버튼 클릭!")

    async def button_callback3(interaction:discord.Interaction):
        await ctx.send("3번 버튼 클릭!")

    async def button_callback4(interaction:discord.Interaction):
        await ctx.send("4번 버튼 클릭!")

    async def button_callback5(interaction:discord.Interaction):
        await ctx.send("5번 버튼 클릭!")

    button1.callback = button_callback1
    button2.callback = button_callback2
    button3.callback = button_callback3
    button4.callback = button_callback4
    button5.callback = button_callback5

    view = View()
    view.add_item(button1)
    view.add_item(button2)
    view.add_item(button3)
    view.add_item(button4)
    view.add_item(button5)

    await ctx.send(embed = discord.Embed(title='메뉴 선택하기',description="원하시는 버튼을 클릭해주세요", colour=discord.Colour.blue()), view=view)

bot.run('')
