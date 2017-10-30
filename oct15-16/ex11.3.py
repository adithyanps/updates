import sys
def print_hist(h):
 for x in sorted(h.keys()):
  print x, h[x]
a = raw_input("enter the string : ")
d = dict()
val = 0
for f in a:
 d[f] = val
 val = val + 1
print_hist(d)
if __name__ == "__print_hist__":
 print_hist(d)
