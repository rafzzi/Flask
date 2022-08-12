from flask import Flask, render_template, request, redirect, session, flash, \
    url_for


app = Flask(__name__)
app.secret_key = 'afiga'

class Usuario:
    def __init__(self, id, nome, senha):
        self.id = id
        self.nome = nome
        self.senha = senha

usuario1 = Usuario('raf', 'Rafael', 'afiga')
usuario2 = Usuario('tino', 'Renato', 'free')
usuario3 = Usuario('luti', 'Luciano', 'lucisn0')
user_dict = {usuario1.id: usuario1,
             usuario2.id: usuario2,
             usuario3.id: usuario3}

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('Super Mario', 'Ação', 'SNES')
jogo2 = Jogo('Pokemon Gold', 'RPG', 'GBA')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'SNES')
lista = [jogo1, jogo2, jogo3]
    
@app.route('/')
def index():
    print(request.content_type) 
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    print(request.content_type)
    return render_template('novo.html', titulo='Novo Jogo') 


@app.route('/criar', methods=['POST',])
def criar():
    print(request.content_type)
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect(url_for('index'))
    
@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', titulo='Faça seu login', proxima=proxima)

@app.route('/autenticar', methods=['POST'])
def autenticar():
    if request.form['usuario'] in user_dict:
        usuario = user_dict[request.form['usuario']]
        if usuario.senha == request.form['senha']:
            session['usuario_logado'] = usuario.id
            flash(f"{usuario.nome} logou com sucesso.")
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash("Não logado, tente novamente")
        return redirect(url_for('login'))
    
@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Usuário deslogado com sucesso.')
    return redirect(url_for('index'))


app.run(debug=True)