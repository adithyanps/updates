import sys
def anagram(x):
 d = {}
 t=[]
 for line in open(x):
  r = line.strip().lower()
  t = list(r)
  t.sort()
  t = ''.join(t)
  if t not in d:
   d[t] = [r]
  else:
   d[t].append(r)
 t=[]
 for v in d.values():
  if len(v) > 1:
   t.append(v)
   t.sort()
  for x in t:
   print x
anagram('anagram.txt')
if __name__ == "__anagram__":
 anagram('anagram.txt')

