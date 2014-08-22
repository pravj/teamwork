from teamwork import app
from flask import Flask, jsonify, request, render_template
from teamwork.engine.procer import Procer
from db.driver import Driver
from config import configer

procer = Procer()
procer.connect()
org = procer.org
config = configer.config('teamwork')
d = Driver(config)
d.connect()


@app.route('/')
def cal():
	if(org is None or org == ''):
		return render_template("sam.html")
	return render_template("calender.html", org=org)

#creating new endpoints

@app.route('/calender')
def calender():
	return d.table_data("contributions", 0)
