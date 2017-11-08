class Point(object):
 def __init__(self, x=None, y=None):
        self.x = x
        self.y = y
 def __add__(self, other):
        return self.x + other.x, self.y + other.y
p1 = Point(5, 3)
p2 = Point(-3, 4)
print p1 + p2
