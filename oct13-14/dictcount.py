##count the elements of string that disply in dictionary##
import sys
def bc(s):
 d = dict()
 for c in s:
  if c not in d:
   d[c] = 1
  else:
   d[c] += 1
 print d
a = raw_input("enter the stng  : ")
print bc(a)
if __name__ == "__bc__":
 bc(a)


