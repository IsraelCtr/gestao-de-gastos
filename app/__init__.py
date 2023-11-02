from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api 

app=Flask(__name__)
api= Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crudgestao.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from app.models.debitos import Debitos
with app.app_context():
    db.create_all()
from app.controller.reso_products import Index,CriaçaoDeDebito
api.add_resource(Index,'/')
api.add_resource(CriaçaoDeDebito,'/criar')

