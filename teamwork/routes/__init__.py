from teamwork import app
from flask import Flask, jsonify, request, render_template
from teamwork.engine.procer import Procer

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/home')
def home():
	return render_template("sam.html");

@app.route('/calender', methods=['GET','POST'])
def calenderData():
	org = request.form['org']
	procer = Procer();
	procer.connect(org);
	# jsonify(procer.getCalenderData())
	return render_template("calender.html", org=org)