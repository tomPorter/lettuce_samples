from nose.tools import *
import Factorial.factorial

def setup():
    pass

def teardown():
    pass

def test_fac_2():
    assert Factorial.factorial.factorial(2) == 2
