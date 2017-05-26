#!/bin/python3

import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

sum1=0
sum2=0

for a_s in range(n):
    sum1= sum1+ a[a_s][a_s]
for a_p in range(n):
    for a_r in range(n):
        if a_p+a_r==n-1:
            sum2= sum2+a[a_p][a_r]
print(abs(sum1-sum2))
