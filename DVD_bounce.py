import numpy as np

class BounceBox:
    def __init__(self, xcor, ycor, h, w, vectorVelocity):
        ''' Instantiator function. Inputs
                scalars: starting xcor, ycor, static height, static width
                list   : vector velocity in form [xvel, yvel]
        '''
        self.xcor = xcor
        self.ycor = ycor
        self._h = h / 2
        self._w = w / 2
        self.velocity = vectorVelocity
            # To do: replace with numpy array
    
    def is_collision(self, boundingBoxObject):
        H, W = boundingBoxObject.getedges()

        if (self.xcor - self._h < 0 ) or (self.ycor - self._w < 0) or (self.xcor + self._h > H) or (self.ycor + self._w > W):
            return True
        return False
    
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
    Bouncer = BounceBox(15 , 15, 1, 1, [1, 0])
    Box = BoundingBox([30,30])

    


if __name__ == '__main__':
    main()