import mysql.connector
from mysql.connector import errorcode
from flask_bcrypt import generate_password_hash

print('Conectando...')

try:    
    conn = mysql.connector.connect(
        user='root', 
        host='127.0.0.1',
        password='password')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Existe algo errado no nome de usuário ou senha')
    else:
        print(err)
        
cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `jogoteca`;")
cursor.execute("CREATE DATABASE `jogoteca`;")
cursor.execute("USE `jogoteca`")

#criando tabelas
TABLES = {}
TABLES['Jogos'] = ('''
                   CREATE TABLE `jogos` (
                       `id` int(11) NOT NULL AUTO_INCREMENT,
                       `nome` varchar(50) NOT NULL,
                       `categoria` varchar(40) NOT NULL,
                       `console` varchar(20) NOT NULL,
                       PRIMARY KEY (`id`)
                    )
                    ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
                   ''')
TABLES['Usuarios'] = ('''
                   CREATE TABLE `usuarios` (
                       `nome` varchar(20) NOT NULL,
                       `username` varchar(8) NOT NULL,
                       `senha` varchar(100) NOT NULL,
                       PRIMARY KEY (`username`)
                    )
                    ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
                   ''')
    
for tb in TABLES:
    tb_sql = TABLES[tb]
    try:
        print(f'Criando tabela {tb}', end=' ')
        cursor.execute(tb_sql)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print('Já existe')
        else:
            print(err.msg)
    else:
        print('OK')
        
        
#inserindo usuários
usuario_sql = 'INSERT INTO usuarios (nome, username, senha) VALUES (%s, %s, %s)'
usuarios = [
    ('Rafael', 'raf', generate_password_hash('afiga').decode('utf-8')),
    ('Renato', 'tino', generate_password_hash('free').decode('utf-8')),
    ('Luciano', 'luti', generate_password_hash('lucisn0').decode('utf-8'))
]
cursor.executemany(usuario_sql, usuarios)

cursor.execute('SELECT * FROM jogoteca.usuarios')

print('----- USUÁRIOS -----')
for user in cursor.fetchall():
    print(user[1])
    
#inserindo jogos
jogos_sql = 'INSERT INTO jogos (nome, categoria, console) VALUES (%s, %s, %s)'
jogos = [
    ('Super Mario', 'Ação', 'SNES'),
    ('Pokemon Gold', 'RPG', 'GBA'),
    ('Mortal Kombat', 'Luta', 'SNES')
]
cursor.executemany(jogos_sql, jogos)

cursor.execute('SELECT * FROM jogos')

print('-----  JOGOS     ------')
for jogo in cursor.fetchall():
    print(jogo[1])


conn.commit()
cursor.close()