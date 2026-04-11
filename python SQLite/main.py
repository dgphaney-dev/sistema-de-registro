import sqlite3
from tkinter import messagebox


class SistemaDeRegistro:
    def __init__(self):
        self.conn = sqlite3.connect('funcionario.db')
        self.c = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.c.execute(''' CREATE TABLE IF NOT EXISTS funcionarios (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nome TEXT NOT NULL,
                       email TEXT NOT NULL,
                       tel TEXT NOT NULL,
                       sexo TEXT NOT NULL,
                       data_nascimento TEXT NOT NULL,
                       endereco TEXT NOT NULL,
                       cargo TEXT NOT NULL,
                       picture TEXT NOT NULL) ''')

    def register_funcionario(self, funcionarios):
        self.c.execute("INSERT INTO funcionarios(nome, email, tel, sexo, data_nascimento, endereco, cargo, picture) VALUES(?,?,?,?,?,?,?,?)",
                       (funcionarios))
        self.conn.commit()

        # mostrando mensagem de sucesso
        messagebox.showinfo('Sucesso', 'Registro com sucesso!')

    def view_all_funcionarios(self):
        self.c.execute("SELECT * FROM funcionarios")
        dados = self.c.fetchall()

        return dados

    def search_funcionario(self, id):
        self.c.execute("SELECT * FROM funcionarios WHERE id=?", (id,))
        dados = self.c.fetchone()

        return dados

    def update_funcionario(self, novo_valores):
        query = "UPDATE funcionarios SET nome=?, email=?, tel=?, sexo=?, data_nascimento=?, endereco=?, cargo=?, picture=? WHERE id=?"
        self.c.execute(query, novo_valores)
        self.conn.commit()

        # mostrando mensagem de sucesso
        messagebox.showinfo(
            'Sucesso', f'Funcionario com ID:{novo_valores[8]} foi atualizado!')

    def delete_funcionario(self, id):
        self.c.execute("DELETE FROM funcionarios WHERE id=?", (id,))
        self.conn.commit()

        # mostrando mensagem de sucesso
        messagebox.showinfo('Sucesso', f'Estudante com ID:{id} foi Deletado!')


# Criando uma instancia do sistema de registro
sistema_de_registro = SistemaDeRegistro()

# informacoes
# funcionario =('dglindogostoso', 'dg@gmail.com', '61 9999-9999', 'M', '01/01/2001', 'Brasil,Brasilia', 'jovem aprendiz', 'imagem.png')
# sistema_de_registro.register_funcionario(funcionario)

# ver funcionarios
# todos_funcionarios = sistema_de_registro.view_all_funcionarios()

# procurar funcionario
# funcionario = sistema_de_registro.search_funcionario(3)

# atualizar funcionario
# funcionario =('keio', 'keio@gmail.com', '444', 'M', '01/01/2001', 'Brasil,Brasilia', 'jovem aprendiz', 'imagem.png', 2)
# funcionario = sistema_de_registro.update_funcionario(funcionario)

# sistema_de_registro.delete_funcionario(1)
