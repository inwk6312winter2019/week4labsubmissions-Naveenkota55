from math import *
class point:
        def __init__(self,x,y):
                self.x=x
                self.y=y

def dist_bwt_two_points():
        distance=sqrt(((x2.x-x1.x)**2)-((x2.y-x1.y)**2))
        print (distance)
x1=point(9,4)
x2=point(5,3)
dist_bwt_two_points()

