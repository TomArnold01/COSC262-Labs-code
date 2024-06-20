"""A program to read a grid of weights from a file and compute the 
   minimum cost of a path from the top row to the bottom row
   with the constraint that each step in the path must be directly
   or diagonally downwards. 
   This question has a large(ish) 200 x 200 grid and you are required
   to use a bottom-up DP approach to solve it.
"""
INFINITY = float('inf')  

def read_grid(filename):
    """Read from the given file an n x m grid of integer weights.
       The file must consist of n lines of m space-separated integers.
       n and m are inferred from the file contents.
       Returns the grid as an n element list of m element lists.
       THIS FUNCTION DOES NOT HAVE BUGS.
    """
    with open(filename) as infile:
        lines = infile.read().splitlines()

    grid = [[int(bit) for bit in line.split()] for line in lines]
    return grid

def filled_table(n_rows, n_cols):
    table = [n_cols * [0] for row in range(n_rows)]
    
    for i in range(n_rows):
        for j in range(n_cols):
            if i == 0:
                table[i][j] = 0
            elif j < i:
                table[i][j] = 1 + table[i-1][j]
            else:
                table[i][j] = 2 + table[i-1][j-i]
    return table

def grid_cost(grid):
    """The cheapest cost from row 1 to row n (1-origin) in the given grid of
       integer weights.
    """
    n_rows = len(grid)
    n_cols = len(grid[0])
    table = filled_table(n_rows, n_cols)
    
    for i in range(0, len(grid)):
        for j in range(len(grid[i])):

            if i == 0: # top row
                table[i][j] = grid[i][j]
            else:
                if j == 0:
                    table[i][j] = grid[i][j] + min(table[i-1][j], table[i-1][j+1])

                    
                elif j == len(grid[i])-1:

                    table[i][j] = grid[i][j] + min(table[i-1][j-1], table[i-1][j]) 
                    
                else:

                    table[i][j] = grid[i][j] + min(table[i-1][j-1], table[i-1][j], table[i-1][j+1]) 
                    
    best = min(table[len(table)-1])

    return best
    
    
def file_cost(filename):
    """The cheapest cost from row 1 to row n (1-origin) in the grid of integer
       weights read from the given file
    """
    return grid_cost(read_grid(filename))


def coins_reqd(value, coinage):
    """A version of the coin change problem that doesn't use a list
    comprehension"""
    num_coins = [0] * (value + 1)
    pred = [0] * (value + 1)
    coin_type = []
    coinage = sorted(coinage)
    
    for amt in range(1, value + 1):
        test = [0] * (value + 1)
        minimum = None
        for c in coinage:
            if c <= amt:
                coin_count = num_coins[amt - c]  # Num coins required to solve for amt - c
                if minimum is None or coin_count < minimum:
                    minimum = coin_count
                    pred[amt] = amt-c
                    
        num_coins[amt] = 1 + minimum
    count = value
    coin = 0
    goal = pred[-1]
    for items in pred[::-1]:
        if count == goal:
            coin_type.append(coin)
            coin = 1
            goal = pred[count]
            count -= 1
        else:
            coin += 1
            count -= 1    
    result = []    
    for items in coinage[::-1]:
        count = 0
        for j in coin_type:
            if j == items:
                count += 1
        if count != 0:
            result.append((items, count))

    return result