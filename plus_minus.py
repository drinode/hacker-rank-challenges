#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
length = len(arr)

pos = []
neg = []
zero = []

for x in arr:
    if x < 0:
    	neg.append(x)
    	
    elif x > 0:
    	pos.append(x)
    else:
    	zero.append(x)


print float(len(pos)) / length
print float(len(neg)) / length
print float(len(zero)) / length




