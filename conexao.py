import sqlite3 # biblioteca instalada no ato de instalação da linguagem python

# esta biblioteca posibilita a utilização de python com banco de dados 
# de forma dinâmica

conexao = sqlite3.connect('banco') # estabelece conexão do arquivo python com data base SQLite
cursor = conexao.cursor() # 

'''
Comandos que Interagem com objetos (tabelas) dentro do Banco de Dados.
'''

# cursor.execute('CREATE TABLE usuarios(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));') # -> começar a executar os comandos

# cursor.execute('ALTER TABLE usuarios RENAME TO usuario')
# cursor.execute('ALTER TABLE usuario ADD COLUMN telefoni INT')
# cursor.execute('ALTER TABLE usuario RENAME COLUMN telefoni TO telefone')

#cursor.execute('CREATE TABLE produtos(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')
# cursor.execute('DROP TABLE produtos')

conexao.commit() # linha que determina o comando de envio das informações (dados)
conexao.close # encerra o processo de comandos feitos entre a conexão e o commit

