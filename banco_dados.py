import sqlite3

conn = sqlite3.connect("galeria.db")

cursor = conn.cursor()

def criar_tabela():
    sql = """
    CREATE TABLE albums(titulo text, artista text, data_lancamento text, data_publicacao text, midia text)
    """

    cursor.execute(sql)

    conn.commit()

def grava_album():
    sql = "INSERT INTO albums VALUES('Glow', 'Andy Hunter', '24/07/2012', 'Xplore Records', 'MP3')"

    cursor.execute(sql)

    conn.commit()


def grava_muitos():
    albums = [('Exodus', 'Andy Hunter', '9/7/2002', 'Sparrow Records', 'CD'),
              ('Until we Have faces', 'Red', '1/2/2011', 'Essential records', 'CD')]

    cursor.executemany("INSERT INTO albums VALUES(?,?,?,?,?)", albums)

    conn.commit()

def atualiza_album():
    sql = """
    UPDATE albums SET artista = 'Jonhn Doe'
    WHERE artista = 'Andy Hunter'
    """

    cursor.execute(sql)

    conn.commit()

def delete():
    sql = """
    DELETE FROM albums where artista = 'Jonhn Doe'
    """

    cursor.execute(sql)

    conn.commit()
    
def listar():
    sql = """
    SELECT rowid, * FROM albums ORDER BY artista
    """

    cursor.execute(sql)

    for row in cursor.fetchall():
        print(row)

    conn.commit()
