#!/bin/python3

import sys


n = int(input().strip())
height = [int(height_temp) for height_temp in input().strip().split(' ')]

height2=max(height)
height3= height.count(height2)
print (height3)
