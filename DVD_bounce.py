import numpy as np
import math

class BounceBox:
    def __init__(self, xcor, ycor, h, w, direction, vector_mag=5):
        ''' Instantiator function. Inputs
                scalars: starting xcor, ycor, static height, static width, velocity as an angle in radians
        '''
        self.xcor = xcor
        self.ycor = ycor
        self._h = h / 2
        self._w = w / 2
        self.velocity = np.array([math.cos(direction), math.sin(direction)])
            # To do: replace with numpy array
    
    def is_collision(self, boundingBoxObject):
        H, W = boundingBoxObject.getedges()

        if (self.xcor - self._w <= 0 ) or (self.ycor - self._h < 0) or (self.xcor + self._w > H) or (self.ycor + self._h > W):
            return True
        return False

    def calculate_next_intersectionpoint(self, boundingBoxObject):
        boundingdim = boundingBoxObject.getedges()

        edges = [0, 0, boundingdim[0], boundingdim[1]]
        
        t = None

        for idx in range(0,4):
            # convention, evens are intersections with left/right, odds are up down
            if idx % 2 == 0:
                t = (edges[idx] - self.xcor) / self.velocity[0]
                if t < boundingdim[0] and t > 0:
                    break
            else:
                t = (edges[idx] - self.ycor) / self.velocity[1]
                if t < boundingdim[1] and t > 0:
                    break

        return (self.velocity[0]*t + self.xcor, self.velocity[1]*t + self.ycor)
    
    def __str__(self):
        return f'Bounce Box Stats: \n\tPosition: [{self.xcor} , {self.ycor}] \n\tVelocity: [{self.velocity}] \n\tDimensions: [{self._h} , {self._w}]'

class BoundingBox:
    def __init__(self, dimensions):
        ''' Instantiator function: Inputs
                list: DImensions in form [Height, Width]
        '''
        self._H = dimensions[0]
        self._W = dimensions[1]
    
    def __str__(self):
        return f'Bounding Box Dimensions are: {self._H} units by {self._W} units'
    
    def getedges(self):
        return [self._H, self._W]

def main():
    angle = 3
    Bouncer = BounceBox(6, 4, 1, 1, angle)
    Box = BoundingBox([10,10])

    print(Bouncer.calculate_next_intersectionpoint(Box))    


if __name__ == '__main__':
    main()