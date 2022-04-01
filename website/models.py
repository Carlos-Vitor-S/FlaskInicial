from enum import unique
from website import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Usuario(db.Model, UserMixin):
   
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150))
    cpf = db.Column(db.String(14),unique=True)
    endereco = db.Column(db.String(150))
    nascimento = db.Column(db.String(30))
    senha = db.Column(db.String(50))

class Passageiro(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150))
    cpf = db.Column(db.String(14),unique=True)
    endereco = db.Column(db.String(150))
    cidade = db.Column(db.String(150))
    uf = db.Column(db.String(2))
    nascimento = db.Column(db.DateTime)

class Motorista(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150))
    cpf = db.Column(db.String(14),unique=True)
    endereco = db.Column(db.String(150))
    cidade = db.Column(db.String(150))
    uf = db.Column(db.String(2))
    nascimento = db.Column(db.DateTime)

class Veiculo(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    tipoTransporte = db.Column(db.String(20))
    placa = db.Column(db.String(30), unique=True)
    marca = db.Column(db.String(150))
    modelo = db.Column(db.String(150))
    ano = db.Column(db.String(4))
    capacidade = db.Column(db.Integer)
    
    id_passageiro = db.Column(db.Integer , db.ForeignKey('motorista.id'))
    
class Transporte(db.Model , UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    dataTransporte = db.Column(db.DateTime)
    horaTransporte = db.Column(db.String(1000))
    quantidadeKm = db.Column(db.Integer)

    id_veiculo = db.Column(db.Integer, db.ForeignKey('veiculo.id'))
    id_passageiro = db.Column(db.Integer, db.ForeignKey('passageiro.id'))

