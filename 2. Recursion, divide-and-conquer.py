def cycle_length(n):
    """ If n is odd we return 3n+1 if even we n/2 """
    if n == 1:
        return 1
    
    if n % 2 == 0:
        return 1 + cycle_length(n/2)
        
    else:
        return 1 +cycle_length((3*n)+1)
    
def recursive_divide(x, y):
    """Performs inteer divison recusivly"""
    
    if x < y:
        return 0
    else:
        return 1 + recursive_divide(x-y,y)
    
    
def my_enumerate(items, index = 0):
    """ takes items from the list and returns them as a tuple with its
    index attacted"""
    
    if len(items) <= index:
        return items
    else:
        items[index] = (index, items[index])
        return my_enumerate(items, index+1)
    
def  num_rushes(slope_height, rush_height_gain, back_sliding):
    """ Calculates how many rushes it take herbert to climb up a slope 
    given that he will slide down a certain ammount each rush"""
    
    if rush_height_gain >= slope_height:
        return 1
    else:
        total_rush = rush_height_gain - back_sliding
        new_height = slope_height - total_rush
        return 1 + num_rushes(new_height, rush_height_gain, back_sliding)
    
def  num_rushes(slope_height, rush_height_gain, back_sliding):
    """ Calculates how many rushes it take herbert to climb up a slope 
    given that he will slide down a certain ammount each rush"""
    
    if rush_height_gain >= slope_height:
        return 1
    else:
        total_rush = rush_height_gain - back_sliding
        new_height = slope_height - total_rush
        return 1 + num_rushes(new_height, 0.95 * rush_height_gain, 0.95 *back_sliding)

    import sys
    sys.setrecursionlimit(100000)
    
    def dumbo_func(data, index =0):
        """Takes a list of numbers and does weird stuff with it
        
        makes it way through the lsit, if the item can be // by 100  and not 
        divsible by 3 then it is count else it is inogred """
        
        if index >= len(data): 
            return 0
        else:
            if (data[index] // 100) % 3 != 0:
                return 1 + dumbo_func(data, index + 1)
            else:
                return dumbo_func(data, index + 1)