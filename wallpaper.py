import os
import praw
from PIL import Image
from PyQt4 import QtGui
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

    def get_subreddit(self):
        return self.subreddit

    def get_submissions_day(self):
        return self.subreddit.get_top_from_day(limit=10)

    def get_submissions_week(self):
        return self.subreddit.get_top_from_week()

    def get_submissions_month(self):
        return self.get_image_urls(self.subreddit.get_top_from_day(limit=10))

    def get_submissions_year(self):
        return self.subreddit.get_top_from_year()

    def get_submissions_all_time(self):
        return self.subreddit.get_top_from_all()
        
    def set_image(self, directory, imageID):
        self.image = directory+imageID
        
    def get_image(self):
        return self.image

    def get_image_urls(self, submissions):
        image_urls = []
        for submission in submissions:
            submission.url = submission.url
            submission.url = submission.url
            image_urls.append(submission.url)
        return image_urls

    def get_wallpaper_database(self):
        conn = sqlite3.connect("Wallpaper.db")
        c = conn.cursor()

        for row in c.execute("SELECT * FROM wallpapers ORDER BY RANDOM() LIMIT 1"):
            return row[0]

        conn.close()

    def get_submissions(self):
        submissionsList = []
        for submission in self.submissions:
            submissionsList.append(submission)
        return submissionsList


def main():
    test1 = RedditWallpaper("wallpapers")
    print(test1.get_wallpaper_database())

if __name__ == '__main__':
    main()

