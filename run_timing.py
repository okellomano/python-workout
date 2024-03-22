from decimal import Decimal, InvalidOperation
'''Asks the user to input the time it takes to run a 10 Km run, and calculates the average time for different runs. '''

def run_timing():
    print('We are going to calculate the average amount of time it takes for a 10 Km run')
    
    number_of_runs = 0
    total_time = 0
    
    while True:
        time_taken = input('Enter the time taken to finish a 10 Km run. [Press Enter to quit]: ')
        
        if not time_taken:
            break
        
        total_time += float(time_taken)
        number_of_runs += 1
    average_time = total_time / number_of_runs
    
    return f'{average_time:.2f}'


'''Write a function that takes a float and two integers (before and after). The function should return a float consisting 
of before digits before the decimalpoint and after digits after. Thus, if we call the function with 1234.5678, 2 and3, 
the return value should be 34.567.

'''

def float_function(float_number, before, after):
    if not isinstance(float_number, float) or not isinstance(before, int) or not isinstance(after, int):
        return TypeError('Invalid arguments. Float_number must be of type float, and before and after must be integers')
    
    left_side, right_side = str(float_number).split('.')
        
    final_number = float(f'{left_side[-before:]}.{right_side[:after]}')
                
    return final_number


# Exploring the decimal class
def decimal_class():
    '''Asks the user to enter two strings, covserts them to decimal numbers and returns their sum. '''
    
    print('\nEnter two decial numbers. Press enter to exit.')
    while True:
        first_number = input('Enter the first decimal number: ')
        second_number = input('Enter the second decimal number: ')
        
        if not first_number or not second_number:
            break
                
        try:
            first_number = Decimal(first_number)
            second_number = Decimal(second_number)
            
            return first_number + second_number
        except ValueError:
            return 'Error: Invalid decimal number. Please provide a valid decimal number.'
        except InvalidOperation:
            return 'Cannot convert string to decimal. Please provide a valid decimal number.'
        
        


if __name__ == '__main__':
    # print(f'\n The average time: {run_timing()}')
    # print(f'Testing floating point: {float_function(1234.5678, 2.1, 3)}')
    print(f'The sum is: {decimal_class()}')
    