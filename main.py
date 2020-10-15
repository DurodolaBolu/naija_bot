import tweepy
import time
import logging
from config import create_api

logging.basicConfig(level=logging.INFO)

api = create_api()
me = api.me()
search_word = f'''"#EndPoliceBrutalityinNigeria" OR "#EndSWAT" OR "#EndBadGoveranceInNigeria", "#SWATMUSTEND" OR "#SARSHASENDED" OR "##EndSARS "
               OR "#EndSARS" -filter:retweets'''

new_since_id = []
since_id_filename = 'since_id.txt'
def get_last_since_id(filename):
    f_read = open(filename, 'r')
    last_id = int(f_read.read().strip())
    f_read.close()
    return last_id

def save_last_since_id(filename, last_id):
    f_write = open(filename, 'w')
    f_write.write(str(last_id))
    f_write.close()
    return

def retweet():
    last_id = get_last_since_id(since_id_filename)
    tweet =api.search(q=search_word,since=last_id, lang = 'en', tweet_mode='extended')
    for t in reversed(tweet):
        if t.user.id == me or t.favorited == True or t.retweeted == True:
            continue
        else:
            try:
                logging.info(f'found a tweet by @{t.user.screen_name}')
                t.retweet()
                t.favorite()
                logging.info(f'Successfully liked and retweeted post made by @{t.user.screen_name}')
            except tweepy.TweepError:
                logging.error(f'Error while liking and retweeting', exc_info = True)
        new_since_id.append(t.id)
        time.sleep(10)
    else:
        logging.info('Done checking for tweets')
    if len(new_since_id) != 0:
        save_last_since_id(since_id_filename,max(new_since_id))
        new_since_id.clear()

while True:
    retweet()
    logging.info('Bot Temporarily de-activated')
    time.sleep(300)

