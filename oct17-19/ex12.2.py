import sys
def sort(x):
 b = []
 m = []
 c = []
 for f in x:
  b.append((len(f),f)) 
  b.sort()
 m = b[::-1]
 for l,w in m:
   c.append(w)
 print c
n = int(input("limit : "))
a = [0 for i in range(n)]
for i in range(n):
 a[i] = raw_input("strngs : ")
sort(a)
if __name__ == '__sort__':
 sort(a)

