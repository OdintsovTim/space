import requests

from download_img import download_image


def get_file_extension(url):
    extension = url.split('.')[-1]
    return extension


def download_hubble_images(image_id):
    url = f'http://hubblesite.org/api/v3/image/{image_id}'

    response = requests.get(url)
    response = response.json()['image_files']

    for image in response:
        image_url = 'http:' + image['file_url']
        extension = get_file_extension(image_url)
        download_image(image_url, f'{image_id}.{extension}')


def get_images_id_collections(collection_name):
    url = 'http://hubblesite.org/api/v3/images'
    params = {
        'collection_name': collection_name
    }

    response = requests.get(url, params=params)

    for image in response.json():
        download_hubble_images(image['id'])
