from datetime import date
from flask import jsonify
from flask_restful import Resource, reqparse
from app.models.debitos import Debitos

argumentos= reqparse.RequestParser()
argumentos.add_argument('nome',type=str )
argumentos.add_argument('tipoPagamneto',type =float )
argumentos.add_argument('data',type = date )
argumentos.add_argument('status',type = bool )
argumentos.add_argument('descriçao',type = str )

class Index(Resource):
    def get(self):
        return jsonify('Seja bem vindo a minha api de gestão')
class CriaçaoDeDebito(Resource):
    def post(self):
        try:
            datas = argumentos.parse_args()
            print (datas)
            Debitos.save_products(self, datas['nome'],
                                  datas['tipoPagamento'],
                                  datas['data'],
                                  datas['status'],
                                  datas['descriçao'])
            return {"message": 'servidor criado com sucesso'},201
        except Exception as e:
            return jsonify({'status':500, 'msg': f'{e}'}),500