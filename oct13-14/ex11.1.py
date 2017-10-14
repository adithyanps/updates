import sys
def readwrd(x):
 b=dict()
 for f in open(x):
  m=f.strip()
  b[m]=m
 print b
readwrd('word.txt')
if __name__ == "__readwrd__":
 readwrd('word.txt')

