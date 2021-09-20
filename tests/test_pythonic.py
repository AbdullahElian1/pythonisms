import pytest
from pythonic import __version__
from pythonic.pyhtonic import *

def test_version():
    assert __version__ == '0.1.0'


@pytest.fixture
def data():
  list = LinkedList()
  list.insert(2)
  list.insert(6)
  list.insert(1)
  return list
def test_len_of_list(data):
  assert len(data)==3

def test_dunder_str_method(data):
    assert str(data)=="[1] -> [6] -> [2] -> None"
