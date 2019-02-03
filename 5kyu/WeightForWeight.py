def order_weight(strng):
    bar = sorted(strng.split(' '))
    baz = sorted(bar, key=foo)
    return " ".join(baz)
    
    
def foo(n):
  return sum([int(item) for item in n])
