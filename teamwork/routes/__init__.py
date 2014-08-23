from teamwork import app
from flask import Flask, jsonify, request, render_template
from db.driver import Driver
from config import configer

config = configer.config('teamwork')
d = Driver(config)
d.connect()


@app.route('/')
def cal():
    return render_template("calender.html", org=config['organization'])


@app.route('/calender')
def calender():
    return d.table_data("contributions", 0, "organization")


@app.route('/user/top')
def top_users():
    # r.db('teamwork_github').table('contributions').orderBy(r.desc('total')).limit(21)
    return d.table_data("contributions", 6, 0, "total")
