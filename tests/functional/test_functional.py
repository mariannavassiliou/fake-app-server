import requests
import json
urlBase = "http://127.0.0.1:5001"
peoplePath = "/people/"
planetsPath = "/planets/"
starshipsPath = "/starships/"

def test_get_people_success() :
    response = requests.get(url=urlBase+peoplePath+"1")
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    assert response.json()["name"] == "Luke Skywalker"

def test_get_people_error() :
    response = requests.get(url=urlBase+peoplePath+"101")
    assert response.status_code == 404

def test_get_planets_success() :
    response = requests.get(url=urlBase+planetsPath+"10")
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    assert response.json()["name"] == "Venus"

def test_get_planets_error() :
    response = requests.get(url=urlBase+planetsPath+"101")
    assert response.status_code == 404
    
def test_get_starships_success() :
    response = requests.get(url=urlBase+starshipsPath+"50")
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    assert response.json()["name"] == "Star Destroyer"

def test_get_starships_error() :
    response = requests.get(url=urlBase+starshipsPath+"101")
    assert response.status_code == 404