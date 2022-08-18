# Flask

Projeto de uma web app usando Flask com as features:
- Conexão com MySQL através do ORM SQLAlchemy
- Controle de validação de formulários com proteção CRSF
- Admin session para manutenção do banco de dados (funcionalidades CRUD)
- Proteção de senhas com BCrypt (password hash)

## Files
### prepara_banco.py
Inicialização do banco de dados contendo alguns dados exemplo.
Necessária a instalação do MySQL e MySQL server, ao criar um usuário e senha, editar na inicialização da conexão.

### jogoteca1.py
Inicialização do app Flask e das funcionalidades (SQLALchemy, CSRFProtect, BCrypt).

### views_game.py
Rotas relativas a criação, visualização, edição e deleção de itens.

### views_user.py
Rotas relativas a login e logout de usuários.

### models.py
Modelos ORM (Object-Relational-Mapping) para conversão das classes (Python) em dados para o banco (SQL).

### helpers.py
helpers para a funcionalidade adequada da aplicação.

### config.py
Inicialização de algumas variáveis globais.

### /uploads/
Arquivos de imagens (padrão + uploads do usuário pelos formulários da aplicação)

### /static/
Arquivos css e js

### /templates/
Arquivos html

### requirements.txt
Arquivo contendo as versões das bibliotecas utilizadas. Para rodar a aplicação:
- Faça o Download do MySQL e do Python3.
- Na pasta onde estão os arquivos extraidos, execute
<code>
python3 -m venv venv
</code>
<br><br><code>
source venv/bin/activate
</code>
<br><br><code>
pip install -r requirements.txt
</code>
<br><br><code>
python3 prepara_banco.py
</code>
<br><br><code>
python3 jogoteca1.py
</code>



