def cycle_length(n):
    if n == 1: #base case
        return 1
    else:
        if n%2 == 0: #even
            return 1+ cycle_length(n//2)
        else: #odd
            return 1 +cycle_length(3*n+1)
        
"""--------------------------------------------------------------------------"""
def recursive_divide(x,y):
    if x < y:
        return 0
    else:
        return 1 +  recursive_divide(x-y,y)
"""--------------------------------------------------------------------------"""
def my_enumerate(items, index=0):
    if len(items) <= index:
        return items
    else:
        items[index] = (index, items[index] )
        return my_enumerate(items, index+1)
"""--------------------------------------------------------------------------"""
def num_rushes(slope_height, rush_height_gain, back_sliding):
    
    if slope_height <= rush_height_gain:
        return 1
    else:
        real_high_gain = rush_height_gain - back_sliding
        return 1 + num_rushes((slope_height-real_high_gain), rush_height_gain, back_sliding)
"""--------------------------------------------------------------------------"""
def num_rushes_mod(slope_height, rush_height_gain, back_sliding):
    
    if slope_height <= rush_height_gain:
        return 1
    else:
        real_high_gain = rush_height_gain - back_sliding
        total_high = slope_height-real_high_gain
        return 1 + num_rushes_mod(total_high, 0.95 * rush_height_gain, 0.95 * back_sliding)
"""--------------------------------------------------------------------------"""
import sys
sys.setrecursionlimit(100000)

def dumbo_func(data, index =0):
    """Takes a list of numbers and does weird stuff with it
    
    makes it way through the lsit, if the item can be // by 100  and not 
    divsible by 3 then it is count else it is inogred
    
    DO NOT RUN ON LAPTOP
    
    """
    
    if index >= len(data): 
        return 0
    else:
        if (data[index] // 100) % 3 != 0:
            return 1 + dumbo_func(data, index + 1)
        else:
            return dumbo_func(data, index + 1)
"""--------------------------------------------------------------------------"""
def all_pairs(list1, list2, index1=0, index2=0):
    
    tuples = []
    for list1_el in list1:
        
    return tuples
print(all_pairs([1, 2], [10, 20, 30]))