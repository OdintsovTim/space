import os

from instabot import Bot

import settings

from fetch_hubble import download_hubble_images
from fetch_spacex import fetch_spacex_last_launch

def main():
    fetch_spacex_last_launch()
    download_hubble_images('spacecraft')
    myfiles = os.listdir('images')
    bot = Bot()
    bot.login(username=settings.LOGIN, password=settings.PASSWORD)

    for image in myfiles:
        if image != '.DS_Store':
            bot.upload_photo(f'images/{image}')

if __name__ == "__main__":
    main()   