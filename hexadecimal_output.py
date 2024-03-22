'''Converting hexadecimal numbers to decimal equivalent. '''


def hex_output():
    '''Takes a hex number and returns a decimal equivalent. '''
    decimal_number = 0
    hex_number = input('Enter a hex number to convert: ')
    
    for power, digit in enumerate(reversed(hex_number)):
        decimal_number += int(digit, 16) * (16 ** power)
    print(f'Decimal number: {decimal_number}')
    

def name_triangle():
    
    '''Asks the user for their name and then produces a name triangle. '''
    name = input('Enter your name: ')
    max_width = len(name) * 2 - 1
    
    for i in range(1, len(name) + 1):
        print(name[:i].center(max_width, ' '))
    

if __name__ == '__main__':
    # hex_output()
    name_triangle()