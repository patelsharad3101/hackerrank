#!/bin/python3

import sys

sum = 0
n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

for arr_temp in range(0,n):
    sum = sum + arr[arr_temp]
print(sum)