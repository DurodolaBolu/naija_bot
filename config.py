import os
import logging
import tweepy

logging.basicConfig(level=logging.INFO)

def create_api():
    auth = tweepy.OAuthHandler('YfriDqJiS94C9ani42xyFXJrh','sRDrG3tCfmaSEOzBgFuHse5HjlTkFIBt0GzyLl1p7YNLZE2Om7')
    auth.set_access_token('1296143491391795200-qN4qHwIfaAW1aMTm1bvZYsPcJ6B3K1','YuhHQlPVELhnAKPVAmb0P62WBAwh9nKE77ygiUx6q2b15')
    api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
    except Exception as e:
        logging.error('Error creating api', exc_info=True)
        raise e
    logging.info('api created')
    return api

