from flask import Flask, render_template, request, redirect, url_for, flash
from app.models.debitos import Debitos
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app=Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crudgestao.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
from app.models.debitos import Products
with app.app_context():
    db.create_all

from app.controller.reso_debitos import Index, CriaçaoDeDebito,AtualizarDebitoo,DeletarDebito
api.add_resource(Index, '/')
api.add_resource(CriaçaoDeDebito, '/criar')
api.add_resource(AtualizarDebitoo, '/atualizar')
api.add_resource(DeletarDebito, '/deletar')