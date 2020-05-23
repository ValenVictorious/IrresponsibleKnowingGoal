from flask import Flask, render_template, request
from random import choice
import sqlalchemy
import json

web_site = Flask(__name__)
  


@web_site.route('/')
def index():
  if request.method == 'GET':
	  return render_template('index.html')
  elif request.method == 'POST':
    name = request.POST['postnameData']
    print(name)


web_site.run(host='0.0.0.0', port=8080)