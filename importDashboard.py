import requests
import json
import ndjson

url = "http://127.0.0.1:5601/api/kibana/dashboards/export?dashboard=b7551620-e959-11eb-9b98-25e9151151c6"
headers = {"Content-Type": "application/x-ndjson"}

res = requests.get(url)
data = res.json()

# print(data)

# with open('sample.ndjson', 'w') as f:
# 	ndjson.dump(data["objects"], f)

with open('sample.json', 'w') as f:
	json.dump(data, f)

print("Dashboard dowloaded!")

