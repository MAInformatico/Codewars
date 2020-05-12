def zero(f=None): #your code here
    return 0 if f is None else f(0)

def one(f=None): #your code here
    return 1 if f is None else f(1)
    
def two(f=None): #your code here
    return 2 if f is None else f(2)

def three(f=None): #your code here
    return 3 if f is None else f(3)

def four(f=None): #your code here
    return 4 if f is None else f(4)

def five(f=None): #your code here
    return 5 if f is None else f(5)

def six(f=None): #your code here
    return 6 if f is None else f(6)

def seven(f=None): #your code here
    return 7 if f is None else f(7)

def eight(f=None): #your code here
    return 8 if f is None else f(8)

def nine(f=None): #your code here
    return 9 if f is None else f(9)

def plus(x): #your code here
    return lambda y: y + x

def minus(x):
    return lambda y: y - x

def times(x):
    return lambda y: y * x

def divided_by(x):
    return lambda y: int(y / x)
