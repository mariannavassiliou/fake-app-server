import requests
import time
import os
import json
import pytest
import logging

script_dir =  os.path.dirname(__file__)
file_path = os.path.join(script_dir, '../../test_variables.json')
logs_path = os.path.join(script_dir, 'logs/')
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

class TestClass():
    def setup_class(self):
        print(f"container: {container_name}")
     #   print("setup_function ", os.system(f"docker run -d -p {port}:5000 -v {logs_path}:/app/ {image_name}"))
        print("setup_function ", os.system(f"docker run -d -p {port}:5000 {image_name}"))
        time.sleep(1) # Let the Docker container start

    def teardown_class(self):
        print("teardown_function container stop ", os.system(f"docker stop $(docker ps -a -q)"))
        print("teardown_function container remove ", os.system(f"docker rm $(docker ps -a -q)"))
        


    def test_get_people_success(self):
        response = requests.get(url=urlBase+port+peoplePath+"1")
        responseJson = json.loads(response.text)
        assert response.status_code == 200
        assert responseJson == valid_responses[0]

    def test_get_people_error(self) :
        response = requests.get(url=urlBase+port+peoplePath+"101")
        assert response.status_code == 404

    def test_get_people_error_characters(self) :
        response = requests.get(url=urlBase+port+peoplePath+"abc")
        assert response.status_code == 404

    def test_get_planets_success(self) :
        response = requests.get(url=urlBase+port+planetsPath+"1")
        responseJson = json.loads(response.text)
        assert response.status_code == 200
        assert responseJson == valid_responses[1]

    def test_get_planets_error(self) :
        response = requests.get(url=urlBase+port+planetsPath+"101")
        assert response.status_code == 404
    
    def test_get_starships_success(self) :
        response = requests.get(url=urlBase+port+starshipsPath+"50")
        responseJson = json.loads(response.text)
        assert response.status_code == 200
        assert responseJson == valid_responses[2]

    def test_get_starships_error(self) :
        response = requests.get(url=urlBase+port+starshipsPath+"101")
        assert response.status_code == 404