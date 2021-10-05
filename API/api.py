from flask import Flask, request
from database import *
app = Flask('cliente')

@app.route('/consulta', methods=['GET'])
def consulta():
    body = request.get_json()
    
    if ('nome' not in body):
        return 'Nome é obrigatorio'
    
    usuario_dados = red(palavra)(body['nome'])
      
    return gerar_response(body['nome'], body['idade'], 'user', usuario_dados)


def gerar_response(nome, idade, nome_conteudo=False, msg=False):
    response = {}
    response['nome'] = nome
    response['idade'] = idade
    
    if  (nome_conteudo and msg) :
        response[nome_conteudo] = msg

app.run()

