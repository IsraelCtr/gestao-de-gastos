from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.debitos import Debitos
from util.db import db


opf= Blueprint("debitos",__name__)
@opf.route("/")
 
def index():
 debito= Debitos.querry.all()
 return render_template("index.html",nome=debito)

@opf.route("/novo")
def adddebito():
 return "adicionar conta"

@opf.route("/deletar")
def DeletarDebito():
 return "deletar conta"
@opf.route("/atualizar")
def AtualizarConta():
 return "deletar conta"