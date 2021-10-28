#get token from config file
from config import TOKEN 

# discord library 
import discord           

# logging library 
import logging 

# refresh every 24 hours using this library 
import datetime

# Bot Client ID 902025855906238474

# OAUTH2
# https://discord.com/api/oauth2/authorize?client_id=902025855906238474&permissions=0&scope=bot

# Permissions Integer: 2147575808


''' INSTANTIATE CLIENT '''
client = discord.Client()

''' ready up the bot '''
@client.event
async def on_ready():
    print('Logged on as', client.user)



''' Manually respond to commands '''
#######################
###    ON MESSAGE   ###
#######################

@client.event
async def on_message(message):
    ''' don't respond to ourselves '''
    if message.author == client.user:
        return

    if message.content.startswith('$ping'):
        await message.channel.send("<@220296856800854018>")
        logging.info('replied to ping')


    if True:
        pass

    ''' Pull last X recent posts with flair 'Deal/Sale' from r/frugalmalefashion manually '''



''' Automatically post a new subreddit post matching criteria and ping Bladexer '''
#######################
### Background Loop ###
#######################

# async def my_background_task():
#     ''' Background task '''
#     await client.wait_until_ready()

#     time = datetime.now()


# ''' run loop and listen for reddit posts '''
# client.loop.create_task(my_background_task())



''' run the bot '''
client.run(TOKEN)