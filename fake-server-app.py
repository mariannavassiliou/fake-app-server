from flask import Flask
from flask import jsonify
import logging
app = Flask(__name__)
import pytest
from random import randint
import time
logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(message)s')
import json
import os

script_dir =  os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'test_variables.json')
with open(file_path) as json_file:
    params = json.load(json_file)

container_name = params["container_name"] 
image_name = params["image_name"]
urlBase = params["urlBase"]
peoplePath = params["peoplePath"]
planetsPath = params["planetsPath"]
starshipsPath = params["starshipsPath"]
valid_responses = params["valid_responses"]
port = params["port"]

@app.route(peoplePath+'<int:number>')
def people(number):
    time.sleep(randint(1,3))
    if number <= 100:
        return valid_responses[0]
    else:
        return "Invalid number", 404

@app.route(planetsPath+'<int:number>')
def planets(number):
    time.sleep(randint(1,3))
    if number <= 100:
        return valid_responses[1]
    else:
        return "Planet not found", 404

@app.route(starshipsPath+'<int:number>')
def starships(number):
    time.sleep(randint(1,3))
    if number <= 100:
        return valid_responses[2]
    else:
        return "Invalid planet identity", 404

app.run(host='0.0.0.0')
