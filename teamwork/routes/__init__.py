import os
from teamwork import app
from flask import Flask, jsonify, request, render_template
from db.driver import Driver
from config import configer
import json

INFO_PATH = os.path.join(os.path.dirname(__file__), './../../raw/info.json')
info_file = os.path.abspath(INFO_PATH)

MEMBER_PATH = os.path.join(os.path.dirname(__file__), './../../raw/members.json')
member_file = os.path.abspath(MEMBER_PATH)

with open(info_file, 'r') as f:
	_info = f.read()
	f.close()

with open(member_file, 'r') as f:
	member = f.read()
	f.close()

info = json.loads(_info)
info["public_member"] = len(json.loads(member));

config = configer.config('teamwork')
d = Driver(config)
d.connect()


@app.route('/')
def cal():
	_d = json.loads(d.table_data("repositories", 5, 0, "repo_commit", "repo_name" ,"repo_commit"))
	__d = json.loads(d.table_data("contributions", 6, 0, "total", "total", "reference"))
	return render_template("teamwork.html", org=config['organization'], repos=_d, users=__d, info=info)

@app.route('/calender')
def calender():
    return d.table_data("contributions", 0, "organization")
