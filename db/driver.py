import os
import ast
import rethinkdb as r
import json


class Driver:

    def __init__(self, config):
        self.host = config['host']
        self.port = config['port']
        self.db = 'teamwork_%s' % (config['db'])

        self.con = None
        self.ref = None
        self.raw_ref = None

    def connect(self):
        self.con = r.connect(host=self.host, port=self.port).repl()

        self.create_db()

        self.ref = r.db(self.db)
        self.raw_ref = self.ref.table('raw')

    def disconnect(self):
        self.con.close()

    def create_db(self):
        db_list = r.db_list().run()

        if self.db in db_list:
            pass
        else:
            r.db_create(self.db).run()

    def table_exist(self, table):
        table_list = self.ref.table_list().run()

        if table in table_list:
            return True
        else:
            return False

    def create_table(self, table):
        if (self.table_exist(table)):
            pass
        else:
            r.db(self.db).table_create(table).run()

    def insert(self, table, data):
        if (self.table_exist(table)):
            pass
        else:
            self.create_table(table)

        self.ref.table(table).insert(data).run()

    def filter_rows(self, members):
        for member in members:
            self.raw_ref.filter({'user': member}).update({'is_member': 'true'}).run()

        self.raw_ref.filter({'is_member': 'false'}).delete().run()

    def table_data(self, table, limit, reference, orderBy=0, with1=0, with2=0):
        result = []
        con = self.ref.table(table)

        if (orderBy != 0):
            if(limit != 0):
                res = con.with_fields(with1, with2).order_by(r.desc(orderBy)).limit(limit).run()

        else:
            if (limit == 0):
                res = con.filter({'reference': reference}).run()
            else:
                res = con.filter({'reference': reference}).limit(limit).run()

        for data in res:
            result.append(data)

        return json.dumps(result)
