import sys
def most_freq(x):
 b = {}
 h = []
 for f in x:
  b[f] = b.get(f, 0) + 1
 for l, c in b.iteritems():
  h.append((l,c))
  h.sort(key=lambda x:x[1])
 c=h[::-1]
 print [(t[0]) for t in c]
a = raw_input("enter the string : ")
most_freq(a)
if __name__ == "__most_freq__":
 most_freq(a)
