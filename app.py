from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoas, Atividades

app = Flask(__name__)
api = Api(app)


class Pessoa(Resource):
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                    'nome': pessoa.nome,
                    'idade': pessoa.idade,
                    'id': pessoa.id }

        except AttributeError:
               response={
                   'status':'error',
                   'mensagem:':'Pessoa não encontrada'
               }
        return response

    def put(self,nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json

        if 'nome' in dados:
             pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.save()

        response = {
            'id':pessoa.id,
            'nome':pessoa.nome,
            'idade':pessoa.idade
        }
        return response

    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        pessoa.delete()
        mensagem = 'Pessoa excluida com sucesso.'
        return{'status':'sucesso', 'mensagem':mensagem}


class ListPessoas(Resource):
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{'id':i.id, 'nome':i.nome, 'idade':i.idade} for i in pessoas]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        response = {
            'id':pessoa.id,
            'nome':pessoa.nome,
            'idade':pessoa.idade
        }
        return response

class ListaAtividades(Resource):
    def get(self):
        atividades = Atividades.query.all()
        response = [{'id':i.id, 'nome':i.nome, 'pessoa':i.pessoa.nome } for i  in atividades]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
        atividade.save()
        response = {
            'pessoa':atividade.pessoa.nome,
            'nome':atividade.nome,
            'id':atividade.id
        }
        return response

    def put(self,id):
        atividade = Atividades.query.filter_by(id=id).first()
        dados = request.json
        if 'nome' in dados:
            atividade.nome = dados['nome']
        if 'pessoa' in dados:
            pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
            atividade.pessoa = pessoa
        atividade.save()
        response = {
            'id': atividade.id,
            'nome': atividade.nome,
            'pessoa': atividade.pessoa.nome
        }
        return response



api.add_resource(Pessoa, '/pessoa/<string:nome>/')
api.add_resource(ListPessoas, '/pessoa/')
api.add_resource(ListaAtividades, '/atividades/', '/atividades/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
