#!/bin/python3

import math
import os
import random
import re
import sys
from fractions import Fraction
#
# Complete the 'solve' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. STRING s
#

def solve(n, k, s):
    # Write your code here
    arr = [int(char) for char in s]
    # counts number of (i,i) pairs
    total = sum(arr)
    window = 0 
    
    if total == 0:
        return "0/1"
    
    for i in range(len(s)):
        # array has a one, so we can make a pair with previously seen ones
        if arr[i]:
            total += 2*window
            window +=1
        if i >= k and arr[i-k]:
            window -= 1
    
    f = Fraction(total, n**2)
    if f == 1:
        return "1/1"
    return str(f)

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        s = input()

        result = solve(n, k, s)

        fptr.write(result + '\n')

    fptr.close()
