# ACM Warm Up Day Two
## What is a Warm up?
We will use warm ups in this class to review algorithm(s) that should already be familiar to us. Depending on the day Warm ups can take anywhere from 5 to 30 minutes and may include one to many different algorithms to implement.
Each day if anything important needs to be conveyed (specifically about the warm up) that information can be found in this file (README.md) and will likely be discussed in class as well.

## Rule's of the Warm up
**Warm up's are closed notes, closed friend, and closed internet (unless a link is provided for you)**

**You may not use awesome packages (like Numpy or Scipy) in Warmups. (Use math: eg. "import math as m")**

**Please at very least attempt the warm-ups. They will be the medium for feedback in this Class**

## Public Test Cases
Sometimes a "public\_test\_[Method\_Name].py" is provided for you. You can run all of these tests by running the following in the terminal: `pytest`

Note: You don't need to specify which file to test, py.test will find all the files that match the following regular expression: "^test.\*\.py$" (start with test and end with .py).

For more information on how py.test go to: http://doc.pytest.org/en/latest/

#Binary Search
In the file: "sol.py" You will find the following function:
```python
def Binary_Search(arr, to_find):
  """A direct implementation of Newton's Method
     (For sanity assume that func and func_prime define there own division correctly,
     that is, don't cast anything to a float)
     params: arr (a list ordered from least to greatest)
             to_find (the item to find in arr)
     returns: index (int), x, s.t. arr[x] == to_find
              None(none-type) if for all x, arr[x] != to_find
  """
  pass
```
Your job is to simply fill in "pass" with the appropriate iterative solution.

#Binary Root Finder
In the file: "sol.py" You will find the following function:
```python
def Bisection(func, left_side, right_side, tol=1e-5):
  """A direct implementation of Newton's Method
     (For sanity assume that func and func_prime define there own division correctly,
     that is, don't cast anything to a float)
     params: func (a function)
             left_side (a value for the function to take on, it should have opposite sign from `right_side`)
             right_side (a value for the function to take on, it should have opposite sign from `left_side`)
             tol (a value for which the function should return once a value at least that distance from zero is found)
     returns: root (float), x, s.t. abs(func(x))<tol
              None(none-type) if func(left_side), func(right_side) < 0 or func(left_side), func(right_side) > 0
  """
  pass
```
Your job is to simply fill in "pass" with the appropriate iterative solution.
