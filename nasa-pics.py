#! /usr/bin/env python3
import requests
import notify2
notify2.init("NASA Astronomy Picture of the Day")
url = "https://api.nasa.gov/planetary/apod?api_key=YOUR API KEY HERE"
r = requests.get(url)
if r:
    APOD = r.json()['url']
    pic = requests.get(APOD, allow_redirects=True)
    if  "jpg" not in APOD:
        n = notify2.Notification("No image for today, must be a YouTube video")
        n.show()
    else:
        open('/home/les/Pictures/APOD.jpg', 'wb').write(pic.content)
        n = notify2.Notification("Enjoy todays image")
        n.show()
else:
    print("Error")
