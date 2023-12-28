import scholarly

import json

response = scholarly.get()

response_json = json.loads(response.scholarly)

print(response_json['title'])