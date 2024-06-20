class Item:
    """An item to (maybe) put in a knapsack"""
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        
    def __repr__(self):
        return f"Item({self.value}, {self.weight})"
        
        
    def getWeight(self):
        return self.weight
    
    def getValue(self):
        return self.value
    
    
def max_value(items, capacity):
    """uses a bottom-up DP implementation of the 0/1 knapsack problem to
    return the maximum value that can be packed into a knapsack of the given
    capacity using a given list of items"""
    n = len(items)
    table = [[0 for x in range(capacity+1)] for x in range(n+1)]
    for i in range(n+1):
        for w in range(capacity+1):
            if i==0 or w==0:
                table[i][w] = 0
            elif items[i-1].getWeight() <= w:
                table[i][w] = max(items[i-1].getValue() + table[i-1][w-items[i-1].getWeight()], table[i-1][w])
            else:
                table[i][w] = table[i-1][w]
      
    return table[n][capacity]
class Item:
    """An item to (maybe) put in a knapsack"""
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        
    def __repr__(self):
        return f"Item({self.value}, {self.weight})"
        
        
    def getWeight(self):
        return self.weight
    
    def getValue(self):
        return self.value
    
    
def max_value(items, capacity):
    """its return value is a pair (maximumValue, itemList) where maximumValue
    is the maximum achievable value returned, as before, and itemList is a
    list of items to achieve that optimum result."""
    n = len(items)
    table = [[0 for x in range(capacity+1)] for x in range(n+1)]
    for i in range(n+1):
        for w in range(capacity+1):
            if i==0 or w==0:
                table[i][w] = 0
            elif items[i-1].getWeight() <= w:
                table[i][w] = max(items[i-1].getValue() + table[i-1][w-items[i-1].getWeight()], table[i-1][w])
            else:
                table[i][w] = table[i-1][w]
      
    result = []
    j=len(table[1])-1
    i = len(table)-1
    while i > 0 and j > 0:

        if table[i][j] != table[i-1][j]:
            
            result.append(items[i-1])
            weight = items[i-1].getWeight()
            j = j - weight
        
        i = i-1

    return table[n][capacity], result

memo = {}

def lcs(s1, s2):
    if s1 == '' or s2 == '':
        return ''
    
    elif s1[-1] == s2[-1]: 
        return lcs(s1[:-1], s2[:-1]) + s1[-1]
   
    else:
        if (s1, s2) not in memo:
            soln1 = lcs(s1[:-1], s2)
            soln2 = lcs(s1, s2[:-1])
        else:
            return memo[s1, s2]
        
        if len(soln1) > len(soln2):
            memo[(s1,s2)] = soln1
            return soln1
        else:
            memo[s1,s2] = soln2
            return soln2
        
