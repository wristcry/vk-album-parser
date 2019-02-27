# -*- coding: utf-8 -*-
import vk_api
import requests
import os
try:
    import configparser
except ImportError:
    import ConfigParser as configparser
 
config = configparser.ConfigParser()

def createConfig(path):
    config.add_section("Configuration")
    config.set("Configuration", "Login", "login")
    config.set("Configuration", "Password", "password")
    config.set("Configuration", "Group_URL", "daydream325")
    with open(path, "w") as config_file:
        config.write(config_file)

config.read("Configuration.ini")
if __name__ == "__main__":
    path = "Configuration.ini"
    if not os.path.exists(path):
        createConfig(path)

LOGIN = config.get("Configuration", "Login")
PASSWORD = config.get("Configuration", "Password")
GROUP_URL = config.get("Configuration", "Group_URL")

def authorization():
	vk_session = vk_api.VkApi(LOGIN, PASSWORD)
	try:
		vk_session.auth()
	except vk_api.AuthError as error_msg:
		print(error_msg)
		return
	return vk_session.get_api()

def main():
    vk = authorization()
    group = vk.groups.getById(group_id=GROUP_URL)[0]['id']
    photoAlbums = vk.photos.getAlbums(owner_id = "-"+str(group))['items']
    for album in photoAlbums:
        i = 0
        if not os.path.exists("parsed/"+album['title']):
            os.makedirs("parsed/"+album['title'])
        photos = vk.photos.get(owner_id = "-"+str(group), album_id = album['id'], photo_sizes = 1, count = 1000)['items']
        for photo in photos:
            try:
                biggest = photo['sizes'][0]['width']
                biggestSrc = photo['sizes'][0]['url']
            except IndexError:
                continue
            for size in photo['sizes']:
                if size['width'] > biggest:
                    try:
                        biggest = size['width']
                        biggestSrc = size['url']
                    except IndexError:
                        continue
            content = requests.get(biggestSrc).content
            try:
                with open("parsed/"+album['title']+"/"+str(i)+".jpg", "wb") as f:
                    f.write(content)
            except FileNotFoundError:
                continue
            print("parsed/"+album['title']+"/"+str(i)+".jpg")
            i = i + 1

if __name__ == "__main__":
    main()