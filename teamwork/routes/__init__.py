import os, time
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

months = ["Jan", "Feb", "March", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
colors = ["#eee", "#d6e685", "#8cc665", "#44a340", "#1e6823"]
cur_mon = int(time.strftime("%m"))#Current month

@app.route('/')
def cal():
	_d = json.loads(d.table_data("repositories", 5, 0, "repo_commit", "repo_name" ,"repo_commit"))
	user = json.loads(d.table_data("contributions", 6, 0, "total", "total", "reference"))
	cal = json.loads(d.table_data("contributions", 0, "organization"))

	max_commit = cal[0]['contributions'][0][1]
	for i in range(0, len(cal[0]['contributions'])):
		if (max_commit < cal[0]['contributions'][i][1]):
			max_commit = cal[0]['contributions'][i][1]

	return render_template("teamwork.html", color=colors,
		repos=_d, users=user, info=info, months=months, cur_mon=cur_mon, res=cal, max=max_commit)

@app.route('/member/<member>')
def members(member):
	cal = json.loads(d.table_data("contributions", 0, member))

	max_commit = cal[0]['contributions'][0][1]
	for i in range(0, len(cal[0]['contributions'])):
		if (max_commit < cal[0]['contributions'][i][1]):
			max_commit = cal[0]['contributions'][i][1]
	
	return render_template("member.html", color=colors,
		info=info, months=months, cur_mon=cur_mon, res=cal, max=max_commit)

@app.route('/repos')
def member():
	repos = json.loads(d.table_data("repositories", 0, 0, "repo_commit", "repo_name" ,"repo_commit"))
	return render_template('repos.html', org=config['organization'], info=info, repos=repos)
