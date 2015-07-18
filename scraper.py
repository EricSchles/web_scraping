import requests
import json
import lxml.html
#Example 1

#r = requests.get("http://104.131.203.11:12000/get_data")
#print json.loads(r.text)

def grabber(links,depth=10):
    for i in links:
        try:
            print i
            if i.startswith("http"):
                r = requests.get(i)
                html = lxml.html.fromstring(r.text)
                for link in html.xpath("//a/@href"):
                    if not link in links:
                        links.append(link)
            else:
                grabber(links,depth-1)
        except:
            grabber(links,depth-1)
    if depth != 0:
        grabber(links,depth-1)
    if depth==0:
        return links
r = requests.get("https://www.google.com")
html = lxml.html.fromstring(r.text)
links = html.xpath("//a/@href")
print grabber(links,depth=2)
