import sys

import requests



r = requests.get("http://www.contenttree.my")
print(r.status_code)
print(r.ok)
