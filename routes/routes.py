from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.debitos import Debitos


debitos= Blueprint("debitos",__name__)
@debitos.route("/")
 
def index():
 debito= Debitos.querry.all()
 return rendertemplate("index.html",nome=debito)