from nose.tools import *
import Factorial.factorial as f

def setup():
    pass

def teardown():
    pass

def test_fac_2():
    assert f.factorial(2) == 2
