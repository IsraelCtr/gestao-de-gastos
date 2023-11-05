from routes.rotas_debito import opf
from models.debitos import Debitos
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION_URI 

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crudgestao.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



if __name__ == '__main__':
    app.run(host='127.0.0.1',debug=True, port=5000)
app.register_blueprint(opf)