import google.generativeai as genai
import discord
from discord.ext import commands
import os
model=genai.GenerativeModel('gemini-1.5-flash')
intents=discord.Intents.all()
bot = commands.Bot(command_prefix='!',intents=intents)
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
@bot.command()
async def chat(ctx,*,prompt):
    response=model.generate_content(prompt)
    text = response.text
    if len(text) > 1500:
        messages = [text[i:i + 1500] for i in range(0, len(text), 1500)]
    else:
        messages = [text]
        # Send the response messages to the Discord channel
    for text in messages:
        await ctx.send("```" + text + "```")
    #for i in range(0,5):
    #    discord.Embed(await ctx.send(response.choices[i].text))  
bot.run(os.environ['DISCORD_TOKEN'])