#!/bin/python3

import sys
neg=0
pos=0
zer=0

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

for arr_temp in range(n):
    if arr[arr_temp]<0:
        neg=neg+1
    elif arr[arr_temp]>0:
        pos=pos+1
    else:
        zer=zer+1 
print((pos/n))
print((neg/n))

print((zer/n))

