from flask import Blueprint, jsonify

usuario = Blueprint('usuario',__name__,url_prefix='/usuario')

users = [
    {'nome':'teste0', 'idade':'10'},
    {'nome':'teste1', 'idade':'11'},
    {'nome':'teste2', 'idade':'12'}
]

@usuario.route('/')
def get_usuarios():
    return jsonify(users)

@usuario.route('/<int:idUser>')
def get_usuarios_por_id(idUser):
    return jsonify(users[idUser])

