import sys
import math
def my_sine(b):
 x=math.radians(b)
 t=x
 i=1
 s=x
 n=100
 while i < n:
  t=(-t * x * x) / ((2 * i) * (2 * i+ 1))
  s=s+t
  i=i+1
 return s
a=my_sine(1.2)
print a
