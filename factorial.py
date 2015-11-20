#!/usr/bin/env python

def factorial(x):
  if x == 0 or x == 1:
    return 1
  else:
    return factorial(x-1) * x

if __name__ == '__main__':
  print factorial(4)
