import requests
from bs4 import BeautifulSoup

def main():
    #Open the document up and set it to html_content
    with open("output.txt", "r", encoding="utf-8") as f:
        html_content = f.read()
        #print(html_content)

    # create a BeautifulSoup object from the html
    soup = BeautifulSoup(html_content, 'html.parser')

    # find all div elements with the class "page-content-listing single-page"
    divs = soup.find_all('div', class_='page-content-listing single-page')
    
    for div in divs:
        link = div.find('a')
        if link is not None:
            print(link.text.strip())
            break  # stop searching after the first matchclear