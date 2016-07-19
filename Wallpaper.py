import os
import praw

class Wallpaper(object):
    def __init__(self):
        user_agent = "pythonRedditWallpaper:v4.0"
        
        self.r = praw.Reddit(user_agent=user_agent)
        self.subreddit = "Wallpaper"
        self.submission = "Week"
        self.resolution = "1920x1080"
        self.imageCount = 0
        self.imageList = []
        self.currentImage = ""

    def getWallpapers(self):
        self.retrievedSubreddit = self.r.get_subreddit(self.subreddit)

        if self.submission == "Day":
            self.submissions = self.retrievedSubreddit.get_top_from_day(limit=10)
        elif self.submission == "Week":
            self.submissions = self.retrievedSubreddit.get_top_from_week(limit=10)
        elif self.submission == "Month":
            self.submissions = self.retrievedSubreddit.get_top_from_month(limit=15)
        elif self.submission == "Year":
            self.submissions = self.retrievedSubreddit.get_top_from_year(limit=25)
        elif self.submission == "All":
            self.submissions = self.retrievedSubreddit.get_top_from_all(limit=25)

        for kek in self.submissions:
            print(kek.url)
        

        