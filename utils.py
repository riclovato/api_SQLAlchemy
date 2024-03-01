from models import Pessoas, Usuarios
def insere():
    pessoa = Pessoas(nome='Philipe', idade = 31)
    print(pessoa)
    pessoa.save()

def consulta():
    pessoa = Pessoas.query.all()
    for p in pessoa:
        print(p)

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Ricardo').first()
    pessoa.idade = 22
    pessoa.save()


def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Ricardo').first()
    pessoa.delete()


def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == '__main__':
    #insere()
    #altera_pessoa()
    #exclui_pessoa()
    #consulta()
    insere_usuario('icardo', '1234')
    consulta_usuarios()