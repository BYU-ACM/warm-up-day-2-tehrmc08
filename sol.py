def Binary_Search(arr, to_find):
    """A direct implementation of Newton's Method
     (For sanity assume that func and func_prime define there own division correctly,
     that is, don't cast anything to a float)
     params: arr (a list ordered from least to greatest)
             to_find (the item to find in arr)
     returns: index (int), x, s.t. arr[x] == to_find
              None(none-type) if for all x, arr[x] != to_find
    """
    cont = True
    low = 0
    high = len(arr)-1
    #c = 0
    while(cont):
        mid = (low + high)/2
        if(arr[mid] < to_find):
            #print mid
            low = mid
        elif(arr[mid] > to_find):
            #print mid
            high = mid
        else:
            return mid
        if(arr[mid] == to_find):
            return mid
        if(arr[low] == to_find):
            return low
        if(arr[high] == to_find):
            return high
        if(high==low or high == (low +1)):
            #print mid
            return None
        #c=c+1
    
    #pass

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
    if(func(left_side) < 0 and func(right_side) < 0):
        return None
    if(func(left_side) > 0 and func(right_side) > 0):
        return None
    cont = True
    low = left_side
    high = right_side
    while(cont):
        mid = (low + high)/2
        if(func(mid) < -tol):
            low = mid
        elif(func(mid) > tol):
            high = mid
        else:
            return mid
    pass
