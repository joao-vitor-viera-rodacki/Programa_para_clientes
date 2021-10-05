import sqlite3 as sg

banco = sg.connect('database.db')
cursor = banco.cursor()

#cursor.execute('CREATE TABLE clientes (nome text , idade integer, email text)')


def create_user(nome, idade, email):
    try:
        cursor.execute(f'INSERT INTO clientes VALUES("{nome}",{idade},"{email}")')
    
    except sg.Error as erro:
        print(f'Não foi possivel adicionar {erro}')

    else:
        print('User create com sucesso !!')
        banco.commit()
    


sql = 'SELECT * FROM clientes WHERE nome = ?'

def red (palavra):
   
    for row in cursor.execute(sql,(palavra,)):
        print(row)

red(12)
banco.close()