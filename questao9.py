
import sqlite3


# Conectar ao banco e criar a tabela
def conectar(arquivo="estoque.db"):
    conn = sqlite3.connect(arquivo)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            categoria TEXT NOT NULL,
            preco REAL NOT NULL,
            quantidade INTEGER NOT NULL,
            minimo INTEGER NOT NULL
        )
    """)

    conn.commit()

    return conn


# Cadastrar produto
def cadastrar(conn, nome, categoria, preco, quantidade=0, minimo=5):
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO produtos (nome, categoria, preco, quantidade, minimo)
        VALUES (?, ?, ?, ?, ?)
    """, (nome, categoria, preco, quantidade, minimo))

    conn.commit()

    return cursor.lastrowid


# Listar todos os produtos
def listar(conn):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, nome, categoria, preco, quantidade, minimo
        FROM produtos
        ORDER BY nome
    """)

    return cursor.fetchall()


# Buscar produto pelo nome
def buscar(conn, texto):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, nome, categoria, preco, quantidade, minimo
        FROM produtos
        WHERE nome LIKE ?
        ORDER BY nome
    """, ("%" + texto + "%",))

    return cursor.fetchall()


# Registrar entrada de produtos
def entrada(conn, id, quantidade):
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE produtos
        SET quantidade = quantidade + ?
        WHERE id = ?
    """, (quantidade, id))

    conn.commit()

    return cursor.rowcount > 0


# Registrar saída de produtos
def saida(conn, id, quantidade):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT nome, quantidade
        FROM produtos
        WHERE id = ?
    """, (id,))

    produto = cursor.fetchone()

    if produto is None:
        return "Produto não encontrado."

    nome = produto[0]
    estoque_atual = produto[1]

    if quantidade > estoque_atual:
        return "Estoque insuficiente: há apenas " + str(estoque_atual) + " unidade(s)."

    cursor.execute("""
        UPDATE produtos
        SET quantidade = quantidade - ?
        WHERE id = ?
    """, (quantidade, id))

    conn.commit()

    return "Saída registrada: " + str(quantidade) + " unidade(s) de " + nome + "."


# Listar produtos com estoque baixo
def estoque_baixo(conn):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, nome, categoria, preco, quantidade, minimo
        FROM produtos
        WHERE quantidade < minimo
        ORDER BY nome
    """)

    return cursor.fetchall()


# Calcular o valor total do estoque
def valor_total(conn):
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(preco * quantidade)
        FROM produtos
    """)

    resultado = cursor.fetchone()[0]

    if resultado is None:
        return 0

    return resultado
