import os
import ast
import rethinkdb as r
import jsontree

CONFIG_PATH = os.path.join(
	os.path.dirname(__file__), '../../config/teamwork.json')
CONFIG_FILE = os.path.abspath(CONFIG_PATH)

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
		self.db = config['db']
		self.auth_key = config['auth_key']

	def connect(self):
		self.con = r.connect(host=self.host,
							 port=self.port,
							 db=self.db,
							 auth_key=self.auth_key).repl()
		print "Connected !! to %s" % self.db

	def getCalenderData(self, org):
		data = r.db(org).table("raw").pluck("repository_pushed_at","user").run()
		l = jsontree.jsontree()
		i=0
		for d in data:
			l[i] = d
			i+=1
		return l
