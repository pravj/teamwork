import os
import json

from bigquery.client import get_client

CONFIG_PATH = os.path.join(
    os.path.dirname(__file__), '../../config/bigquery.json')
CONFIG_FILE = os.path.abspath(CONFIG_PATH)


class Query:

    def __init__(self):
        self.config = None

        self.project_id = None
        self.client_email = None
        self.private_key = None

        self.client = None

        self.load_config()
        self.create_client()

    def load_config(self):
        with open(CONFIG_FILE, 'r') as f:
            self.config = json.loads(f.read())
            print self.config
            f.close()

        self.project_id = self.config['project_id']
        self.client_email = self.config['client_email']
        self.private_key = self.config['private_key']

    def create_client(self):
        self.client = get_client(self.project_id,
                                 service_account=self.client_email,
                                 private_key=self.private_key, readonly=True)

    def execute(self, query):
        job_id, results = self.client.query(query)
        complete, rows = self.client.check_job(job_id)

        if complete:
            results = self.client.get_query_rows(job_id)
            return results
