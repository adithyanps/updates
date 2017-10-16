import sys
def rvrslukup(w,y):
 m = []
 for f in w:
  if w[f] == y:
   m.append(f)
 print m
a =  raw_input("enter the string : ")
b = int(input("enter the value : "))
d = dict()
c = 1
for x in a:
 d[x] = c
 c = c + 1
rvrslukup(d,b)
if __name__ == "__rvslukup__":
 rvrslukup(d,b)
