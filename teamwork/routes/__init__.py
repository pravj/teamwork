from teamwork import app
from flask import Flask, jsonify, request, render_template
from db.driver import Driver
from config import configer
import json

config = configer.config('teamwork')
d = Driver(config)
d.connect()


@app.route('/')
def cal():
	_d = json.loads(d.table_data("repositories", 5, 0, "repo_commit", "repo_name" ,"repo_commit"))
	__d = json.loads(d.table_data("contributions", 6, 0, "total", "total", "reference"))
	return render_template("calender.html", org=config['organization'], repos=_d, users=__d)

@app.route('/calender')
def calender():
    return d.table_data("contributions", 0, "organization")
