from flask import Flask
from flask import jsonify
import logging
app = Flask(__name__)
import pytest
logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(message)s')

@app.route('/people/<int:number>')
def people(number):
    if number <= 100:
        return jsonify({
	    "name": "Luke Skywalker"
    })
    else:
        return "Invalid number", 404

@app.route('/planets/<int:number>')
def planets(number):
    if number <= 100:
        return jsonify({
	    "name": "Venus"
    })
    else:
        return "Planet not found", 404

@app.route('/starships/<int:number>')
def starships(number):
    if number <= 100:
        return jsonify({
	    "name": "Star Destroyer"
    })
    else:
        return "Invalid planet identity", 404

app.run(host='0.0.0.0')
