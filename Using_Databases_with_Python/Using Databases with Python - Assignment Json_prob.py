import urllib.request, urllib.parse, urllib.error
import json

url = 'http://py4e-data.dr-chuck.net/comments_273244.json'
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print(data)

c = 0
info = json.loads(data)
print(info)
for comment in info["comments"]:
    c = c + int(comment["count"])
print(c)
