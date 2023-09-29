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
    "key": api_key
  }
  # ini contoh url salah dengan string biasa
  # req = requests.get("https://api.rajaongkir.com/starter/provincessss", headers=head)

  # klo ini contoh url salah dengan menambahkan string
  req = requests.get(API_PROVINCE + 'sssss', headers=head)

  # VERIFIKASI
  status_code = req.status_code
  latency = req.elapsed.microseconds

  # ASSERT
  assert_that(status_code).is_equal_to(404)
  assert_that(latency).is_less_than(max_latency)
