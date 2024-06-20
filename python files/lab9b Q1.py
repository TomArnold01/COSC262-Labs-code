import sys
sys.setrecursionlimit(2000)

class Item:
    """An item to (maybe) put in a knapsack. Weight must be an int."""
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def __repr__(self):
        """The representation of an item"""
        return f"Item({self.value}, {self.weight})"
   
memo = {}
def max_value(items, capacity, n=None):
    if n==None:
        n=len(items)
    
    if n == 0 or capacity == 0:
        return 0
    
    
    elif items[n-1].weight > capacity:
        
        if items not in memo:
            
            return max_value(items, capacity, n-1)
        
        else:
            
            return memo[items]
   
    else:
   
        memo[items] = max(max_value(items, capacity, n-1)
            ,items[n-1].value + max_value(items, capacity-items[n-1].weight, n-1))
       
       
        return max(max_value(items, capacity, n-1)
            ,items[n-1].value + max_value(items, capacity-items[n-1].weight, n-1))
    
    
# The example from the lecture notes
items = [
    Item(45, 3),
    Item(45, 3),
    Item(80, 4),
    Item(80, 5),
    Item(100, 8)]

print(max_value(items, 10))

	
## A large problem (500 items)
#import random
#random.seed(12345)  # So everyone gets the same

#items = [Item(random.randint(1, 100), random.randint(1, 100)) for i in range(500)]
#print(max_value(items, 500))