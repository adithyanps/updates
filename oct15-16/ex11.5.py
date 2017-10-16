import sys
def invert_dict(w):
 invrse = dict()
 for key, val in w.items():
  invrse.setdefault(val, []).append(key) 
 print invrse
a = raw_input("enter the string")
d = dict()
val = 1
for x in a:
 d[x] = val
 val = val + 1
invert_dict(d)
if __name__ == "__invert_dict__":
 invert_dict(d)
