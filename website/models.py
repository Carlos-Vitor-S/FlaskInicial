from enum import unique
from website import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Usuario(db.Model, UserMixin):
   
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150))
    cpf = db.Column(db.Integer(11),unique=True)
    endereco = db.Column(db.String(150))
    nascimento = db.Column(db.DateTime(8))
    senha = db.Column(db.String(150))

class Passageiro(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150))
    cpf = db.Column(db.Integer(11),unique=True)
    endereco = db.Column(db.String(150))
    cidade = db.Column(db.String(150))
    uf = db.Column(db.String(2))

class Motorista(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150))
    cpf = db.Column(db.Integer(11),unique=True)
    endereco = db.Column(db.String(150))
    cidade = db.Column(db.String(150))
    uf = db.Column(db.String(2))

class Veiculo(db.Model, UserMixin):
    pass

class Transporte(db.Model, UserMixin):
    pass

class Relatorio(db.Model, UserMixin):
    pass