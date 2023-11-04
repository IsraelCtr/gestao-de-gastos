from app import db
class Debitos(db.Model):
    __tablename__ =  'debito'
    __table_args__ = {'sqlite_autoincrement':True} 
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))
    tipoPagamento = db.Column(db.Float)
    data =  db.Column(db.Date)
    status= db.Column(db.Boolean)
    descriçao= db.Column(db.String(255))
    
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