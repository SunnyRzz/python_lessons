from testing_linting.testing_lab import *
import pytest

def test_intergers():
    assert count(1234567890, 5) == 1

def test_string():
    assert count("Hello", "l") == 2
    assert count("Hello", "h") == 0
    assert count("Hello", "H") == 1

#From the QA github
    
def test_count_zeros():
	assert count([0,0,0],0)==3

def test_count_string():
	assert count(["a","a","a"],"a")==3

def test_count_minus():
	assert count([-1,-3,-5,-4], -1)==1

def test_count_normalNum():
	assert count([1,2,3,4,5,6,6,5,4,3,2,1], 1)==2
