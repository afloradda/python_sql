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
Comandos de consulta dentro do Banco de Dados.
'''

dados = cursor.execute('SELECT * FROM usuario')
for usuario in dados:
    print(usuario)


'''
Clausulas de ordenação e consulta dentro do SQL (ORDER BY e DESC).
'''

# dados = cursor.execute('SELECT * FROM usuario ORDER BY nome') # -> ordenando alfabeticamente
# dados = cursor.execute('SELECT * FROM usuario ORDER BY id DESC') # -> retorna os dados de forma decrescente (reverso)
# for usuario in dados:
#    print(usuario)


'''
Clausulas de ordenação e consulta dentro do SQL (LIMIT e DISTINCT).
'''

# dados = cursor.execute('SELECT * FROM usuario LIMIT 2') # -> limitando o limite de dados (linhas da tabela) a serem retornados
# dados = cursor.execute('SELECT DISTINCT * FROM usuario LIMIT 2') # -> utilizando o 'DISTINCT' você filtar o retorno de dados diferentes dentro da tabela
# for usuario in dados:
#    print(usuario)


'''
Clausulas de ordenação e consulta dentro do SQL (GROUP BY e HAVING).
'''

# dados = cursor.execute('SELECT nome FROM usuario GROUP BY nome') # -> agrupando informações por uma ou mais colunas
# dados = cursor.execute('SELECT nome FROM usuario GROUP BY nome HAVING id>1') # -> utilizando o 'HAVING' no lugar de 'WHERE' (após o processo de agregação)
# for usuario in dados:
#     print(usuario)


'''
Clausulas de agrupamento e consulta dentro do SQL em duas ou mais tabelas (JOIN'S: INNER, LEFT, RIGHT, FULL).
'''

# cursor.execute('CREATE TABLE gerentes(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100))')
# cursor.execute('DROP TABLE gerentes')

# cursor.execute('INSERT INTO gerentes (id, nome, endereco, email) VALUES (1, "Mariana Souza", "Rua A, 123 - São Paulo", "mariana@email.com")')
# cursor.execute('INSERT INTO gerentes (id, nome, endereco, email) VALUES (2, "Carlos Pereira", "Av. B, 456 - Rio de Janeiro", "carlos@email.com")')
# cursor.execute('INSERT INTO gerentes (id, nome, endereco, email) VALUES (3, "Fernanda Lima", "Rua C, 789 - Belo Horizonte", "fernanda@email.com")')
# cursor.execute('INSERT INTO gerentes (id, nome, endereco, email) VALUES (4, "Roberto Mendes", "Av. D, 101 - Curitiba", "roberto@email.com")')

# dados = cursor.execute('SELECT * FROM usuario INNER JOIN gerentes ON usuario.id = gerentes.id') # -> o INNER JOIN retorna as linhas correspondentes as condições determinadas
# dados = cursor.execute('SELECT * FROM usuario LEFT JOIN gerentes ON usuario.id = gerentes.id') # -> o LEFT JOIN retorna todas as informações da primeira tabela inserida na clausula
# dados = cursor.execute('SELECT * FROM usuario INNER JOIN gerentes ON usuario.id = gerentes.id') # -> o RIGHT JOIN preenche todas as informações a direita tal como o LEFT JOIN com a esquerda
# dados = cursor.execute('SELECT * FROM usuario INNER JOIN gerentes ON usuario.id = gerentes.id') # -> retorna todas as linhas de ambas as tabelas e passa a compara-las uma a uma
# for usuario in dados:
#     print(usuario)


conexao.commit() # linha que determina o comando de envio das informações (dados)
conexao.close # encerra o processo de comandos feitos entre a conexão e o commit

