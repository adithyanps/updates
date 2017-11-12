import sys
class Complex:
 ""
def add(self,other):
 c = complex(self.real+other.real,self.imag+other.imag)
 print (c.real,c.imag)
def multiply(self,other):
 d= complex(self.real*other.real,self.imag*other.imag)
 print(d.real,d.imag)
a=complex(1,9)
b=complex(3,4)
add(a,b)
multiply(a,b)
