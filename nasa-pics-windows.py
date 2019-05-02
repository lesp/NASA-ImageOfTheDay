#! /usr/bin/env python3
import requests
import ctypes
url = "https://api.nasa.gov/planetary/apod?api_key=YOUR API KEY HERE"
r = requests.get(url)
if r:
    APOD = r.json()['url']
    pic = requests.get(APOD, allow_redirects=True)
    if  "jpg" not in APOD:
        print("No image")
    else:
        open('C:\\Users\\les\\Pictures\\APOD.jpg', 'wb').write(pic.content)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Users\\les\\Pictures\\APOD.jpg" , 0)
        print("DONE")
else:
    print("Error")
