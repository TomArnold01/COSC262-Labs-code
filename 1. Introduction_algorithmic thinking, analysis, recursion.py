def almost_all(numbers): 
    total = sum(numbers)
    test = [total-x for x in numbers]
        
    return test

def concat_list(strings):
    """ recurvily adds the words to each other and retruns the whole word  
    """
    if len(strings) == 1:
        return strings[0]
    if len(strings) == 0:
        return ""
    else: 
        return strings[0] + concat_list(strings[1:])

def product(data):
    """retruns the product of the elements of a list"""
    if len(data) == 1:
        return data[0]
    if len(data) == 0:
        return 1
    else:
        return data[0] * product(data[1:])

def backwards(s):
    """returns a string backwards"""
    if s == "":
        return s 
    else:
        return backwards(s[1:]) + s[0]
    
def odds(data):
    """returns the odd elements of a list"""
    if len(data) == 0:
        return []
    if data[0] % 2 == 1:
        return [data[0]] + odds(data[1:])
    return odds(data[1:])
        
def squares(data):
    """returns a new list of the square of the number"""
    
    if len(data) == 0:
        return data
    else:
        sqr = data[0]**2
        return [sqr] + squares(data[1:])
