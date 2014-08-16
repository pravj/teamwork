import os
from flask import Flask, jsonify, request, render_template
tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

app = Flask("teamwork", template_folder=tmpl_dir)
from teamwork import routes