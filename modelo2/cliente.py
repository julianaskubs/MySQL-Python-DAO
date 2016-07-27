#!/usr/bin/python
# -*- coding: UTF-8 -*-

from conexao import MySQL
from datetime import date


class Cliente:
    def __init__(self):
        self.nome = ''
        self.end = ''
        self.email = ''
        self.tel = ''
        self.dt_nasc = ''


class ClienteDao():
    def __init__(self):
        pass

    def insere(self, Cliente):
        try:
            dados = {'nome': Cliente.nome, 'end': Cliente.end, 'email': Cliente.email,
                     'tel': Cliente.tel, 'dt_nasc': Cliente.dt_nasc}

            sql = ("INSERT INTO clientes (nome, endereco, email, tel, dt_nasc) "
                   "values (%(nome)s, %(end)s, %(email)s, %(tel)s, %(dt_nasc)s)")
            self.conn(sql, dados)
            return dict(message='ok')
        except Exception as e:
            return dict(message=e.message)

    def lista(self):
        try:
            sql = "SELECT * FROM clientes"
            result = self.conn_r(sql)
            return result
        except Exception as e:
            return dict(message=e.message)

    def altera(self, Cliente, id):
        try:
            sql = "UPDATE clientes SET nome = %(nome)s, endereco = %(end)s," \
                  " email = %(email)s, tel = %(tel)s, dt_nasc = %(dt_nasc)s WHERE id = %(id)s"
            dados = {'nome': Cliente.nome, 'end': Cliente.end, 'email': Cliente.email,
                     'tel': Cliente.tel, 'dt_nasc': Cliente.dt_nasc, 'id': id}
            self.conn(sql, dados)
            return dict(message='ok')
        except Exception as e:
            return dict(message=e.message)

    def deleta(self, id):
        try:
            sql = "DELETE FROM clientes WHERE id = %s" % (id)
            self.conn(sql, dados=None)
            return dict(message='ok')
        except Exception as e:
            return dict(message=e.message)

    def recupera(self, id):
        try:
            sql = "SELECT nome, endereco, email, tel, dt_nasc FROM clientes where id = %s" % (id)
            result = self.conn_r(sql)
            nome, email, end, tel, dt_nasc = result[0]
            cli = Cliente()
            cli.nome = nome
            cli.email = email
            cli.end = end
            cli.dt_nasc = dt_nasc
            return cli
        except Exception as e:
            return dict(message=e.message)

    def conn(self, sql, dados):
        conn = MySQL().get_conexao2()
        cursor = conn.cursor()
        cursor.execute(sql, dados)
        conn.commit()
        cursor.close()
        conn.close()

    def conn_r(self, sql):
        conn = MySQL().get_conexao2()
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        return result
