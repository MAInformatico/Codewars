# Should return triangle type:
#  0 : if triangle cannot be made with given sides
#  1 : acute triangle
#  2 : right triangle
#  3 : obtuse triangle

def triangle_type(a, b, c):
    x, y, z = sorted([a, b, c])
    if z >= x + y:
        return 0
    if pow(z,2) == pow(x,2) + pow(y,2):
        return 2
    return 1 if pow(z,2) < pow(x,2) + pow(y,2) else 3
