'''
Write a function, mysum() that takes any  number  of  arguments.
The  arguments  must  all  be  of  the same  type  and  know  how  to  respond  to  the +  operator.
(Thus,  the  function  shouldwork with numbers, strings, lists, and tuples, but not with sets and dicts.)


Thus, the result of mysum('abc','def') will be the string abcdef, and the result ofmysum([1,2,3],[4,5,6])  will  be  the  six-element  list [1,2,3,4,5,6].
Of  course,  it should also still return the integer 6 if we invoke mysum(1,2,3).
'''

def mysum(*items):
    if not items:
        return items
    
    result = items[0]
    
    for item in items[1:]:
        result += item
        
    return result


'''
Write a function, mysum_bigger_than, that works the same as mysum, except that it  takes  a  first  argument  that  precedes *args.
That  argument  indicates  the threshold  for  including  an  argument  in  the  sum.
Thus,  calling mysum_bigger_than(10,5,20,30,6) would return 50—because 5 and 6 aren’t greater than10.
This function should similarly work with any type and assumes that all of thearguments are of the same type.
Note that > and < work on many different types in Python, not just on numbers; with strings, lists, and tuples, it refers to their sort order.

'''
def mysum_bigger_than(*items):
    if not items:
        return items
    
    output = 0
    
    for item in items:
        if item > items[0]:
            output += item
    return output


'''
Write  a  function, sum_numeric,  that  takes  any  number  of  arguments.
If  the argument is or can be turned into an integer, then it should be added to the total.
Arguments  that  can’t  be  handled  as  integers  should  be  ignored.  Theresult  is  the  sum  of  the  numbers.
Thus, sum_numeric(10,20,'a','30','bcd') would return 60.
Notice that even if the string 30 is an element in thelist, it’s converted into an integer and added to the total.

'''

def sum_numeric(*items):
    return sum([int(item) for item in items if str(item).isdigit()])



'''
Write a function that takes a list of dicts and returns a single dict that combines all  of  the  keys  and  values.
If  a  key  appears  in  more  than  one  argument,  the value should be a list containing all of the values from the arguments.

'''

def combine_dictionaries(list_of_dicts):
    resulting_dict = {}
        
    for dict in list_of_dicts:
        for key, value in dict.items():
            if key in resulting_dict:
                if isinstance(resulting_dict[key], list):
                    resulting_dict[key].append(value)
                else:
                    resulting_dict[key] = [resulting_dict[key], value]
            else:
                resulting_dict[key] = value
            
    return resulting_dict
    

if __name__ == '__main__':
    print(mysum(1,2,3))
    print(mysum_bigger_than(10,5,20,30,6))
    print(f"The numeric sum: {sum_numeric(10,20,'a','20','bcd')}")
    
    dicts = [{'Car': 'Audi'}, {'Language': 'Python'}, {'Car': 'Bentley'}]
    print(combine_dictionaries(dicts))
    
    
