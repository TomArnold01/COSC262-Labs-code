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

# The example in the lecture notes
items = [Item(45, 3),
         Item(45, 3),
         Item(80, 4),
         Item(80, 5),
         Item(100, 8)]
maximum, selected_items = max_value(items, 10)
print(maximum)
# Check the returned item list with a hidden function
#check_item_list(items, selected_items, maximum)