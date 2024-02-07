import math
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def show(self):
        print(f"x:{self.x};y:{self.y}")
    def move(self,newx,newwy):
        self.newx = newx
        self.newwy = newwy
        self.x = self.newx
        self.y = self.newwy
        print(f"Coordinates of x:{self.newx};y:{self.newwy}")
    def dist(self,nx,ny):
        self.nx = nx
        self.ny = ny
        dist = math.sqrt(((self.nx - self.x)**2)+((self.ny - self.y)**2))
        print(f"Distance between 2 points:{dist}")
print("Coordinates of x and y:")
z = Point(int(input()),int(input()))
z.show()
print("New coordinates of x and y:")
z.move(int(input()),int(input()))
print("New point coordinates:")
z.dist(int(input()),int(input()))