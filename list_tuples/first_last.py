'''
Write a function, firstlast, that takesa  sequence  (string,  list,  or  tuple)  
and  returns  the  first  and  last  elements  of  thatsequence,  in  a  two-element  
sequence  of  the  same  type.  
So firstlast('abc')  willreturn the string ac, while firstlast([1,2,3,4]) will return the list [1,4]

'''

def firstlast(sequence):
    if len(sequence) == 1:
        return sequence
    
    # We retrieve the elements using slicing to ensure that the returned value is of the same type as the original sequence.
    return sequence[:1] + sequence[-1:]


if __name__ == '__main__':
    print(firstlast([1]))
