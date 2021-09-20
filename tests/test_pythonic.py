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
