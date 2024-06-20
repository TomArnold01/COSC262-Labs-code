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
    
def knapsack(items, matrix, index, n):
    if matrix[index][n] >= 0:
        return matrix[index][n]

    if index == 0:
        result = 0
    elif items[index].weight <= n:
        result = max(knapsack(items, matrix, index - 1,
                         n - items[index].weight) + items[index].value,
                knapsack(items, matrix, index - 1, n))
    else:
        result = knapsack(items, matrix, index - 1, n)
    matrix[index][n] = result
    return result



def max_value(items, capacity):
    
    items.insert(0, None)
    n = len(items) - 1
    matrix = [[-1] * (capacity + 1) for _ in range(n + 1)]
    return knapsack(items, matrix, n, capacity)


# The example from the lecture notes
items = [
    Item(45, 3),
    Item(45, 3),
    Item(80, 4),
    Item(80, 5),
    Item(100, 8)]

print(max_value(items, 10))