import sys
def anagram(x):
 d = {}
 l=[]
 for f in open(x):
  d[f[:-1]] = d.get(f, len(f)-1)
 
 print d
anagram('word.txt')
if __name__ == "__anagram__":
 anagram('word.txt')
