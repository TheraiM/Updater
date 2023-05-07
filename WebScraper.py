import requests

#res = requests.get('https://m0nkeybra1nz.github.io/')
res = requests.get('https://www.mangaread.org/')
#print(res.text)
#print(res.status_code)

with open("output.txt", "w") as f:
    print(res.text, file=f)
