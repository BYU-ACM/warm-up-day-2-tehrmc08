import pytest
from sol import Binary_Search

def test_returns_correct_for_arange_list():
  assert Binary_Search(range(0,100), 99) == 99
  assert Binary_Search(range(0,100), 50) == 50
  assert Binary_Search(range(0,100), 34) == 34
  assert Binary_Search(range(0,100), 14) == 14
  assert Binary_Search(range(0,100), 49) == 49

def test_returns_correctly_for_sqaure_list():
  my_list = [x**2 for x in range(100)]
  assert Binary_Search(my_list, 64**2) == 64
  assert Binary_Search(my_list, 8**2) == 8
  assert Binary_Search(my_list, 34**2) == 34
  assert Binary_Search(my_list, 77**2) == 77

def test_returns_none_when_not_in_list():
  assert Binary_Search(range(0,100), 100) == None
