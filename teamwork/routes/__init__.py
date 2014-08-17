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
	if(org is None or org == ''):
		return render_template("sam.html")
	return render_template("calender.html", org=org)

@app.route('/calender/details', methods=['POST'])
def return_details():
	org = request.form['org']
	if(org is None or org == ''):
		return render_template("sam.html")
	procer = Procer()
	procer.connect()
	return jsonify(procer.getCalenderData(org))