import discord
import json
import logging
import os
import time
from dotenv import load_dotenv

# logging.basicConfig(level=logging.INFO)

class RoombaBoi(discord.Bot):
	async def on_ready(self):
		print(config["StartingMsg"])
		print("Logged in as {0.user}".format(bot))

#Load Config File
#-----------------------
with open("config.json", "r") as in_configFile:
	config = json.load(in_configFile)
	in_configFile.close()

#Load .env
#-----------------------
load_dotenv()

#Discord Bot Settings
#-----------------------
__BotAuthKey = os.getenv('DIS_AUTHK')
description = "Clean a channel's message history. \nDon't worry, we won't tell anyone what we find."
__MSG_LIMIT = 500

#Instantiate Bot
#-----------------------
bot = RoombaBoi()

#Commands
#-----------------------
@bot.slash_command(name="cleanchannel", description="Deletes all messages in the current channel.")
async def cleanChannel(ctx):
	print("Received command")
	await ctx.respond("Deleting Messages...")
	deleted = await ctx.channel.purge()
	count = len(deleted)
	while len(deleted) != 0:
		deleted = await ctx.channel.purge()
		count += len(deleted)
	print('Deleted {} message(s)'.format(str(count)))
	await ctx.send('Deleted {} message(s)\nAll Clean!'.format(str(count)))

@bot.slash_command(name="generatemessages", description="Generates a specified number of messages in the current channel.")
async def genMsgs(ctx, message_count: int):
	count = 0
	try:
		count = int(message_count)
	except:
		print("Argument must be a number")
		await ctx.respond("Argument must be a number")
		return

	await ctx.respond("Sending Messages...")
	if count > __MSG_LIMIT: 
		count = __MSG_LIMIT
	for index in range(1,count+1):
		message = "Some message #" + str(index)
		await ctx.send(message)

	await ctx.send("All Messages sent!")

bot.run(__BotAuthKey)