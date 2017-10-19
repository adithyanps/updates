import sys
def seq_sum(x):
 c = 0
 b = []
 for f in x:
  c = int(f) + c
  b.append(c)
  print c
n = int(input("enter the limit : "))
a = [0 for i in range(n)]
for i in range(n):
 a[i] = raw_input("enter the numbers : ")
seq_sum(a)
if __name__ == "__seq_sum__":
 seq_sum(a)
