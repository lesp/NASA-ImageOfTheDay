import requests
url = "https://api.nasa.gov/planetary/apod?api_key=PUT YOUR API KEY HERE"
r = requests.get(url)
if r:
    APOD = r.json()['url']
    pic = requests.get(APOD, allow_redirects=True)
    open('/home/les/Pictures/APOD.jpg', 'wb').write(pic.content)
else:
    print("Error")
