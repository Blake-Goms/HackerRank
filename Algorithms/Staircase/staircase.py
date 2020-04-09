# https://www.hackerrank.com/challenges/staircase/problem
def staircase(n):
    for i in range(1, n + 1):
        # its saying give me n- 1 spaces, then add # i many times
        print(' ' * (n - i) + '#' * i)
        
staircase(6)