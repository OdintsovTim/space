import os
import requests


def download_image(url, filename):
    filename = 'images/' + filename

    os.makedirs('images', exist_ok=True)
    response = requests.get(url, verify=False)

    with open(filename, 'wb') as f:
        f.write(response.content)
