def elevator(left, right, call):
    value=" "
    if left==call or abs(call-left)<abs(call-right):
        value="left"
    if right==call or abs(right-call)<=abs(call-left):
        value="right"    
        
    return value    
