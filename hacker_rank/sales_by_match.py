'''
There is a pile of socks that must be paired by color. Given an array of integers representing the color of each sock,
determine how many pairs of socks with matching colors there are.

Example:
n = 7
ar = [1, 2, 1, 2, 1, 3, 2]

Output: 2

Explanation:
There is one pair of color 1 and one pair of color 2, there are three odd socks left one for each color. Thus number of matching pairs is 2.
'''

def sock_merchant(n, ar):
    # n = int(input().strip())
    # ar = list(map(int(), input.rstrip().split()))
    
    return sum([ar.count(n)//2 for n in set(ar)])


if __name__ == '__main__':
    n = 7
    ar = [1, 2, 1, 2, 1, 3, 2]
    
    print(sock_merchant(n, ar))