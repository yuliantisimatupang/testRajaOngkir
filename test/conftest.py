import pytest


@pytest.fixture(scope='function', autouse=True)
def hook(request):
  print('\nbefore suite f')
  yield
  print('\nafter suite f')

@pytest.fixture(scope='session', autouse=True)
def suite(request):
  print('\nbefore suite')
  yield
  print('\nafter suite')