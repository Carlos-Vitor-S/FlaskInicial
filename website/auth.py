


from flask import Blueprint, render_template
from flask import request

auth = Blueprint('auth',__name__)

@auth.route('/login' , methods=['GET', 'POST'])
def login():
    dados = request.form
    print(dados)
    return render_template("home.html")

@auth.route('/logout')
def logout():
    return "<p> pagina de logout</p>"

@auth.route('/sign-up')

def signup():
    return "<p> pagina de signup </p>"

@auth.route('/musicas/' , methods = ['GET'])
def musicas ():
    
    return render_template("play.html")
