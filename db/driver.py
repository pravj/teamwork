import os
import json
import rethinkdb as r

CONFIG_PATH = os.path.join(os.path.dirname(__file__), '../config/teamwork.json')
CONFIG_FILE = os.path.abspath(CONFIG_PATH)


class Driver:

    def __init__(self):
        self.host = None
        self.port = None
        self.db = None
        self.auth_key = None

    def load(self):
        with open(CONFIG_FILE, 'r') as f:
            config = json.loads(f.read())
            f.close()

        self.host = config['host']
        self.port = config['port']
        self.db = config['db']
        self.auth_key = config['auth_key']

    def connect(self):
        return r.connect(host=self.host, port=self.port, db=self.db, auth_key=self.auth_key)
