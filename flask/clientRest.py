import requests, json


#re = requests.get('http://httpbin.org/ip')
#print(re.json())

headers = {"Content-Type":"application/json"}
data = {'nome':'leandro'}

re = requests.post(
    "http://localhost:5000/",
    data=json.dumps(data),
    headers=headers
)
