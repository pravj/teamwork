import os
import ast

TEAMWORK_PATH = os.path.join(os.path.dirname(__file__), 'teamwork.json')
BIGQUERY_PATH = os.path.join(os.path.dirname(__file__), 'bigquery.json')


class Configer:

    def __init__(self):
        pass

    def config(self, form):
        if (form == 'teamwork'):
            config_file = os.path.abspath(TEAMWORK_PATH)
        elif (form == 'bigquery'):
            config_file = os.path.abspath(BIGQUERY_PATH)

        return self.load_file(config_file)

    def load_file(self, file):
        with open(file, 'r') as f:
            config = ast.literal_eval(f.read())
            f.close()

        return config
