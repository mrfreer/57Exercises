#Who's in space?

import json,urllib.request
with urllib.request.urlopen('http://api.open-notify.org/astros.json') as url:
    response = url.read()
    data = json.loads(response)

for a in data['people']:
    print(a['name'])
print(str(len(data['people'])) + ' people in space')