
from flask import Flask, render_template, request, redirect, session, flash, url_for


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('Goo of War', 'Rack n Slash', 'PS2')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS2')
jogo4 = Jogo('EuroTruck', 'Simulador', 'PS3')

lista = [jogo1, jogo2, jogo3, jogo4]


class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha


ususario1 = Usuario("Gustavo Cardoso", "GC", "admin123")
ususario2 = Usuario("Alexandre G Moraes", "34218417806", "mudar@123")
ususario3 = Usuario("Margareth Tebas", "28973326899", "mudar@123")

usuarios = {
    ususario1.nickname: ususario1,
    ususario2.nickname: ususario2,
    ususario3.nickname: ususario3, }


app = Flask(__name__)
app.secret_key = 'gustavo'


@app.route('/')
def index():
    return render_template('lista.html', titulo='jogos', jogos=lista)


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='novo jogo')


@app.route('/criar', methods=['POST', ])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect(url_for('index'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[ request.form['usuario'] ]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash( usuario.nome + ' logado com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Usuário não logado.')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))


app.run(debug=True, host='0.0.0.0', port=8080)
