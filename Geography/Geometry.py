#  File: Geometry.py

#  Description: Classes of different geometrical objects with their respective methods

#  Student Name: Samuel Kalisch

#  Student UT EID: sk54596

#  Course Name: CS 313E

#  Unique Number: 51130

#  Date Created: February 8 2022

#  Date Last Modified: February 15 2022

import math
import sys


class Point(object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0):
    self.x = x
    self.y = y
    self.z = z
    
  # create a string representation of a Point
  # returns a string of the form (x, y, z)
  def __str__ (self):
    return '(' + str(float(self.x))+ ', '+ str(float(self.y)) + ', '+ str(float(self.z)) + ')'
  
  # get distance to another Point object
  # other is a Point object
  # returns the distance as a floating point number
  def distance (self, other):
    return math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2 +(other.z - self.z)**2 )
  
  # test for equality between two points
  # other is a Point object
  # returns a Boolean
  def __eq__ (self, other):
    return (self.x, self.y, self.z) == (other.x, other.y, other.z)

class Sphere(object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1):
    self.x = x
    self.y = y
    self.z = z
    self.center = Point(x,y,z)
    self.radius = radius
  
  # returns string representation of a Sphere of the form:
  # Center: (x, y, z), Radius: value
  def __str__ (self):
    return 'Center: (' + str(float(self.x))+ ', '+ str(float(self.y)) + ', '\
      + str(float(self.z)) + ')'+ ', Radius: '+ str(float(self.radius))
  
  #gets distance from the center of the circle to other point/center
  #returns a floating pointy number
  def distance (self, other):
    return math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2 +(other.z - self.z)**2 )
  
  # compute surface area of Sphere
  # returns a floating point number
  def area (self):
    return 4*math.pi*self.radius**2
  
  # compute volume of a Sphere
  # returns a floating point number
  def volume (self):
   return 4/3*math.pi*self.radius**3
 
  # determines if a Point is strictly inside the Sphere
  # p is Point object
  # returns a Boolean
  def is_inside_point (self, p):
    if p.distance(self) < self.radius:
      return True
    return False
  
  # determine if another Sphere is strictly inside this Sphere
  # other is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, other):
    if other.distance(self) < self.radius - other.radius:
      return True 
    return False
    
  # determine if a Cube is strictly inside this Sphere
  # determine if the eight corners of the Cube are strictly
  # inside the Sphere
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, c):
    return Point(c.x + c.side/2,c.y+ c.side/2,c.z- c.side/2).distance(self) < self.radius and \
           Point(c.x + c.side/2,c.y+ c.side/2,c.z+ c.side/2).distance(self) < self.radius and \
           Point(c.x + c.side/2,c.y- c.side/2,c.z- c.side/2).distance(self) < self.radius and \
           Point(c.x + c.side/2,c.y- c.side/2,c.z+ c.side/2).distance(self) < self.radius and \
           Point(c.x - c.side/2,c.y+ c.side/2,c.z- c.side/2).distance(self) < self.radius and \
           Point(c.x - c.side/2,c.y+ c.side/2,c.z+ c.side/2).distance(self) < self.radius and \
           Point(c.x - c.side/2,c.y- c.side/2,c.z- c.side/2).distance(self) < self.radius and \
           Point(c.x - c.side/2,c.y- c.side/2,c.z+ c.side/2).distance(self) < self.radius  
   
  
  # determine if a Cylinder is strictly inside this Sphere
  # a_cyl is a Cylinder object
  # returns a Boolean
  def is_inside_cyl (self, cyl):
    #checks if distance is lower than redius, then calulates the radius at that z distance
    if abs(self.z - (cyl.z - cyl.height/2)) < self.radius and  abs(self.z - (cyl.z + cyl.height/2)) < self.radius:
      upper_radius = math.sqrt(self.radius**2 - abs(self.z - (cyl.z + cyl.height/2))**2) 
      lower_radius = math.sqrt(self.radius**2 - abs(self.z - (cyl.z - cyl.height/2))**2) 
      distance = math.sqrt((self.x-cyl.x)**2+(self.y-cyl.y)**2)
      if cyl.radius + distance < upper_radius and cyl.radius + distance < lower_radius:
        return True 
    return False
  
  # determine if another Sphere intersects this Sphere
  # other is a Sphere object
  # two spheres intersect if they are not strictly inside
  # or not strictly outside each other
  # returns a Boolean
  def does_intersect_sphere (self, other):
    if not self.is_inside_sphere(other) and not other.is_inside_sphere(self): 
      if other.distance(self) < self.radius + other.radius:
        return True 
    return False

  # determine if a Cube intersects this Sphere
  # the Cube and Sphere intersect if they are not
  # strictly inside or not strictly outside the other
  # a_cube is a Cube object
  # returns a Boolean
  
  def does_intersect_cube (self, c):
    if not c.is_inside_sphere(self) and not self.is_inside_cube(c):
      if abs(self.x-c.x) < c.side/2 + self.radius:
        if abs(self.y-c.y) < c.side/2 + self.radius:
          if abs(self.z-c.z) < c.side/2 + self.radius:
           return True
    return False
  # return the largest Cube object that is circumscribed
  # by this Sphere
  # all eight corners of the Cube are on the Sphere
  # returns a Cube object
  def circumscribe_cube (self):
    return Cube(self.x, self.y, self.z, 1/2*math.sqrt(2*self.radius**2))
  
