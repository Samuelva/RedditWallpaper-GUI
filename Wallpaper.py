import os
import praw

class Wallpaper(object):
    def __init__(self):
        user_agent = "pythonRedditWallpaper:v4.0"
        
        self.r = praw.Reddit(user_agent=user_agent)
        self.subreddit = "Wallpaper"
        self.submission = "week"
        self.resolution = "1920x1080"
        