import sys
def histogram(x):
 d = dict()
 for c in x:
  d[c] = d.get(c,0) + 1
 print d
a = raw_input("enter the sting")
histogram(a)
if __name__ == "__histogram__":
 histogram(a)
