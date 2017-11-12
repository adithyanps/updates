import sys
class Base1:
 def fun(self):
  print 'hallo base1'
class derived1(Base1):
 def fun2(self):
  print 'halo derived1'
a=derived1()
a.fun()
a.fun2()

