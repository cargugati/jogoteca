SECRET_KEY = 'gustavo'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = '12345',
        servidor = 'localhost',
        database = 'jogoteca'
    )