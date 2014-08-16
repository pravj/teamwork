import os
import ast
import rethinkdb as r

CONFIG_PATH = os.path.join(
    os.path.dirname(__file__), '../config/teamwork.json')
CONFIG_FILE = os.path.abspath(CONFIG_PATH)


class Driver:

    def __init__(self):
        self.host = None
        self.port = None
        self.db = None
        self.auth_key = None

        self.con = None
        self.ref = None
        self.raw_ref = None

        self.load()

    def load(self):
        with open(CONFIG_FILE, 'r') as f:
            config = ast.literal_eval(f.read())
            f.close()

        self.host = config['host']
        self.port = config['port']
        self.db = config['db']
        self.auth_key = config['auth_key']

    def connect(self):
        self.con = r.connect(host=self.host,
                             port=self.port,
                             db=self.db,
                             auth_key=self.auth_key).repl()

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
        r.table_create(table).run()

    def insert(self, table, data):
        if (self.table_exist(table)):
            pass
        else:
            self.create_table(table)

        self.ref.table(table).insert(data).run()

    def filter_rows(self, members):
        self.raw_ref.merge({'is_member': 'false'}).run()

        for member in members:
            self.raw_ref.filter({'is_member': member}).update({'is_member': 'true'}).run()

        self.raw_ref.filter({'is_member': 'true'}).delete().run()
