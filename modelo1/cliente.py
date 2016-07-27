#!/usr/bin/python
# -*- coding: UTF-8 -*-

from conexao import MySQL
from datetime import date


class Cliente:
    def __init__(self, **kwargs):
        self.nome = kwargs['nome'] if 'nome' in kwargs else ''
        self.end = kwargs['end'] if 'end' in kwargs else ''
        self.email = kwargs['email'] if 'email' in kwargs else ''
        self.tel = kwargs['tel'] if 'tel' in kwargs else ''
        self.dt_nasc = kwargs['dt_nasc'] if 'dt_nasc' in kwargs else ''


class ClienteDao(Cliente):
    def __init__(self, **kwargs):
        Cliente.__init__(self, **kwargs)


    def insere(self):
        try:
            dados = {'nome': self.nome, 'end': self.end, 'email': self.email,
                     'tel': self.tel, 'dt_nasc': self.dt_nasc}
            sql = ("INSERT INTO clientes (nome, endereco, email, tel, dt_nasc) "
                   "values (%(nome)s, %(end)s, %(email)s, %(tel)s, %(dt_nasc)s)")
            conn = MySQL().get_conexao2()
            cursor = conn.cursor()
            cursor.execute(sql, dados)
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as e:
            return dict(message=e.message)

    def altera(self, id):
        try:
            sql = "UPDATE clientes SET nome = %(nome)s, endereco = %(end)s," \
                  " email = %(email)s, tel = %(tel)s, dt_nasc = %(dt_nasc)s WHERE id = %(id)s"
            dados = {'nome': self.nome, 'end': self.end, 'email': self.email,
                     'tel': self.tel, 'dt_nasc': self.dt_nasc, 'id': id}
            conn = MySQL().get_conexao2()
            cursor = conn.cursor()
            cursor.execute(sql, dados)
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as e:
            return dict(message=e.message)

    def deleta(self, id):
        try:
            sql = "DELETE FROM clientes WHERE id = %s" % (id)
            conn = MySQL().get_conexao2()
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as e:
            return dict(message=e.message)


    def lista(self):
        try:
            sql = "SELECT * FROM clientes"
            conn = MySQL().get_conexao2()
            cursor = conn.cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except Exception as e:
            return dict(message=e.message)

    def recupera(self, id):
        try:
            sql = "SELECT nome, endereco, email, tel, dt_nasc FROM clientes where id = %s" % (id)
            conn = MySQL().get_conexao2()
            cursor = conn.cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
            nome, email, end, tel, dt_nasc = result[0]
            return ClienteDao(nome=nome, email=email, end=end, tel=tel, dt_nasc=dt_nasc)
        except Exception as e:
            return dict(message=e.message)
