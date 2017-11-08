import sys
class Point(object):
 def __init__(self,x=1,y=2):
  self.x = x
  self.y = y
  print x,y
para = Point(9,6)
para.__init__()
