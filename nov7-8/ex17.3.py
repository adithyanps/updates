import sys
class point(object):
 def __str__(self):
  return '%d,%d,%d' % (self.hour, self.minute, self.second)
pnt=point()
pnt.hour =4
pnt.minute =3
pnt.second=1
print pnt