class Cube (object):
  # Cube is defined by its center (which is a Point object)
  # and side. The faces of the Cube are parallel to x-y, y-z,
  # and x-z planes.
  def __init__ (self, x = 0, y = 0, z = 0, side = 1):
    self.x = x
    self.y = y
    self.z = z
    self.center = Point(x,y,z)
    self.side = side
  # string representation of a Cube of the form:
  # Center: (x, y, z), Side: value
  def __str__ (self):
    return 'Center: (' + str(float(self.x))+ ', '+ str(float(self.y)) + ', '+ \
      str(float(self.z)) + ')'+ ', Side: '+ str(float(self.side))
  
  # compute the total surface area of Cube (all 6 sides)
  # returns a floating point number
  def area (self):
    return 6*self.side**2
  # compute volume of a Cube
  # returns a floating point number
  def volume (self):
    return self.side**3
  # determines if a Point is strictly inside this Cube
  # p is a point object
  # returns a Boolean
  def is_inside_point (self, p):
    if self.x - self.side/2< p.x < self.x + self.side/2:
      if self.y - self.side/2 < p.y < self.y + self.side/2:
        if self.z - self.side/2 < p.z < self.z + self.side/2:
          return True 
    return False
      
  # determine if a Sphere is strictly inside this Cube
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
    if self.x - (self.side-a_sphere.radius)/2< a_sphere.x < self.x + (self.side-a_sphere.radius)/2:
      if self.y - (self.side-a_sphere.radius)/2 < a_sphere.y < self.y + (self.side-a_sphere.radius)/2:
        if self.z - (self.side-a_sphere.radius)/2 < a_sphere.z < self.z + (self.side-a_sphere.radius)/2:
          return True 
    return False
  
  # determine if another Cube is strictly inside this Cube
  # other is a Cube object
  # returns a Boolean
  def is_inside_cube (self, other):
    return Cube(self.x, self.y, self.z, self.side - other.side).is_inside_point(other)
  
  # determine if a Cylinder is strictly inside this Cube
  # a_cyl is a Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, cyl):
    if cyl.height/2 + abs(self.z-cyl.z) < self.side/2:
      if self.x - self.side/4< cyl.x < self.x + self.side/4:
       if self.y - self.side/4 < cyl.y < self.y + self.side/4:
         return True 
    return False

  # determine if another Cube intersects this Cube
  # two Cube objects intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, other):
    if not self.is_inside_cube(other) and not other.is_inside_cube(self):
      if abs(self.x-other.x) < self.side/2 + other.side/2: 
        if abs(self.y-other.y) < self.side/2 + other.side/2:
          if abs(self.z-other.z) < self.side/2 + other.side/2:  
            return True 
    return False

  # determine the volume of intersection if this Cube
  # intersects with another Cube
  # other is a Cube object 
  # returns a floating point number
  def intersection_volume (self, other):
    
    if not self.does_intersect_cube(other): return 0
      
    if self.x < other.x:
      x = (self.x + self.side/2) - (other.x-other.side/2)
    else:
       x = (other.x+other.side/2)- (self.x - self.side/2) 
    
    if self.y < other.y:
      y = (self.y + self.side/2) - (other.y-other.side/2)
    else:
       y = (other.y+other.side/2)- (self.y - self.side/2) 
      
    if self.z < other.z:
      z = (self.z + self.side/2) - (other.z-other.side/2)
    else:
      z = (other.z+other.side/2)- (self.z - self.side/2) 
        
    return float(x*y*z)

  # return the largest Sphere object that is inscribed
  # by this Cube
  # Sphere object is inside the Cube and the faces of the
  # Cube are tangential planes of the Sphere
  # returns a Sphere object
  def inscribe_sphere (self):
    return Sphere(self.x, self.y, self.z, self.side/2)
 
