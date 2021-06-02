from credentials import CONSUMER_SECRET
import tweepy
import webbrowser
import time

CONSUMER_KEY = 
CONSUMER_SECRET = 

callback_uri = 'oob'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET, callback_uri)
redirect_url = auth.get_authorization_url()
print(redirect_url)

webbrowser.open(redirect_url)

user_pint_input = input("What's the pin value?:")

auth.get_access_token(user_pint_input)

api = tweepy.API(auth)

me = api.me()
optn = input("with media or without media:")
optn = optn.lower()
if optn == "without media":
    status = input("enter tweet:")
    new_status = api.update_status(status)
else:
    status = input("enter caption:")
    img_path = input("enter the path of the img:")
    img_obj = api.media_upload(img_path)
    new_status = api.update_status(status, media_ids=[img_obj.media_id_string])







