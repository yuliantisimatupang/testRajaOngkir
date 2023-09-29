import json
import requests
from assertpy import assert_that
from setting.general import api_key, max_latency
from setting.endpoint import API_CITY

def test():
  head = {
    "key": api_key
  }
  req = requests.get(API_CITY + 'ssasf', headers=head)
  #
  #  VERIFIKASI
  status_code = req.status_code
  latency = req.elapsed.microseconds

  # ASSERT
  assert_that(status_code).is_equal_to(404)
  assert_that(latency).is_less_than(max_latency)

  # [scenario negatif 1] hasil yang akan ditampilkan adalah passed, karena kita url api city dengan negatif scenario dgn
  # menambahkan string 'assasf' dan kita buat expected result assert nya 404

  # [scenario negatif 2] hasil akan ditampilkan error ketika url api city sudah benar namun expected result kita adalah negatif 404