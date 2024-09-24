'''
    Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
    
    Example:
    12:01:00PM returns 12:01:00
    12:01:00AM returns 00:01:00
    
    Pseudocode:
    ; Split the time at : to make time list
    ; If the time is PM, and the first element is not 12, add 12 to the time
    ; Else if the first element is 12, set it to 00
'''

def time_conversion(s):
    time = s.split(':')
    print(f'Splited time: {time}')
    
    if s[-2:] == 'PM':
        if time[0] != '12':
            time[0] = str(int(time[0]) + 12)
    elif time[0] == '12':
        time[0] = '00'
    
    military_time = ':'.join(time)[:-2]
    
    return military_time


if __name__ == '__main__':
    s = '07:05:45PM'
    s1 = '12:01:00AM'
    print(time_conversion(s))
    