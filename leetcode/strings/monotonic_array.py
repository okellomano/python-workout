'''An array is monotonic if it is either monotone increasing or monotone decreasing. 
An array is monotone increasing if all its elements from left to right are non-decreasing. 
An array is monotone decreasing if all  its elements from left to right are non-increasing.
Given an integer array return true if the given array is monotonic, or false otherwise'''

def monotonic_array(array):
    if not array:
        return True
    else:
        n = len(array)
        left = array[0]
        right = array[n - 1]

    if left > right:
        # MD - The values should be decreasing
        for k in range(n - 1):
            if array[k] < array[k+1]:
                return False
    elif left == right:
        # All values must be equal
        for k in range(n - 1):
            if array[k] != array[k+1]:
                return False
    else:
        # right > left: MI
        for k in range(n - 1):
            if array[k] > array[k+1]:
                return False
    return True
