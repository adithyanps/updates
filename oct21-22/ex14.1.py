import os
def walk(x):
 for f in os.listdir(x):
  path =  os.path.join(x,f)
  if os.path.isfile(path):
   print path
  else:
   walk(path)
walk('/home/adhi/updates')
