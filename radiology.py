
from bs4 import BeautifulSoup as bs
import urllib.request
import os.path
import csv

file_path = "radiology.html"
content_file = ""

if not os.path.isfile(file_path):
    download = urllib.request.urlretrieve("https://www.mayoclinic.org/departments-centers/radiology/sections/tests-procedures/orc-20469692", file_path)

with open(file_path, "r") as file:
    content_file = file.read()

soup = bs(content_file, "html.parser")
content = soup.find("article", {"id": "main-content"})
content = content.find("div", {"class": "titlelist"})

rows = list(map(lambda x: x.text.strip(),content.find_all("li")))
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

with open("radiology.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(fields)
    writer.writerows(map(lambda x: [x], rows))



