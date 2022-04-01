from flask import Blueprint, render_template, request , flash , redirect, url_for
from flask import request

auth = Blueprint('auth',__name__)

@auth.route('/', methods=['GET','POST'])
def login():
    
    return render_template("login.html")


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.form == 'POST':
        nome = request.form.get('nome')
        cpf = request.form.get('cpf')
        endereco = request.form.get('endereco')
        nascimento = request.form.get('nascimento')
        senha1 = request.form.get('senha1')
        senha2 = request.form.get('senha2')
        
        if len(cpf) != 11:
            flash("Cpf deve conter 11 digitos",category='error')
        elif senha2 != senha1:
            flash("As senhas digitadas não sao iguais", category='error')
        else:
            flash("Cadastro feito com sucesso" , category='success')
           
    return render_template('signup.html')

@auth.route('/passageiros/', methods=['GET','POST'])
def passageiros():
    return render_template('passageiros.html')


@auth.route('/motoristas/', methods=['GET','POST'])
def motoristas():
    return render_template('motoristas.html')


@auth.route('/veiculos/', methods=['GET','POST'])
def veiculos():

    return render_template('veiculos.html')

@auth.route('/transportes/', methods=['GET','POST'])
def transportes():

    return render_template('transporte.html')

@auth.route('/relatorios/', methods=['GET','POST'])
def relatorios():

    return render_template('relatorios.html')

