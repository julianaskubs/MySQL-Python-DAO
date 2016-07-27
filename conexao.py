import mysql.connector as msc
import MySQLdb as mdb

# Host, name (database, opcional), user, pass, port

class MySQL:
    def __init__(self):
        pass

    def get_conexao(self):
        _host = 'localhost'
        _name = 'namedatabase'
        _user = 'root'
        _passwd = 'passwd'
        db = msc.connect(host=_host, database=_name, user=_user, passwd=_passwd)
        return db

    def get_conexao2(self):
        _host = 'localhost'
        _name = 'namedatabase'
        _user = 'root'
        _passwd = 'passwd'
        db = mdb.connect(_host, _user, _passwd, _name)
        return db
