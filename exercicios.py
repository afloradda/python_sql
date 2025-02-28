import sqlite3

exercicios = sqlite3.connect('exercicios')
cursor = exercicios.cursor()

# 1. Criação da tabela alunos
cursor.execute('''
    CREATE TABLE alunos(
        id INTEGER PRIMARY KEY, 
        nome TEXT, 
        idade INTEGER, 
        curso TEXT
    )
''')

# 2. Inserção de 5 registros na tabela alunos
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(1, "Ana", 22, "Engenharia")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(2, "Carlos", 25, "Medicina")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(3, "Beatriz", 21, "Direito")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(4, "Eduardo", 23, "Engenharia")')
cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES(5, "Fernanda", 19, "Arquitetura")')

# 3. Consultas básicas
cursor.execute('SELECT * FROM alunos')

cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')

cursor.execute('SELECT * FROM alunos WHERE curso="Engenharia" ORDER BY nome')

cursor.execute('SELECT COUNT(*) FROM alunos')

# 4. Atualização e remoção
cursor.execute('UPDATE alunos SET idade=23 WHERE id=1')
cursor.execute('DELETE FROM alunos WHERE id=2')

# 5. Criar a tabela clientes e inserir dados
cursor.execute('''
    CREATE TABLE clientes(
        id INTEGER PRIMARY KEY, 
        nome TEXT, 
        idade INTEGER, 
        saldo FLOAT
    )
''')

cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(1, "João", 35, 1500.50)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(2, "Maria", 28, 200.75)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(3, "Pedro", 42, 3200.00)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES(4, "Ohana", 30, 1000.00)')

# 6. Consultas e funções agregadas
cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30')

cursor.execute('SELECT AVG(saldo) FROM clientes')

cursor.execute('SELECT nome, saldo FROM clientes ORDER BY saldo DESC LIMIT 1')

cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo > 1000')

# 7. Atualização e remoção com condições
cursor.execute('UPDATE clientes SET saldo=2000 WHERE id=4 AND nome="Ohana"')

cursor.execute('DELETE FROM clientes WHERE id=3')

# 8. Junção de tabelas
cursor.execute('''
    CREATE TABLE compras(
        id INTEGER PRIMARY KEY, 
        cliente_id INTEGER, 
        produto TEXT, 
        valor FLOAT,
        FOREIGN KEY (cliente_id) REFERENCES clientes(id)
    )
''')

cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(1, 1, "Notebook", 2500.00)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(2, 3, "Celular", 1200.00)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES(3, 4, "Tablet", 800.00)')

cursor.execute('''
    SELECT clientes.nome, compras.produto, compras.valor 
    FROM compras 
    INNER JOIN clientes ON compras.cliente_id = clientes.id
''')