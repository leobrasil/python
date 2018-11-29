from flask import Flask, jsonify, redirect, request, make_response, Response
import requests, json
from pymongo import MongoClient
#para trabalhar com object id do mongo
from bson import ObjectId

#re = requests.get('http://httpbin.org/ip')
#print(re.json())
app = Flask(__name__)
headers = {"Content-Type":"application/json"}

re = requests.get(
    "https://world-georss.waze.com/rtserver/web/TGeoRSS?tk=ccp_partner&ccp_partner_name=Prodam&format=JSON&acotu=true&types=traffic%2Calerts%2Cirregularities&polygon=-46.774000%2C-23.381000%3B-46.876000%2C-23.529000%3B-46.895000%2C-23.702000%3B-46.835000%2C-23.800000%3B-46.715000%2C-23.854000%3B-46.538000%2C-23.855000%3B-46.431000%2C-23.786000%3B-46.335000%2C-23.684000%3B-46.283000%2C-23.591000%3B-46.272000%2C-23.502000%3B-46.284000%2C-23.426000%3B-46.387000%2C-23.343000%3B-46.512000%2C-23.344000%3B-46.623000%2C-23.402000%3B-46.774000%2C-23.381000%3B-46.774000%2C-23.381000"
)

#print(re.json())
aux = (re.json())
for k in aux:
    print(k,type(aux[k]))

#print(len(aux['alerts']))

try:
    #pode ser passado usuario e senha
    client = MongoClient()
    #conenctando na base de dados: python
    db = client['python']
except Exception as e:
    print(e)
    exit()

#db.alerts.insert(aux['alerts'])
print(type(aux['alerts'][0]))
count = 0 
for i in aux['alerts']:
    alert = {"_id":i['uuid']}
    alert.update(i)
    #for k in i.keys():
        
    try:
        db.alerts.insert_one(alert)
    except Exception:
        count +=1
        pass

print(count,' alerts repetidos')
