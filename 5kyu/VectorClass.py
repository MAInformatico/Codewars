import math
import functools 

class Vector:

    def __init__(self,values):
        self.values = values

    def __str__(self):
        r = '('
        for v in self.values:
            r += str(v) + ','
        return r[:-1] + ')'

    def add(self, other):
        return Vector([x+y for x,y in zip(self.values,other.values)])

    def subtract(self,other):
        return Vector([x-y for x,y in zip(self.values,other.values)])

    def dot(self,other):
        return functools.reduce(lambda x,y: x+y,[x*y for x,y in zip(self.values,other.values)])

    def norm(self):
        return math.sqrt(functools.reduce(lambda x,y: x+y,map(lambda x: x*x, self.values)))
    
    def equals(self,other):
        return self.values == other.values
