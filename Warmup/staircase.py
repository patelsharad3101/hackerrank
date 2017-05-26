#!/bin/python3

import sys

#staircase solution
n = int(input().strip())
s=" "
h="#"
for i in range(1,(n+1)):
    
        print(s*(n-i) + h*i)
       
