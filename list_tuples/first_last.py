'''
Write a function, firstlast, that takes a  sequence  (string,  list,  or  tuple)  
and  returns  the  first  and  last  elements  of  that sequence,  in  a  two-element  
sequence  of  the  same  type.  
So firstlast('abc')  willreturn the string ac, while firstlast([1,2,3,4]) will return the list [1,4]

'''

def firstlast(sequence):
    if len(sequence) == 1:
        return sequence
    
    # We retrieve the elements using slicing to ensure that the returned value is of the same type as the original sequence.
    return sequence[:1] + sequence[-1:]


'''
Write a function that takes a list or tuple of numbers. 
Return a two-element list,containing (respectively) the sum of the even-indexed numbers and the sum ofthe odd-indexed numbers. 
So calling the function as even_odd_sums([10,20,30,40,50,60]), you’ll get back [90,120].

'''

def even_odd_sums(numbers):
    if len(numbers) == 1:
        return numbers
    
    if type(numbers) == list:
        return [sum(numbers[0::2]), sum(numbers[1::2])]
    elif type(numbers) == tuple:
        return sum(numbers[0::2]), sum(numbers[1::2])
    
    
'''
Write a function that takes a list or tuple of numbers. 
Return the result of alternately adding and subtracting numbers from each other. 
So calling the function  as plus_minus([10,20,30,40,50,60]),  you’ll  get  back  the  result  of 10+20-30+40-50+60, or 50

Pseudocode:
    ; Loop through the length of the sequence
'''

def plus_minus(numbers):
    pass


'''
Write a function that partly emulates the built-in zip function (http://mng.bz/Jyzv), taking any number of iterables and returning a list of tuples.
Each tuple will  contain  one  element  from  each  of  the  iterables  passed  to  the  function.
Thus, if I call myzip([10,20,30],'abc'), the result will be [(10,'a'),(20,'b'),(30,'c')].
You can return a list (not an iterator) and can assume that all of the iterables are of the same length

'''
        
def my_zip(iterables):
    pass



if __name__ == '__main__':
    print(firstlast([1, 2, 3, 4]))
    print(f'\nEven Odds Sum: {even_odd_sums([10,20,30,40,50,60])}')
    # print(f'Plus Minus: {plus_minus([10,20,30,40,50,60])}')
