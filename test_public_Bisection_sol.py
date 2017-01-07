import pytest
from sol import Bisection

def approx_equal(val1, val2):
  if not(isinstance(val1, (int, long, float, complex)) and isinstance(val2, (int, long, float, complex))):
    return val1==val2
  else:
    return abs(val1 - val2) < 1e-5

def test_linear_function():
  func = lambda x: 5*x - 3
  assert approx_equal(Bisection(func, 0, 2), 3/5.)

def test_quadratic_function():
  func = lambda x: 3*x**2-5*x-2
  assert approx_equal(Bisection(func, 1, 4), 2)
