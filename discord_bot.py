#get token from config file
from config import TOKEN 
from config import CLIENTID
from config import CLIENTSECRET 

# discord library 
import discord
from discord.ext import commands,tasks           

# logging library 
import logging 

from datetime import datetime
from pytz import timezone

#import reddit
import asyncpraw
import asyncio
import commonprojects

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
        # await message.channel.send("<@220296856800854018>")
        await message.channel.send("pong")
        logging.info('replied to ping')


    if True:
        pass

    ''' Pull last X recent posts with flair 'Deal/Sale' from r/frugalmalefashion manually '''



''' Automatically post a new subreddit post matching criteria and ping Bladexer '''
#######################
### Background Loop ###
#######################

async def my_background_task():
    ''' Background task '''
    await client.wait_until_ready()

    reddit = asyncpraw.Reddit(
        client_id=CLIENTID,
        client_secret=CLIENTSECRET,
        user_agent="bot user agent",
    )

    ''' live stream new posts to discord '''
    # subreddit = await reddit.subreddit("frugalmalefashion")
    # async for submission in subreddit.stream.submissions(skip_existing=True):
    #     if submission.link_flair_text == "[Deal/Sale]" or "common projects achilles" in submission.title:
    #         print(submission.title)
    #         timestamp = datetime.fromtimestamp(submission.created_utc)
    #         pacific = timestamp.astimezone(timezone("US/Pacific"))
    #         print("Posted on:", pacific.strftime('%m/%d/%Y %H:%M:%S %Z\n'))

    #         # if submission is an achilles low sale, message/ping user in channel
    #         channel_id = client.get_channel(903768737608499220)
    #         bladexer = "<@220296856800854018>"

    #         # put reddit post into embed object
    #         embed = discord.Embed(
    #             title = submission.title,
    #             url = submission.shortlink,
    #             timestamp = pacific
    #         )

    #         alert_message = "<@220296856800854018> New sale post: " + submission.shortlink + "\n"

    #         # send ping into channel 
    #         await channel_id.send(content=alert_message, embed=embed)
            

    ''' test subreddit '''
    subreddit2 = await reddit.subreddit("pythonstreamtest")
    async for submission in subreddit2.stream.submissions(skip_existing=True):
        if submission.link_flair_text == "test1flair" or "common projects achilles" in submission.title:
            print(submission.title)
            timestamp = datetime.fromtimestamp(submission.created_utc)
            pacific = timestamp.astimezone(timezone("US/Pacific"))
            print("Posted on:", pacific.strftime('%m/%d/%Y %H:%M:%S %Z\n'))

        # if submission is an achilles low sale, message/ping user in channel
            channel_id = client.get_channel(903768737608499220)
            bladexer = "<@220296856800854018>"

        # put reddit post into embed object
            embed = discord.Embed(
                title = submission.title,
                url = submission.shortlink,
                timestamp = pacific
            )

            alert_message = "<@220296856800854018> New sale post: " + submission.shortlink + "\n"

        # send ping into channel 
            await channel_id.send(content=alert_message, embed=embed)
    
    await commonprojects.get_prices()
    await asyncio.sleep(5) #24*60*60)


counter = 0
@tasks.loop(seconds=24*60*60)
async def background2():
    update = await commonprojects.get_prices()
    #await asyncio.sleep(20) #24*60*60)
    global counter 
    counter+=1
    print(counter)
    await client.get_channel(903768737608499220).send(update)


background2.start()
''' run loop and listen for reddit posts '''
client.loop.create_task(my_background_task())



''' run the bot '''
client.run(TOKEN)
