# Space Instagram

This program downloads photos of the last SpaceX rocket launch and from the collection "spacecraft" (you can choose your collection) 
and post them on your Instagram

### How to install

You need to introduce login and passoword of your instargram in terminal
```
$ python main.py your_login your_password
```

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

If you want to change collection, you need open file main.py and change it:
```
download_hubble_images('your collection')
```
