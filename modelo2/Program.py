from datetime import date, datetime
from cliente import ClienteDao, Cliente


class Run:
    def __init__(self):
        self.clienteDao = ClienteDao()

    def insere(self):
        cli = Cliente()
        cli.nome = "juliana teste"
        cli.end = "teste"
        cli.email = "teste@teste.com"
        cli.tel = '2222-3333'
        cli.dt_nasc = datetime.strptime('1999-08-01', '%Y-%m-%d').date()
        # cli.dt_nasc = date(1999, 08, 01)  # bug da classe date nao aceita meses 8 e 9

        # em cliente.py:
        novo = ClienteDao()
        result = novo.insere(cli)
        print result


    def lista(self):
        lista = self.clienteDao.lista()
        result = []
        for l in lista:
            # retorno do mysql eh uma tupla, no qual desempacotamos numa sequencia de variaveis:
            w, x, y, z, a, b = l
            b = date.strftime(b, '%Y-%m-%d')
            cli = {'id': str(w), 'nome': x, 'end': y, 'email': z, 'tel': a, 'dt_nasc': b}
            result.append(cli)
        # cada elemento na lista result representa um dict com os dados do cliente
        for r in result:
            # imprime o dict inteiro:
            print r
            # imprime somente valor correspondente a chave 'nome':
            print r['nome']

    def altera(self, id):
        # passo o id e recupero os dados do cliente no sql
        cliente = self.clienteDao.recupera(id)
        # altero o nome do cliente
        cliente.nome = "Teste altera again"
        # salvo a alteracao no sql
        update = ClienteDao()
        result = update.altera(cliente, id)
        print result

    def deleta(self, id):
        result = self.clienteDao.deleta(id)
        print result



Teste = Run()
# Teste.insere()
# Teste.lista()
# Teste.altera(4)
# Teste.insere()
Teste.deleta(6)

