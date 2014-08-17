import os
import ast
import json

TEAMWORK_PATH = os.path.join(os.path.dirname(__file__), 'teamwork.json')
BIGQUERY_PATH = os.path.join(os.path.dirname(__file__), 'bigquery.json')


class Configer:

    def __init__(self):
        pass

    def config(self, _type):
        if (_type == 'teamwork'):
            config_file = os.path.abspath(TEAMWORK_PATH)
        elif (_type == 'bigquery'):
            config_file = os.path.abspath(BIGQUERY_PATH)

        return self.load_file(config_file, _type)

    def load_file(self, _file, _type):
        with open(_file, 'r') as f:
            config = f.read()
            f.close()

        if (_type == 'teamwork'):
            config = ast.literal_eval(config)
        elif (_type == 'bigquery'):
            config = json.loads(config)

        return config
