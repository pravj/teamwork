import os
import ast
import rethinkdb as r
import jsontree, json
from config import configer

CONFIG_PATH = os.path.join(
	os.path.dirname(__file__), '../../config/teamwork.json')
CONFIG_FILE = os.path.abspath(CONFIG_PATH)

config = configer.config('teamwork')

class Procer:

	def __init__(self):
		self.host = None
		self.port = None
		self.db = None
		self.auth_key = None
		
		self.con = None
		self.load()

	def load(self):
		with open(CONFIG_FILE, 'r') as f:
			config = ast.literal_eval(f.read())
			f.close()

		self.host = config['host']
		self.port = config['port']
		self.db = 'teamwork_%s' % (config['db'])
		self.auth_key = config['auth_key']
		self.org = config['organization']

	def org(self):
		return self.org

	def connect(self):
		self.con = r.connect(host=self.host,
							 port=self.port,
							 db=self.db,
							 auth_key=self.auth_key).repl()
		print "Connected !! to %s" % self.db

	def get_calender_data(self):
		data = r.db(self.db).table("raw").pluck("repository_pushed_at","user").run()
		l = jsontree.jsontree()
		i=0
		for d in data:
			l[i] = d
			i+=1
		return l

	def get_gravatar(self):
		# data = r.db(self.db).table("repos").pluck("owner").limit(1).run()
		data = []
		l = jsontree.jsontree()
		for d in data:
			l["avatar_url"] = d["owner"]["avatar_url"]
			l["login"] = d["owner"]["login"]
		return json.dumps(l)
