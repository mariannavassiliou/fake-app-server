import requests
import time
import os
import json
urlBase = "http://127.0.0.1:5002"
peoplePath = "/people/"
planetsPath = "/planets/"
starshipsPath = "/starships/"
def setup_module():
    global image_name
    image_name = 'fake-server-app'
    print(f"image: {image_name}")
    print("setup_module ", os.system(f"docker build -t {image_name} ."))

def teardown_module():
    print("teardown_module ", os.system(f"docker rmi -f {image_name}"))


def setup_function():
    global port
    global container_name

    port = '5002'
    container_name = 'fake-server-app'
    print(f"container: {container_name}")
    print("setup_function ", os.system(f"docker run -d -p {port}:5000 {image_name}"))
    time.sleep(1) # Let the Docker container start

def teardown_function():
    print("teardown_function ", os.system(f"docker stop -t 0 {container_name}"))

def test_get_people_success() :
    response = requests.get(url=urlBase+peoplePath+"1")
    responseJson = json.loads(response.text)
    assert response.status_code == 200
    assert response.json()["name"] == "Luke Skywalker"

setup_module()
setup_function()
test_get_people_success()
teardown_module()
teardown_function()
