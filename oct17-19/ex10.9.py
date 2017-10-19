import sys
def rmv_dplct(x):
 s=x[:]
 b=[]
 s.sort()
 for f in range(len(s)-1):
  if s[f] == s[f+1]:
   b.append(s[f])
 print b
n=int(input("enter the limit : "))
a=[0 for i in range(n)]
for i in range(n):
 a[i]=raw_input("enter the words :")
rmv_dplct(a)
if __name__ == "__rmv_dplct__":
 rmv_dplct(a)
