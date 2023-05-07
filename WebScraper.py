import requests
from bs4 import BeautifulSoup


#res = requests.get('https://m0nkeybra1nz.github.io/')
res = requests.get('https://www.google.com')

documentcontent = res.content

soup = BeautifulSoup(documentcontent, "html.parser")
with open("output.txt", "wb") as f:
    f.write(soup.prettify("utf-8"))
