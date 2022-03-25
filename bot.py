# BOT
Meu primeiro BOT

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = ">", case_insensitive = True)

@bot.event
async def on_ready():
  print("Entramos como {0.user}" .format(bot))

@bot.command()
async def ajuda(ctx):
  await ctx.send("**Comandos: >professores / >instagram / >youtube / >disc / >materias**")

@bot.command()
async def youtube(ctx):
  await ctx.send("**Link para o youtube do colégio:** https://www.youtube.com/c/eeepjoseribeirodamasceno?app=desktop")

@bot.command()
async def disc(ctx):
  await ctx.send("**Link para o discord do curso:** https://discord.gg/CtgkXnCbVc")

@bot.command()
async def professores(ctx):
  await ctx.send("**1º- Jefferson / 2º- Marcelo**")

@bot.command()
async def instagram(ctx):
  await ctx.send("**Link para o instagram do curso:** https://www.instagram.com/info_jrd/")

@bot.command()
async def materias(ctx):
  embed = discord.Embed(
  title = "Matérias",
  description = "Aqui estão as matérias do 1º, 2º e 3º ano do curso de informática:",
  colour = discord.Colour.red()
  )

  embed.set_author(name = f"{ctx.author}", icon_url = f"{ctx.author.avatar_url}")

  embed.set_thumbnail(url = "https://instagram.ffor1-2.fna.fbcdn.net/v/t51.2885-15/s150x150/115990115_349230139810681_6820611375770938959_n.jpg?_nc_ht=instagram.ffor1-2.fna.fbcdn.net&_nc_cat=101&_nc_ohc=wfRRv4hfHa8AX9e4O8C&edm=ALbqBD0BAAAA&ccb=7-4&oh=00_AT96iKgxi4BWaHahpTSPCyG5ErNYXIHkXJbVfc_pAi0x6A&oe=61E272DE&_nc_sid=9a90d6")

  embed.set_image(url = "https://media.discordapp.net/attachments/930069554107912205/930186310600228906/materias.jpeg?width=587&height=468")

  embed.set_footer(text = f"Seu ID: {ctx.author.id}")

  await ctx.send(embed = embed)

bot.run("token")
