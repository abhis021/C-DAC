
import math
import copy

class Point:
    """  Represent a point. """

class Rectangle:
    """" Represent a Rectangle.  """

class Circle:
    """Represents a circle.

    Attributes: center, radius
    """

def print_point(p):
    print(p.x,p.y)
def distance_between_points(p1,p2):
    s=math.sqrt((p1.x-p2.x)**2+(p1.y-p2.y)**2)
    print(s)
    return s
def point_in_circle(point, circle):
    
    d = distance_between_points(point, circle.center)
    print(d)
    return d <= circle.radius


def rect_in_circle(rect, circle):
    """Checks whether the corners of a rect fall in/on a circle.

    rect: Rectangle object
    circle: Circle object
    """
    p = copy.copy(rect.corner)
    print_point(p)
    if not point_in_circle(p, circle):
        return False
    print("hello1")
    p.x += rect.width
    print_point(p)
    if not point_in_circle(p, circle):
        return False

    p.y -= rect.height
    print_point(p)
    if not point_in_circle(p, circle):
        return False

    p.x -= rect.width
    print_point(p)
    if not point_in_circle(p, circle):
        return False

    return True


def rect_circle_overlap(rect, circle):
    """Checks whether any corners of a rect fall in/on a circle.

    rect: Rectangle object
    circle: Circle object
    """
    p = copy.copy(rect.corner)
    print_point(p)
    if point_in_circle(p, circle):
        return True

    p.x += rect.width
    print_point(p)
    if point_in_circle(p, circle):
        return True

    p.y -= rect.height
    print_point(p)
    if point_in_circle(p, circle):
        return True

    p.x -= rect.width
    print_point(p)
    if point_in_circle(p, circle):
        return True

    return False


def main():
    box = Rectangle()
    box.width = int(input("Enter width of a rectangle"))
    box.height = int(input("Enter height of a rectangle"))
    box.corner = Point()
    box.corner.x = int(input("Enter x coordiante of rectangle corner"))
    box.corner.y = int(input("Enter y coordinate of rectangle corner"))

    print(box.corner.x)
    print(box.corner.y)

    circle = Circle
    circle.center = Point()
    circle.center.x = int(input("Enter x coordiante of circle center"))
    circle.center.y = int(input("Enter x coordiante of circle center"))
    circle.radius = int(input("Enter the radius of circle"))

    print(circle.center.x)
    print(circle.center.y)
    print(circle.radius)

    print(point_in_circle(box.corner, circle))
    print(rect_in_circle(box, circle))
    print(rect_circle_overlap(box, circle))


if __name__ == '__main__':
    main()
