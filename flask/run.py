from flask import Flask, jsonify, redirect, request, make_response, Response
import requests, json
from modulos.usuarios import usuario
from modulos.view import view

#passando o contexto com o atributo do arquivo __name__
app = Flask(__name__)
app.register_blueprint(usuario)
app.register_blueprint(view)

@app.route('/', methods=['GET'])
def index():
    mensagem = {'mensagem':'valor'}
    headers = {'cabecalho':'valor do cab'}
    #return jsonify(mensagem)
    #para manipular o status de retorno
    return make_response(jsonify(mensagem),301,headers)

@app.route('/', methods=['POST'])
def indexPost():

    parametro = request.get_json()
    print(parametro)
    return redirect('/')



@app.route('/cep')
def buscar_end():
    re = requests.get('http://httpbin.org/ip')
    return jsonify(re.json())

@app.route('/cep2/<string:busca>')
def buscar_end2(busca):
    re = requests.get('http://viacep.com.br/ws/{}/json'.format(busca))
    return jsonify(re.json())

#passando parametro na url
@app.route('/rota/<string:dinamico>/<int:numero1>/<int:numero2>')
def rota_dinamico(dinamico, numero1, numero2):
    soma = numero1+numero2
    return str(soma)

if __name__ == '__main__':
    #host0.0.0.0 libera o acesso externo para todas as maquinas
    app.run(host='0.0.0.0', debug='true', port=5000)