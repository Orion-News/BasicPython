import sqlite3

class Endereco(object):
    def __init__(self):
        self.cep = None
        self.logradouro = None
        self.complemento = None
        self.bairro = None
        self.uf = None
        self.localidade = None
        self.ibge = None
        self.gia = None

    def create_table(self):
        connect = sqlite3.connect("endereco.db")
        cursor = connect.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS endereco(
             cep text, logradouro text, complemento text, bairro text, localidade text, uf text, ibge text, gia text   
            )
        ''')

        connect.commit()

    def salvar(self):
        self.create_table()

        connect = sqlite3.connect("endereco.db")
        cursor = connect.cursor()

        cursor.execute("INSERT INTO endereco VALUES('%s','%s','%s','%s','%s','%s','%s','%s')" % (self.cep, self.logradouro, self.complemento, self.bairro, self.localidade, self.uf, self.ibge, self.gia))

        connect.commit()
                       
        print('CEP: %s, Encontrado e Salvo com sucesso!.: ' % self.cep)
