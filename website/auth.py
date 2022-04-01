from flask import Blueprint, render_template, request , flash , redirect, url_for
from flask import request

auth = Blueprint('auth',__name__)

@auth.route('/', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['cpf'] == '99999999999' and request.form['senha'] == 'admin':
            return redirect(url_for('views.home'))
            
        else:
            flash('Dados invalidos')
            
    return render_template('login.html', error=error)
    '''
    metodo = request.method
    if metodo == 'POST':
        cpf = request.form['cpf']
        senha = request.form['senha']
        if cpf == '99999999999' and senha == 'admin':
            return render_template('home.html')
        else:
            return error == 'false'
    else:
    #senha = request.form['senha']
    #cpf = request.form['cpf']
    #if request.method == 'POST':
        #if senha == 'admin' and cpf == '99999999999':
            #return render_template("home.html")
        return render_template('login.html', error=error) '''

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

@auth.route('/transporte/', methods=['GET','POST'])
def transporte():

    return render_template('transporte.html')

@auth.route('/relatorios/', methods=['GET','POST'])
def relatorios():

    return render_template('relatorios.html')

