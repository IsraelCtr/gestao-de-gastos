from app import db
class Debitos(db.Model):
    __tablename__ =  'debito'
    __table_args__ = {'sqlite_autoincrement':True} 
    id = db.colms(db.Integer,primary_key=True)
    nome = db.colums(db.String(255))
    tipoPagamento = (db.colums.Float)
    data = (db.colums.Date)
    status= (db.colums.Bolean)
    descriçao=(db.colums.String(255))
    
    def __init__(self,nome,tipoPagamneto,data,status,descriçao):
        self.nome = nome
        self.tipoPagamneto =tipoPagamneto       
        self.data = data       
        self.status = status       
        self.descriçao = descriçao       

    def json(self):
        return{
            'nome': self.nome,
            'tipopagamento': self.tipoPagamneto,
            'data': self.data,
            'status': self.status,
            'descriçao': self.descriçao
        }
    def salvar_debitos(self,nome,tipoPagamneto,data,status,descriçao):
        try:
            add_banco = Debitos(nome,tipoPagamneto,data,status,descriçao)
            db.session.add(add_banco)
            db.session.commit()
        except Exception as e:
            print(e)