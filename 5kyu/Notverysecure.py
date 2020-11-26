import re
def alphanumeric(password):
     return bool(re.match(r'^[A-Za-z0-9]+$', password))
