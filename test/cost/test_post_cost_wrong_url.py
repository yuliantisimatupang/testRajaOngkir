import json
import requests
from assertpy import assert_that
import pytest

from setting.general import api_key, max_latency
from setting.endpoint import API_COST
from jsonschema import validate as validate_json_schema
from jsonschemas.schema_cost import *


def test():
  head = {
    "key": api_key
  }
  payload = {
      "origin": "1",
      "destination": "60",
      "weight": 1000,
      "courier": "jne"
  }
  req = requests.post(API_COST + 's', headers=head, json=payload)

  # VERIFIKASI
  status_code = req.status_code
  latency = req.elapsed.microseconds

  # ASSERT
  assert_that(status_code).is_equal_to(404)
  assert_that(latency).is_less_than(max_latency)
