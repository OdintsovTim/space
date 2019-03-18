import os
import requests


def download_images(url, filename):
    filename = 'images/' + filename

    if not os.path.exists('images'):
        os.makedirs('images')

    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)









