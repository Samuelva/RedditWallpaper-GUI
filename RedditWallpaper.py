import os
import praw
from PIL import Image
import random
import sqlite3
import sys
import urllib.request

directory = "/home/samuel/Pictures/Wallpapers/"
subreddits = ["earthporn", "spaceporn", "wallpaper", "topwalls", "wallpapers"]

def main(arg):
    conn = sqlite3.connect("Wallpaper.db")
    c = conn.cursor()
    user_agent = "python:RedditWallpapers:v2.0"
    r = praw.Reddit(user_agent=user_agent)

    if arg == "-db":
        get_from_database(conn, c, arg)
    else:
        get_from_reddit(c, r, arg)

    conn.commit()
    conn.close()


def get_from_reddit(c, r, subredditChoice):
    subreddit = r.get_subreddit(subredditChoice)

    for submission in subreddit.get_top_from_day():
        image_name = submission.url.split("/")[-1]

        if not valid_submission(c, image_name):
            continue

        try:
            urllib.request.urlretrieve(submission.url, directory+image_name)
        except urllib.error.HTTPError:
            continue

        if allowed_resolution(directory+image_name):
            change_wallpaper(directory+image_name)
            os.system("gsettings set org.gnome.desktop.background picture-uri file://%(path)s" % {'path':directory+image_name})
            os.system("gsettings set org.gnome.desktop.background picture-options wallpaper")
            c.execute("INSERT INTO wallpapers VALUES (?)", (directory+image_name,))
            break
        else:
            os.system("rm %s" % directory+image_name)
            continue

def change_wallpaper(image):
    os.system("gsettings set org.gnome.desktop.background picture-uri file://%(path)s" % {'path':image})
    os.system("gsettings set org.gnome.desktop.background picture-options wallpaper")

def get_from_database(conn, c, arg):
    for row in c.execute("SELECT * FROM wallpapers ORDER BY RANDOM() LIMIT 1"):
        change_wallpaper(row[0])

def valid_submission(c, image):
    for row in c.execute("SELECT * FROM wallpapers"):
        if image in row[0]:
            return False
    if image.split(".")[-1] in ["jpg", "png"]:
        return True
    else:
        False

def allowed_resolution(image):
    with Image.open(image) as img:
        if img.size[0] >= 1920 and img.size[1] >= 1080:
            return True
        else:
            return False

def check_connectivity():
    try:
        urllib.request.urlopen("https://google.com", timeout=1)
        return True
    except urllib.request.URLError:
        return False

if __name__ == "__main__":
    if check_connectivity():
        if sys.argv[1] == "-r" and len(sys.argv) > 2:
            main(sys.argv[2])
        elif sys.argv[1] == "-db" and len(sys.argv) == 2:
            main("-db")
        else:
            main(random.choice(subreddits))
    else:
        main("-db")