from models import Pessoas
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

if __name__ == '__main__':
    #insere()
    #altera_pessoa()
    exclui_pessoa()
    consulta()