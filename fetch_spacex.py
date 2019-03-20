import json
import requests

from download_img import download_image

def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v3/launches/latest'

    response = requests.get(url)
    spacex_imgs = response.json()["links"]["flickr_images"]

    for url_num, url in enumerate(spacex_imgs, start=1):
        download_image(url, f'spacex{url_num}.jpg')