import sys
def lc(x):
 c = 0
 for line in open(x):
  c += 1
 return c
lc('ex14.5.py')
if __name__ == "__main__":
 print lc('ex14.5.py')
