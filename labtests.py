
from bs4 import BeautifulSoup as bs
import urllib.request
import os.path
import csv

file_path = "content.html"
content_file = ""

if not os.path.isfile(file_path):
    download = urllib.request.urlretrieve("https://www.laboratoryalliance.com/tests/alpha/", file_path)

with open(file_path, "r") as file:
    content_file = file.read()

soup = bs(content_file, "html.parser")
content = soup.find("section", {"id": "content"})

rows = list(map(lambda x: x.text,content.find_all("li")))
print(len(rows))
result=[]

marker = set()

for l in rows:
    ll = l.lower()
    if ll not in marker:   # test presence
        marker.add(ll)
        result.append(l)   # preserve order

rows = result
print(len(rows))

fields = ["test_name"]

with open("labtests.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(fields)
    writer.writerows(map(lambda x: [x], rows))



