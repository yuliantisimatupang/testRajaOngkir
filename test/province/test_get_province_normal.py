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
  req = requests.get(API_PROVINCE, headers=head)
  # print(req.json())
  # dibawah ini script untuk merapikan text jadi json


  print(json.dumps(req.json(), indent=4))
  # VERIFIKASI
  status_code = req.status_code
  latency = req.elapsed.microseconds
  description = req.json().get('rajaongkir')['status']['description']
  results = req.json().get('rajaongkir')['results']

  # ASSERT
  assert_that(status_code).is_equal_to(400) # coba di bikin salah dulu
  # assert_that(status_code).is_equal_to(200)
  assert_that(latency).is_less_than(max_latency)
  assert_that(description).is_equal_to('OK')
  # is_type_of(list) digunakan jika bentuk nya adalah list
  # is not none digunkan untuk verifikasi result tidak boleh kosong
  assert_that(results).is_not_none()
  validate_json_schema(instance=req.json(), schema=schema_list_province_normal)
