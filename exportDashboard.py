import requests
import json
import urllib
import ndjson

# f = open('imported.ndjson')
# f = open('sample.ndjson')

# ndjson_data = ndjson.load(f)

# print(ndjson_data)

# url = "http://127.0.0.1:5601/api/kibana/dashboards/import"

# url = "http://127.0.0.1:5601/api/saved_objects/_import"
# headers = {'Content-Type': 'application/json', 'kbn-xsrf': 'true'}

# for doc in ndjson_data:
# 	requests.post(url, data = doc, headers=headers)


json_file = "sample.json"
headers = {'Content-Type': 'application/json', 'kbn-xsrf': 'true'}

with open(json_file, 'r') as f:
    data = f.read()

json_data = json.loads(data)

# print(json_data)

url = 'http://localhost:5601/api/kibana/dashboards/import?exclude=some-pattern' 

requests.post(url, headers=headers, json=json_data)

print("Dashboard sent!")

# curl -X POST http://127.0.0.1:5601/api/saved_objects/_import -H "kbn-xsrf: true" --form file=@imported.ndjson