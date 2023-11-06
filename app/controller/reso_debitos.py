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

atualizar_argumentos= reqparse.RequestParser()
atualizar_argumentos.add_argument("id",type=int)
atualizar_argumentos.add_argument("nome",type=str)
atualizar_argumentos.add_argument("data",type=date)
atualizar_argumentos.add_argument("status",type=bool)
atualizar_argumentos.add_argument("descriçao",type=str)

argumentos_deletar = reqparse.RequestParser()#definir os argumentos da solicitação HTTP
argumentos_deletar.add_argument('id', type=int)

class Index(Resource):
    def get(self):
        return jsonify('Seja bem vindo a minha api de gestão')
class CriaçaoDeDebito(Resource):
    def AddDebitos(self):
        try:
            datas = argumentos.parse_args()
            print (datas)
            Debitos.salvar_debitos(self, datas['nome'],
                                  datas['tipoPagamento'],
                                  datas['data'],
                                  datas['status'],
                                  datas['descriçao'])
            return {"mensagem": 'servidor criado com sucesso'},201
        except Exception as e:
            return jsonify({'status':500, 'msg': f'{e}'}),500
class AtualizarDebitoo(Resource):
    def put(self):
        try:
            datas= atualizar_argumentos.parse_args()
            atualizar = Debitos.atualizar_produtos(self,datas["id"],
                                                   datas["nome"],
                                                   datas["tipoPagamento"],
                                                   datas["data"],
                                                   datas["status"],
                                                   datas["descriçao"])
            return jsonify({"mensagem": "produto atualizado com sucesso"}), 200
        
        except Exception as e:
            return jsonify({'status': 500, 'mensagem': f'{e}'}), 500
class DeletarDebito:
 def deletar(self):
        try:
            datas = argumentos_deletar.parse_args()
            deletar = Debitos.deletar_debito(self, datas['id'])
            return {"message": 'Products delete successfully!'}, 200    
        except Exception as e:
            return jsonify({'status': 500, 'msg': f'{e}'}), 500          