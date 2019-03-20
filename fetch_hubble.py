import requests

from download_img import download_image

def get_file_extension(url):
    extension = url.split('.')[-1]
    return extension


def download_hubble_images(image_id):
    url = f'http://hubblesite.org/api/v3/image/{image_id}'
    image_urls = []

    response = requests.get(url)
    response = response.json()['image_files']

    for image_url in response:
        image_urls.append(image_url['file_url'])
    
    extension = get_file_extension(image_urls[-1])
    download_image(image_urls[-1], f'{image_id}.{extension}')

def get_images_id_collections(collection_name):
    url= 'http://hubblesite.org/api/v3/images'
    params = {
        'collection_name' : collection_name
    }

    response = requests.get(url, params=params)

    for image_id in response.json():
        download_hubble_images(image_id['id'])