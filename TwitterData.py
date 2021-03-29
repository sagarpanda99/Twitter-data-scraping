# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 13:24:17 2021

@author: panda
"""

import json
import csv
import tweepy
import re
import pandas as pd

def search_for_hashtags(consumer_key,consumer_secret,access_token,access_token_secret,hashtag_phrase):
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    
    api = tweepy.API(auth)
    fname = hashtag_phrase
    
    print("COLLECTING TWITTER DATA.....")
    print("Please wait...")
    # Creating DataFrame using pandas
    
    
    
    db = pd.DataFrame(columns=['Username', 'Description', 'Location', 'Following',
                               'Followers', 'Totaltweets', 'Retweetcount', 'Text', 'Hashtags'])
    tweets = tweepy.Cursor(api.search, q=hashtag_phrase, lang="en",
                            geocode="29.3117,47.4818,2500km",tweet_mode='extended').items(500)
    
    # We are using .Cursor() to search through twitter for the required tweets.
    # The number of tweets can be restricted using .items(number of tweets)
    
    # .Cursor() returns an iterable object. Each item
    list_tweets = [tweet for tweet in tweets]
    
    # Counter to maintain Tweet Count
    
    i = 1 
    
    # we will iterate over each tweet in the list for extracting information about each tweet
    
    
    for tweet in list_tweets:
        username = tweet.user.screen_name
        description = tweet.user.description
        location = tweet.user.location
        following = tweet.user.friends_count
        followers = tweet.user.followers_count
        totaltweets = tweet.user.statuses_count
        retweetcount = tweet.retweet_count
        hashtags = tweet.entities['hashtags']
        
        # Retweets can be distinguished by a retweeted_status attribute,
        # in case it is an invalid reference, except block will be executed
        try:
            text = tweet.retweeted_status.full_text
        except AttributeError:
            text = tweet.full_text
        hashtext = list()
        for j in range(0, len(hashtags)):
            hashtext.append(hashtags[j]['text'])
        #Here we are appending all the extracted information in the DataFrame 
        
        
        ith_tweet = [username, description, location, following,
                     followers, totaltweets, retweetcount, text, hashtext]
        db.loc[len(db)] = ith_tweet
        
        i = i+1
        
        # Giving name to CSV File 
        
        
        filename = hashtag_phrase+'.csv'
        # we will save our database as a CSV file.
    
        db.to_csv(filename)
    
    print("Data Retrived Succesfully...")
    print("Kindly Check Your Current Directory .")
    print(" THANK YOU ")

#Twitter developer access portal credentialss


consumer_key = input("Enter your Consumer Key : ")
consumer_secret = input("Enter your Consumer Secret : ")
access_token = input("Enter your Access Token : ")
access_token_secret = input("Enter your Access Token Secret : ")
hashtag_phrase = input("Enter the Hashtag to collect data : ")


if __name__ == '__main__':
    search_for_hashtags(consumer_key, consumer_secret, access_token, access_token_secret, hashtag_phrase)
        