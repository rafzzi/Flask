from jogoteca1 import app
from helpers import FormularioUsuario
from models import Usuarios
from flask import render_template,\
    request, redirect, session, flash, url_for
from flask_bcrypt import check_password_hash


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    form = FormularioUsuario()
    return render_template('login.html', titulo='Faça seu login',
                           proxima=proxima, form=form)

@app.route('/autenticar', methods=['POST'])
def autenticar():
    form = FormularioUsuario(request.form)
    usuario = Usuarios.query.filter_by(username=form.username.data).first()
    senha = check_password_hash(usuario.senha, form.senha.data)
    print(request.form)
    if usuario and senha: 
        session['usuario_logado'] = usuario.username
        flash(f"{usuario.nome} logou com sucesso.")
        proxima_pagina = request.form['proxima']
        return redirect(proxima_pagina)
    flash("Não logado, tente novamente")
    return redirect(url_for('login'))
    
@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Usuário deslogado com sucesso.')
    return redirect(url_for('index'))