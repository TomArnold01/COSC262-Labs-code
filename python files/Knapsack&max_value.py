class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def __repr__(self):
        return f"Item({self.value},{self.weight})"


def knapsack(items, matrix, index, wei):
    if matrix[index][wei] >= 0:
        return matrix[index][wei]

    if index == 0:
        result = 0
    elif items[index].weight <= wei:
        result = max(knapsack(items, matrix, index - 1,
        wei - items[index].weight) + items[index].value,knapsack(items, matrix, index - 1, wei))
    else:
        result = knapsack(items, matrix, index - 1, wei)
    matrix[index][wei] = result
    return result


def max_value(items, weight):
    items.insert(0, None)

    n = len(items) - 1


    matrix = [[-1] * (weight + 1) for _ in range(n + 1)]
    return knapsack(items, matrix, n, weight)


	
# A large problem (500 items)
import random
random.seed(12345)  # So everyone gets the same

items = [Item(random.randint(1, 100), random.randint(1, 100)) for i in range(500)]
print(max_value(items, 500))