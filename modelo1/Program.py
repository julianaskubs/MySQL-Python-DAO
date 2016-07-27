from datetime import date
from cliente import ClienteDao, Cliente


class Run:
    def __init__(self):
        # a ideia eh que esse cara nunca tenha de fato um cliente preenchido,
        # que ele sirva apenas para chamada de funcoes
        self.clienteDao = ClienteDao()

    def lista_clientes(self):
        lista = self.clienteDao.lista()
        result = []
        for l in lista:
            w, x, y, z, a, b = l
            b = date.strftime(b, '%Y-%m-%d')
            cli = {'id': w, 'nome': x, 'end': y, 'email': z, 'tel': a, 'dt_nasc': b}
            result.append(cli)
        for r in result:
            print r

    def altera_cliente(self, id):
        # funcao
        clienteDao = self.clienteDao.recupera(id)
        # alterando um atributo
        clienteDao.nome = "Alterando Nome Again"
        # funcao
        clienteDao.altera(1)

    def insere_cliente(self):
        clienteDao = ClienteDao(nome='Teste ju nariga', email='teste3@teste.com', end='rua dos testes',
                                tel='5555-7777', dt_nasc=date(2001, 05, 20))
        clienteDao.insere()

    def deleta_cliente(self, id):
        self.clienteDao.deleta(id)


Teste = Run()
# Teste.lista_clientes()
# Teste.altera_cliente(1)
# Teste.insere_cliente()
# Teste.deleta_cliente(3)

