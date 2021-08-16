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
        self.point_history = np.array([xcor, ycor, direction])
    
    def is_collision(self, boundingBoxObject):
        H, W = boundingBoxObject.getedges()

        if (self.xcor - self._w <= 0 ) or (self.ycor - self._h < 0) or (self.xcor + self._w > H) or (self.ycor + self._h > W):
            return True
        return False

    def calculate_next_intersectionpoint(self, boundingBoxObject):
        boundingdim = boundingBoxObject.getedges()

        t = None
            # generic parameterization variable
        contact_edge = None
        edges = [0, 0, boundingdim[0], boundingdim[1]]
        for idx in range(0,4):
            # convention, evens are intersections with left/right, odds are up down
            # 0 = left, 1 = bottom, 2 = right, 3 = top
            if idx % 2 == 0:
                t = (edges[idx] - self.xcor) / self.velocity[0]
                if t < boundingdim[0] and t > 0:
                    contact_edge = idx
                    break
            else:
                t = (edges[idx] - self.ycor) / self.velocity[1]
                if t < boundingdim[1] and t > 0:
                    contact_edge = idx
                    break

        newcor = (self.velocity[0]*t + self.xcor, self.velocity[1]*t + self.ycor)

        newdirect = 2 * np.dot(self.velocity, boundingBoxObject.getNormal(contact_edge)) / np.linalg.norm(boundingBoxObject.getNormal(contact_edge)) - self.velocity
        newdirect = np.multiply(newdirect, boundingBoxObject.reflecscalars[contact_edge])
            # projection of incident vector across normal vector
        
        newangle = math.atan(newdirect[0] / newdirect[1])
            # conversion of velocity vector to angle 
            # Todo: this isn't converting correctly for some reason

        print(newcor, newangle)

        self.xcor = newcor[0]
        self.ycor = newcor[1]
        self.velocity = np.array([math.cos(newangle), math.sin(newangle)])

    
    def __str__(self):
        return f'Bounce Box Stats: \n\tPosition: [{self.xcor} , {self.ycor}] \n\tVelocity: [{self.velocity}] \n\tDimensions: [{self._h} , {self._w}]'

class BoundingBox:
    def __init__(self, dimensions):
        ''' Instantiator function: Inputs
                list: DImensions in form [Height, Width]
        '''
        self._H = dimensions[0]
        self._W = dimensions[1]
        self.normals = [np.array([1,   0]), np.array([0,   1]), np.array([-1,  0]), np.array([0,  -1])]
        self.reflecscalars = [np.array([-1 , 1]), np.array([1 , -1]), np.array([-1, 1]), np.array([1, -1])]
    
    def __str__(self):
        return f'Bounding Box Dimensions are: {self._H} units by {self._W} units'
    
    def getedges(self):
        return [self._H, self._W]
    
    def getNormal(self, edge):
        return self.normals[edge]

def main():
    angle = 0.785398
    Bouncer = BounceBox(0, 5, 1, 1, angle)
    Box = BoundingBox([10,10])

    for jdx in range(0,10):
        try:
            print(' ')
            Bouncer.calculate_next_intersectionpoint(Box)
        except:
            print(f'error on {jdx}')
            break

if __name__ == '__main__':
    main()