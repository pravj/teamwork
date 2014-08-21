from teamwork import app
from flask import Flask, jsonify, request, render_template
from teamwork.engine.procer import Procer
# from teamwork.engine.api import Api

procer = Procer()
procer.connect()
org = procer.org
avatar_url = procer.get_gravatar()

@app.route('/')
def cal():
	if(org is None or org == ''):
		return render_template("sam.html")
	return render_template("calender.html", org=org)


@app.route('/api/org')
def org_detail():
	print avatar_url
	return avatar_url
	# return Api().detail_org(org)

"""
@app.route('/calender', methods=['GET','POST'])
def calenderData():
	org = request.form['org']
	if(org is None or org == ''):
		return render_template("sam.html")
	return render_template("calender.html", org=org)
"""

@app.route('/calender/details', methods=['POST'])
def return_details():
	org = request.form['org']
	if(org is None or org == ''):
		return render_template("sam.html")
	return jsonify(procer.get_calender_data())