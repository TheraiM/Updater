import requests
from bs4 import BeautifulSoup

def main():
    #res = requests.get('https://m0nkeybra1nz.github.io/')

    #Pull data from the website link
    res = requests.get('https://www.mangaread.org/manga/solo-leveling-manhwa/')

    #Put the content of the data into an object
    documentcontent = res.content

    #Create soup object for the content
    soup = BeautifulSoup(documentcontent, "html.parser")

    #Write the html to a txt document
    with open("output.txt", "wb") as f:
        f.write(soup.prettify("utf-8"))