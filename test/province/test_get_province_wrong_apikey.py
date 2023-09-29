import json
import requests
from assertpy import assert_that
import pytest

from setting.general import api_key, max_latency
from setting.endpoint import API_PROVINCE
from jsonschema import validate as validate_json_schema
from jsonschemas.schema_province import *


def test():
  head = {
    "key": api_key + 's'
  }
  req = requests.get(API_PROVINCE, headers=head)
  # print(req.json())
  # dibawah ini script untuk merapikan text jadi json


  print(json.dumps(req.json(), indent=4))
  # VERIFIKASI
  status_code = req.status_code
  latency = req.elapsed.microseconds
  description = req.json().get('rajaongkir')['status']['description']

  # ASSERT
  assert_that(status_code).is_equal_to(400)
  assert_that(latency).is_less_than(max_latency)
  assert_that(description).is_equal_to('Invalid key. API key tidak ditemukan di database RajaOngkir.')