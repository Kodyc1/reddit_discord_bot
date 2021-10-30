import praw
import asyncpraw

import time
from datetime import datetime
from pytz import timezone
import pytz

from config import CLIENTID
from config import CLIENTSECRET 
from config import USERNAME
from config import PASSWORD

''' Python Reddit API Wrapper Instantiator '''
reddit = praw.Reddit(
    client_id=CLIENTID,
    client_secret=CLIENTSECRET,
    username=USERNAME,
    password=PASSWORD,
    user_agent="bot user agent",
)


''' get subreddit, search for key word, and return newest sorted by flair '''
subreddit = reddit.subreddit("frugalmalefashion")

# print(subreddit.display_name)
# print(subreddit.title)

#search = subreddit.search('common projects achilles').sort(key=lambda submission: submission.created_utc)
for submission in subreddit.search(query='common projects achilles',
                                   sort='new',
                                   time_filter='year'):
    # if flair is correct within last 6 months, print
    if submission.link_flair_text == "[Deal/Sale]" and \
        submission.created_utc > (time.time()-15552000):
            print(submission.link_flair_text)
            print(submission.title)

            timestamp = datetime.fromtimestamp(submission.created_utc)
            pacific = timestamp.astimezone(timezone("US/Pacific"))
            print("Posted on:", pacific.strftime('%m/%d/%Y %H:%M:%S %Z\n'))


''' async for discord bot '''

def stream_posts():
    reddit = asyncpraw.Reddit(
        client_id=CLIENTID,
        client_secret=CLIENTSECRET,
        user_agent="bot user agent",
    )

# read only without username/pass, read with user/pass
#print(reddit.read_only)

    ''' live stream new posts to discord '''
    subreddit = reddit.subreddit("frugalmalefashion")
    for submission in subreddit.stream.submissions():
        if submission.link_flair_text == "[Deal/Sale]": # or "common projects achilles" in submission.title:
            print(submission.title)
            timestamp = datetime.fromtimestamp(submission.created_utc)
            pacific = timestamp.astimezone(timezone("US/Pacific"))
            print("Posted on:", pacific.strftime('%m/%d/%Y %H:%M:%S %Z\n'))
