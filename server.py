import requests
import json
import time

# http
url = 'http://127.0.0.1:8080'

# upload a message
# data = "string log value"

# requests.post(url, data = data)

# upload json

# class Logstash:
#     def __init__(self, url):
#         self.url = url

f = open('csvjson.json')

json_data = json.load(f)

# requests.post(url, json = json_data)

count = 0
for i in json_data:
    requests.post(url, json = i)
    count += 1
    print(count)
    # if count == 2000:
    #     print("Reached 2000 sleeping.....")
    #     time.sleep(10)
    #     count = 0

# upload csv 

print("successful")