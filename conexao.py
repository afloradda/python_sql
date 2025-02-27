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

# cursor.execute('CREATE TABLE produtos(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')
# cursor.execute('DROP TABLE produtos') -> excluindo o objeto (tabela) como um todo


'''
Comandos de interação com os dados em tabelas.
'''

# cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES(1, "Heloisa", "Itália", "lohelo@gmail.com", 123456)') # -> agregando dados a tabela 'usuario'
# cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES(2, "Ana", "Itália", "aanaa@gmail.com", 678910)')
# cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES(3, "Eisten", "Brasil", "albert_e@gmail.com", 400289)')
# cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES(4, "Isadora", "França", "izoca@gmail.com", 123458)')

# cursor.execute('DELETE FROM usuario WHERE id=4') # -> excluindo uma linha especifica da tabela

# cursor.execute('UPDATE usuario SET endereco="Itália" WHERE id=3')


'''
Comandos de consulta dentro do Banco de Dados
'''

dados = cursor.execute('SELECT * FROM usuario')
for usuario in dados:
    print(usuario)

conexao.commit() # linha que determina o comando de envio das informações (dados)
conexao.close # encerra o processo de comandos feitos entre a conexão e o commit

