import sys
def anagram(x,y):
 m = list(x)
 n = list(y)
 m.sort()
 n.sort()
 if m == n:
  print 'true'
 else:
  print 'none'
a=raw_input("enter the 1st string : ")
b=raw_input("enter the 2nd string : ")
anagram(a,b)
if __name__ == "__anagram__":
 anagram(a)
