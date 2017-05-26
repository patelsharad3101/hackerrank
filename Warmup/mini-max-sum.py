#!/bin/python3

import sys

arr = list(map(int, input().strip().split(' ')))

x=sum(arr)
a=(x-max(arr))
b=(x-min(arr))
print(a,b)