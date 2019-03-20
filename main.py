import argparse
import os

from instabot import Bot

import settings

from fetch_hubble import download_hubble_images
from fetch_spacex import fetch_spacex_last_launch

def main():
    parser = argparse.ArgumentParser(description='This program downloads photos of the last SpaceX rocket launch and from the collection "spacecraft" (you can choose your collection)')
    parser.add_argument('login')
    parser.add_argument('password')
    args = parser.parse_args()
    login = args.login
    password = args.password

    fetch_spacex_last_launch()
    download_hubble_images('spacecraft')
    myfiles = os.listdir('images')
    bot = Bot()
    bot.login(username=login, password=password)

    for image in myfiles:
        if image != '.DS_Store':
            bot.upload_photo(f'images/{image}')

if __name__ == "__main__":
    main()   