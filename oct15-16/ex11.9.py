import sys
def dplcts(t):
 d = dict()
 for f in t:
  if f in d:
    return 'true'
  else:
   d[f] = 'val'
 return 'false'
n = int(input("enter the limit : "))
a = [0 for i in range(n)]
for i in range(n):
 a[i] = raw_input("enter the parameters :")
print dplcts(a)
if __name__ == "__dplcts__":
 dplcts(a)
