class circle:
    """   a circle consists of a center and its radius  """
class point:
    """     """
c=circle()
c.r=int(input("Eneter the radius of the circle"))
print(c.r)
c.center=point()
c.center.x=int(input("Enter the x point of the center"))
c.center.y=int(input("Enetr the y point of the center"))
print(c.center.x)
print(c.center.y)
p=point()
p.x=int(input("Enter x for a point"))
p.y=int(input("Enter y for a point"))
print(p.x)
if (p.x<=c.center.x+c.r) and (p.y<=c.center.y+c.r):
    print("Point lies inside the circle")
else :
    print("point lies outside the circle")
