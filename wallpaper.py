import os
import praw
from PIL import Image
import random
import sqlite3
import sys
import urllib.request

class RedditWallpaper:

    def __init__(self, subreddit):
        user_agent = "python:RedditWallpapers:v3.0"
        self.r = praw.Reddit(user_agent=user_agent)
        self.subreddit = self.r.get_subreddit(subreddit)

    def set_subreddit(self, subreddit):
        self.subreddit = self.r.get_subreddit(subreddit)

    def set_wallpaper(self, wallpaper):
        self.wallpaper = wallpaper

    def set_wallpaper_database(self, wallpaper):
        conn = sqlite3.connect("Wallpaper.db")
        c = conn.cursor()

        c.execute("INSERT INTO wallpapers VALUES (?)", (wallpaper))

        conn.commit()
        conn.close()

    def set_resolution(self, resolution):
        self.resolution = resolution
        
    def get_resolution(self):
        return self.resolution

    def get_subreddit(self):
        return self.subreddit

    def set_submissions_day(self):
        self.submissions = self.get_image_urls(self.subreddit.get_top_from_day(limit=10))

    def set_submissions_week(self):
        self.submissions = self.get_image_urls(self.subreddit.get_top_from_week(limit=10))
        
    def set_submissions_month(self):
        self.submissions = self.get_image_urls(self.subreddit.get_top_from_month(limit=10))

    def set_submissions_year(self):
        self.submissions = self.get_image_urls(self.subreddit.get_top_from_year(limit=10))

    def set_submissions_all_time(self):
        self.submissions = self.get_image_urls(self.subreddit.get_top_from_all(limit=10))
        
    def set_image(self, directory, imageID):
        self.image = directory+imageID
    
    def get_submissions(self):
        return self.submissions
    
    def get_image(self):
        return self.image

    def get_image_urls(self, submissions):
        image_urls = []
        for submission in submissions:
            submission = self.valid_image(submission.url)
            if submission == False:
                continue
            else:
                image_urls.append(submission)
        return image_urls

    def get_wallpaper_database(self):
        conn = sqlite3.connect("Wallpaper.db")
        c = conn.cursor()

        for row in c.execute("SELECT * FROM wallpapers ORDER BY RANDOM() LIMIT 1"):
            return row[0]

        conn.close()
    
    def valid_image(self, submission):
        if submission.split(".")[-1] not in ("jpg", "png"):
            return(False)
        else:
            return(submission)
          
        
def main():
    test1 = RedditWallpaper("wallpapers")
    print(test1.get_wallpaper_database())

if __name__ == '__main__':
    main()

