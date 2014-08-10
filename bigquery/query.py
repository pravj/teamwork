import os
import json
from bigquery.client import get_client

config_file_path = os.path.join(os.path.dirname(__file__), '../config/bigquery.json')
config_file = os.path.abspath(config_file_path)

with open(config_file, 'r') as f:
    data = f.read()
    f.close()

config = json.loads(data)

# BigQuery project id as listed in the Google Developers Console.
project_id = config['project_id']

# Service account email address as listed in the Google Developers Console.
client_email = config['client_email']

# PKCS12 or PEM key provided by Google.
key = config['private_key']

client = get_client(project_id, service_account=client_email, private_key=key, readonly=True)

query = "SELECT payload_head, repository_name, repository_language, repository_size, repository_pushed_at FROM [githubarchive:github.timeline] WHERE type='PushEvent' AND repository_organization='github' AND actor_attributes_login='holman' AND PARSE_UTC_USEC(created_at) >= PARSE_UTC_USEC('2014-01-01 00:00:00');"

# Submit a query.
job_id, results = client.query(query)

# Check if the query has finished running.
complete, row_count = client.check_job(job_id)

# Retrieve the results.
if complete:
    results = client.get_query_rows(job_id)
    print results
