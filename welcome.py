import requests

r = requests.get("https://www.cemtech.biz")
print(r.status_code)