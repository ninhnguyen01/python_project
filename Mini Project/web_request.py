import requests

url_page = "Enter URL here"
response = requests.get(url_page)

if response.status_code == 200:
    print("Successful ping!")
    print()
    print(response.headers)    
    print()
    print(response.text)
    print()
