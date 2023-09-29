import json

import pytest


@pytest.fixture(scope='function', autouse=True)
def hook(request):
  # print('\nbefore suite f')
  get_error  = request.session.testsfailed
  yield
  # print('\nafter suite f')
  test_result =  request.session.testsfailed - get_error

  if test_result == 0:
    with open('test_report', 'r') as file:
      data = json.load(file)
    data['success'].append(1)
    with open('test_report', 'w') as file:
        json.dump(data, file, indent=4)
  else:
    with open('test_report', 'r') as file:
      data = json.load(file)
    data['success'].append(1)
    with open('test_report', 'w') as file:
        json.dump(data, file, indent=4)


@pytest.fixture(scope='session', autouse=True)
def suite(request):
  # print('\nbefore suite')
  json_temp = {
    "other" : [],
    "failed" : [],
    "success" : []
  }
  jsonString = json.dumps(json_temp)
  jsonFile = open ("test_report.json", "w")
  jsonFile.write(jsonString)
  jsonFile.close()
  yield
  # print('\nafter suite')