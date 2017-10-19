import sys
def capitl_all(x):
 b = []
 c = []
 for f in x:
  b.append(f.upper())
 for x in b:
  for k in x:
   c.append(k)
 print c
n = int(input("enter the limit : "))
a = [0 for i in range(n)]
for i in range(n):
 a[i] = raw_input("enter the string : ")
capitl_all(a)
if __name__ == "__capitl_all__":
 capitl_all(a)
