import sys
def sum_list(x):
 c = []
 b = 0
 for f in x:
  b = b + int(f)
 c.append(b)
 print b 
n = int(input("enter the limit : "))
a = [0 for i in range(n)]
for i in range(n):
 a[i] = raw_input("enter the nmbrs :") 
sum_list(a)
if __name__ == "__sum_list__":
 sum_list(a)

