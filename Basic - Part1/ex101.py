import requests


url = "https://www.baidu.com"
response = requests.post(url)
print(response.text)