class Cylinder (object):
  # Cylinder is defined by its center (which is a Point object),
  # radius and height. The main axis of the Cylinder is along the
  # z-axis and height is measured along this axis
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):
    self.x = x
    self.y = y
    self.z = z
    self.center = Point(x,y,z)
    self.radius = radius
    self.height = height
  # returns a string representation of a Cylinder of the form:
  # Center: (x, y, z), Radius: value, Height: value
  def __str__ (self):
    return 'Center: (' + str(float(self.x))+ ', '+ str(float(self.y)) +', '+ str(float(self.z)) + ')'+ \
      ', Radius: '+ str(float(self.radius)) + ', Height: '+ str(float(self.height))
      
  #gets distance from the center of the circle to other point/center
  #returns a floating pointy number
  def distance (self, other):
    return math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2 +(other.z - self.z)**2 )
  
  # compute surface area of Cylinder
  # returns a floating point number
  def area (self):
    return 2*math.pi*self.radius*self.height  + 2*math.pi*self.radius**2 
  # compute volume of a Cylinder
  # returns a floating point number
  def volume (self):
    return self.height*math.pi*self.radius**2 
  
  # determine if a Point is strictly inside this Cylinder
  # p is a Point object
  # returns a Boolean
  def is_inside_point (self, p):
    if math.sqrt((p.x - self.x)**2 + (p.y - self.y)**2) < self.radius:
      if self.z-self.height/2 < p.z< self.z+self.height/2: 
        return True
    return False
  
  # determine if a Sphere is strictly inside this Cylinder
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, s):
    if (s.radius < self.radius- s.distance(self)) and (s.radius< self.height- s.distance(self)):
      return True
    return False
      
  # determine if a Cube is strictly inside this Cylinder
  # determine if all eight corners of the Cube are inside
  # the Cylinder
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, c):
    if c.side/2 + abs(self.z-c.z) < self.height/2:
      return math.sqrt((self.x- (c.x + c.side/2) )**2 + (self.y- (c.y+c.side/2))**2) < self.radius and \
        math.sqrt((self.x- (c.x + c.side/2) )**2 + (self.y- (c.y-c.side/2))**2)< self.radius and \
        math.sqrt((self.x- (c.x - c.side/2) )**2 + (self.y- (c.y+c.side/2))**2)< self.radius and \
        math.sqrt((self.x- (c.x - c.side/2) )**2 + (self.y- (c.y-c.side/2))**2)< self.radius
   
  # determine if another Cylinder is strictly inside this Cylinder
  # other is Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, cyl):
    if (cyl.radius < self.radius- cyl.distance(self)) and cyl.height/2 + abs(self.z-cyl.z) < self.height/2:
      return True
    return False

  # determine if another Cylinder intersects this Cylinder
  # two Cylinder object intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cylinder object
  # returns a Boolean
  def does_intersect_cylinder (self, other):
    if not self.is_inside_cylinder(other) and not other.is_inside_cylinder(self):
      if other.height/2 + self.height/2 > abs(self.z-other.z):
        if math.sqrt((self.x- other.x )**2 + (self.y- other.y)**2) < self.radius +other.radius:
          return True
    return False

