import os
import json
from bigquery.client import get_client


class Query:

    def __init__(self, config):
        self.project_id = config['project_id']
        self.client_email = config['client_email']
        self.private_key = config['private_key']

        self.client = None

        self.create_client()

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
