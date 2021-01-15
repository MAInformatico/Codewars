class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def length(node):
    result = 0
    while node:
        result += 1
        node = node.next
    return result
  
def count(node, data):
    result = 0
    while node:
        if node.data == data:
            result += 1
        node = node.next
    return result
