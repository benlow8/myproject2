import sys

import requests

print(sys.version)
print(sys.executable)

r = requests.get("https://www.contenttree.my")
print(r.status_code)

