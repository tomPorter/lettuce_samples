from nose.tools import *
import factorial

def setup():
    pass

def teardown():
    pass

def test_fac_0():
    assert factorial.factorial(0) == 1

def test_fac_1():
    assert factorial.factorial(1) == 1

def test_fac_2():
    assert factorial.factorial(2) == 2

def test_fac_4():
    assert factorial.factorial(4) == 24
