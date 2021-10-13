import math
class Circle:
    """Represents a circle.

    Attributes: center, radius
    """
def point_in_circle(point, circle):
    
    d = distance_between_points(point, circle.center)
    print(d)
    return d <= circle.radius
class point:
    """   """
def print_point(p):
    print('(%g,%g)'%(p.x,p.y))
def distance_between_points(p1,p2):
    dx=p1.x-p2.x
    dy=p1.y-p2.y
    dist=math.sqrt(dx**2+dy**2)
    return dist




def main():
    circle = Circle
    circle.center = Point()
    circle.center.x = 150.0
    circle.center.y = 100.0
    circle.radius = 75.0
    print(circle.center.x)
    print(circle.center.y)
    print(circle.radius)

    print("enter the point for test")
    
    p=point()
    p.x=int(input("Enter the x value"))
    p.y=int(input("Enter the y value"))
    print(point_in_circle(p,circle))
    