def main():
  
  # read data from standard input
  data = [line.split(' ') for line in sys.stdin.read().strip().split('\n')]
    
  # read the coordinates of the first Point p
  # create a Point object
  p = Point(float(data[0][0]), float(data[0][1]), float(data[0][2]))
  
  # read the coordinates of the second Point q
  # create a Point object
  q = Point(float(data[1][0]), float(data[1][1]),float(data[1][2]))
  
  # read the coordinates of the center and radius of sphereA
  # create a Sphere object
  sphereA = Sphere(float(data[2][0]), float(data[2][1]), float(data[2][2]),float(data[2][3]))
  
  # read the coordinates of the center and radius of sphereB
  # create a Sphere object
  sphereB = Sphere(float(data[3][0]), float(data[3][1]), float(data[3][2]),float(data[3][3]))
  
  # read the coordinates of the center and side of cubeA
  # create a Cube object
  cubeA = Cube(float(data[4][0]), float(data[4][1]), float(data[4][2]),float(data[4][3]))
  
  # read the coordinates of the center and side of cubeB
  # create a Cube object
  cubeB = Cube(float(data[5][0]), float(data[5][1]), float(data[5][2]),float(data[5][3]))

  # read the coordinates of the center, radius and height of cylA
  # create a Cylinder object
  cylA = Cylinder(float(data[6][0]), float(data[6][1]), float(data[6][2]),float(data[6][3]),float(data[6][4]))
  
  # read the coordinates of the center, radius and height of cylB
  # create a Cylinder object
  cylB = Cylinder(float(data[7][0]), float(data[7][1]), float(data[7][2]),float(data[7][3]),float(data[7][4]))

  # print if the distance of p from the origin is greater
  # than the distance of q from the origin
  if p.distance(Point(0,0,0)) > q.distance(Point(0,0,0)):
    print('Distance of Point p from the origin is greater than the distance of Point q from the origin')
  else:
    print('Distance of Point p from the origin is not greater than the distance of Point q from the origin')
  
  # print if Point p is inside sphereA
  if sphereA.is_inside_point(p):
    print('Point p is inside sphereA')
  else:
    print('Point p is not inside sphereA')
  
  # print if sphereB is inside sphereA
  if sphereA.is_inside_sphere(sphereB):
    print('sphereB is inside sphereA')
  else:
    print('sphereB is not inside sphereA')
  
  # print if cubeA is inside sphereA
  if sphereA.is_inside_cube(cubeA):
    print('cubeA is inside sphereA')
  else:
    print('cubeA is not inside sphereA')
   
  # print if cylA is inside sphereA
  if sphereA.is_inside_cyl(cylA):
    print('cylA is inside sphereA')
  else:
    print('cylA is not inside sphereA')
  
  # print if sphereA intersects with sphereB
  if sphereA.does_intersect_sphere(sphereB):
    print('sphereA does intersect sphereB')
  else:
    print('sphereA does not intersect sphereB')
  
  # print if cubeB intersects with sphereB
  if sphereB.does_intersect_cube(cubeB):
    print('cubeB does intersect sphereB')
  else:
    print('cubeB does not intersect sphereB')
  
  # print if the volume of the largest Cube that is circumscribed
  # by sphereA is greater than the volume of cylA
  if sphereA.circumscribe_cube().volume() > cylA.volume():
    print('Volume of the largest Cube that is circumscribed by sphereA is greater than the volume of cylA')
  else:
    print('Volume of the largest Cube that is circumscribed by sphereA is not greater than the volume of cylA')
  
  # print if Point p is inside cubeA
  if cubeA.is_inside_point(p):
    print('Point p is inside cubeA')
  else:
    print('Point p is not inside cubeA')
  
  # print if sphereA is inside cubeA
  if cubeA.is_inside_sphere(sphereA):
    print('sphereA is inside cubeA')
  else:
    print('sphereA is not inside cubeA')
  # print if cubeB is inside cubeA
  if cubeA.is_inside_cube(cubeB):
    print('cubeB is inside cubeA')
  else:
    print('cubeB is not inside cubeA')

  # print if cylA is inside cubeA
  if cubeA.is_inside_cylinder(cylA):
    print('cylA is inside cubeA')
  else:
    print('cylA is not inside cubeA')
  # print if cubeA intersects with cubeB
  if cubeA.does_intersect_cube(cubeB):
    print('cubeA does intersect cubeB')
  else:
    print('cubeA does not intersect cubeB')
  
  # print if the intersection volume of cubeA and cubeB
  # is greater than the volume of sphereA
  if cubeA.intersection_volume(cubeB) > sphereA.volume():
    print('Intersection volume of cubeA and cubeB is greater than the volume of sphereA')
  else:
    print('Intersection volume of cubeA and cubeB is not greater than the volume of sphereA')
  
  # print if the surface area of the largest Sphere object inscribed
  # by cubeA is greater than the surface area of cylA
  if  cubeA.inscribe_sphere().area()> cylA.area():
    print('Surface area of the largest Sphere object inscribed by cubeA is greater than the surface area of cylA')
  else:
    print('Surface area of the largest Sphere object inscribed by cubeA is not greater than the surface area of cylA')

  # print if Point p is inside cylA
  if   cylA.is_inside_point(p):
    print('Point p is inside cylA')
  else:
    print('Point p is not inside cylA')
  
  # print if sphereA is inside cylA
  if  cylA.is_inside_sphere(sphereA):
    print('sphereA is inside cylA')
  else:
    print('sphereA is not inside cylA')
  
  # print if cubeA is inside cylA
  if cylA.is_inside_cube(cubeA):
    print('cubeA is inside cylA')
  else:
    print('cubeA is not inside cylA')
    
  # print if cylB is inside cylA
  if cylA.is_inside_cylinder(cylB):
    print('cylB is inside cylA')
  else:
    print('cylB is not inside cylA')
  # print if cylB intersects with cylA
  if cylB.does_intersect_cylinder(cylA):
    print('cylB does intersect cylA')
  else:
    print('cylB does not intersect cylA')
       
if __name__ == "__main__":
  main()