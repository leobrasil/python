from pymongo import MongoClient
#para trabalhar com object id do mongo
from bson import ObjectId

try:
    #pode ser passado usuario e senha
    client = MongoClient()
    #conenctando na base de dados: python
    db = client['python']
except Exception as e:
    print(e)
    exit()

user = {
    "nome":"Leandro",
    "sobrenome":"natale"
}
db.usuario.insert(user)

busca = db.usuario.find()
print (busca)

#convertendo em lista
busca = [x for x in busca]
print(busca)

