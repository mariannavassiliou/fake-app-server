This document describes the process to build the fake-server-app project and execute the functional and the performance tests.
During the test setup, the script automatically raises the container , runs the tests using the pytest module and saves the logs internally. After completion a container teardown is initiated where the container and all relevant processes are killed.

Before you run the tests, you need the following plugins/ modules/ frameworks installed on your machine:
- Docker client for windows (e.g. docker desktop)
- Python 3
- pip installation
- pytest module
- After you have installed pip, you can execute: pip install requests
- K6 framework
- Allure binary file 

Functional Test Suite Steps
1. Build docker image in project directory using the following command "docker build -t fake-server-app .".
2. Change directory to tests
3. Initiate functional tests with python command "python3 -m pytest functional --alluredir=/tmp/my_allure_results".
4. To see the allure results in your browser you can execute the following command "allure serve /tmp/my_allure_results".

Performance Test Suite Steps
1. Raise docker container with the following command: docker run -d -p 5001:5000 fake-server-app
2. Change directory to tests/performance
3. Execute the command: "k6 run load_test.js --out csv=test_results.csv"
4. Kill the container.
5. Results are stores in test.csv file.
6. Run puthon3 standard_deviation.py to take the mean and the standard deviation.

