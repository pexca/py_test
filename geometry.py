from geom2d import *

a = Point(0,0)#create class instance
b = Point(3,4)

print(a.distance(b))#call class method
print(a == b)
print(a == Point(0,0))