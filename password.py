import sqlite3

MASTER_PASSWORD = "123456"

senha = input('Insira sua senha master: ')
if senha != MASTER_PASSWORD:
    print('Senha Invalida! Encerrando...')
    exit()

conn = sqlite3.connect('passwords.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
  service TEXT NOT NULL,
  username TEXT NOT NULL,
  password  TEXT NOT NULL
);
''')


def menu():
    print("*******************************")
    print("* i : inserir nova senha")
    print("* l : listar serviços salvos")
    print("* r : recuperar senha")
    print("* s : sair")
    print("*******************************")


def get_password(service):
    pass


def insert_password(service, username, password):
    cursor.execute(f'''
        INSERT INTO users (service, username, password)
        VALUES ('{service}, '{username}', '{password}')
    ''')
    conn.commit()


def show_services():
    cursor.execute('''
        SELECT service FROM users;
    ''')
    for service in cursor.fetchall():
        print(service)


while True:
    menu()
    op = input("O que deseja fazer?")
    if op not in ['l', 'i', 'r', 's']:
        print('Opção Invalida')
        continue

    if op == 's':
        break

    if op == 'i':
        service = input('Qual o nome do serviço?')
        username = input('Qual o nome do usuário?')
        password = input('Qual a senha?')
        insert_password(service, username, password)

    
    if op == 'l':
        show_services()

conn.close()