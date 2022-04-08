# bot.py
import os

import discord

from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_message(message):
    tooth_price = 0.25
    primogem_cost_low = 0.015
    primogem_cost_high = 0.0165
    low_cost = str(round(tooth_price/primogem_cost_low,2))
    high_cost = str(round(tooth_price/primogem_cost_high,2))
    response = 'Assuming the going rate of '+ str(tooth_price) +\
        ' dollars per tooth, and the cost of a primogem ranges from '\
            + str(primogem_cost_low) + ' to ' + str(primogem_cost_high) + \
                ' dollars, we can calculate that one tooth is worth '\
                    + high_cost + ' to ' + low_cost + ' primogems'
    if message.content == 'teeth?':
        await message.channel.send(response)
        
        
