def transpose(adj_list):
    """transposes the graph as a adj_list"""
    transpose_adj_list = [[] for i in range(0, len(adj_list))]
    for i in range(0, len(adj_list)):

        for j in range(0, len(adj_list[i])):

            transpose_adj_list[adj_list[i][j][0]].append((i, adj_list[i][j][1]))

    return transpose_adj_list
"""--------------------------------------------------------------------------"""
def dfs_tree(adj_list, start, parent=None, state=None):
    """Runs a DFS on a adj_list this will return parent"""
    if parent is None:
        parent = [None]*len(adj_list)
    if state is None:
        state = [False]*len(adj_list)
    state[start] = True

    for item in adj_list[start]:
        if state[item[0]] == False:    
            parent[item[0]] = start
            dfs_tree(adj_list, item[0], parent, state)
            print(state)
            print(parent)
            print()
    state[start] = True
    print(state)
    return parent
"""--------------------------------------------------------------------------"""
def bfs_tree(adj_list, start):
    """Runs a BFS on an adj_list this will return parent"""
    length = len(adj_list)
    parent = [None] * length
    visited = [False] * length
    visited[start] = True
    queue = []
    queue.append(start)
    
    while len(queue) != 0:
        node_pop = queue.pop(0)
        neighbours = adj_list[node_pop]
        for node_v, weight in neighbours:
            if visited[node_v] is False:
                visited[node_v] = True
                parent[node_v] = node_pop
                queue.append(node_v)
        print(queue)
        print(visited)
        print(parent)
        print()
    print(visited)
    return parent


"""--------------------------------------------------------------------------"""
def adjacency_matrix(graph_str):
    """Turns a string graph into a adjacncy matrix"""
    graph_list = graph_str.split()
    length = int(graph_list[1])
    result = [[]for i in range(length)]

    count = 0 
    last = []
    
    if len(graph_list) <= 2:
        for lists in result:
            for i in range(length):
                result[i].append(0)  
        return result

    if graph_list[2] != "W": # for non-weighted lists
        
        for lists in result:
            for i in range(length):
                result[i].append(0)        
        
        for char in graph_list[2:]:
            count += 1    
            if count == 2:
                if graph_list[0] == "D": # dirceted
                    result[int(last[0])][int(char)] = 1
                    last = [] 
                    count = 0
                else:
                    result[int(last[0])][int(char)] = 1
                    result[int(char)][int(last[0])] = 1
                    last = [] 
                    count = 0
            else:
                last.append(int(char))

    else:        
        for lists in result:
            for i in range(length):
                result[i].append(None)        
        
        for char in graph_list[3:]:
            count += 1
            if count == 3:
                if graph_list[0] == "D": # dirceted
                    result[last[0]][last[1]] = int(char)
                    last = []
                    count = 0
                else:
                    result[last[0]][last[1]] = int(char)
                    result[last[1]][last[0]] = int(char)
                    last = []
                    count = 0
                    
            else:
                last.append(int(char))
                    
    return result
"""--------------------------------------------------------------------------"""
def adjacency_list(graph_str):
    """Truns a str graph into a adjaceny_list"""
    graph_list = graph_str.split()
    length = int(graph_list[1])
    result = [[]for i in range(length)]
    count = 0
    last = []
    
    if graph_list[2] != "W": # for non-weighted lists
        for char in graph_list[2:]:
            count += 1

            if count == 2:
                char_index = (int(last[0]), None)
                last_index = (int(char), None)
                if graph_list[0] == "U":
                    result[int(last[0])].append(last_index)
                    result[int(char)].append(char_index)
                else:
                    result[int(last[0])].append(last_index)
                count = 0
                last = []
            else:
                last.append(char)
    else:
        for char in graph_list[3:]:
            count += 1
            if count == 3:
                if graph_list[0] == "U":
                    result[int(last[0])].append((int(last[1]), int(char)))
                    
                    result[int(last[1])].append((int(last[0]), int(char)))
                else:
                    result[int(last[0])].append((int(last[1]), int(char)))
                count = 0
                last = []
            else:
                last.append(char)
    return result

	
#from pprint import pprint

#graph_string = """\
#U 7
#1 5
#5 0
#0 4
#4 3
#3 1
#3 5
#"""

#pprint(adjacency_list(graph_string))
"""--------------------------------------------------------------------------"""
def dijkstra(adj_list, start):
    """Implements dijkstras algorithm this will return parent and distance"""

    len_adj = len(adj_list)
    in_tree = [False] * len_adj
    distance = [float('inf')] * len_adj
    parent = [None] * len_adj
    distance[start] = 0
    
    no_possible_vertex = []
    
    while not all(in_tree):
        next_vert = next_vertex(in_tree, distance)
        if next_vert == float('inf'):
            break
        in_tree[next_vert] = True
        for vertex, weight in adj_list[next_vert]:
            test = distance[next_vert] + weight
            if not in_tree[vertex] and test < distance[vertex]:
                distance[vertex] = test
                parent[vertex] = next_vert
        print(in_tree)
        print(distance)
        print(parent)
        print()
    print(distance)
    result = (parent, distance)
    return result


"""--------------------------------------------------------------------------"""
def prim(adj_list, start):
    """Implements Prim algorithm this will return parent and distance"""

    n = len(adj_list)
    in_tree = [False] * n
    distance = [float('inf')] * n
    parent = [None] * n
    distance[start] = 0
    
    no_possible_vertex = []
    
    while not all(in_tree):
        next_vert = next_vertex(in_tree, distance)

        if next_vert == float('inf'):
            break
        in_tree[next_vert] = True
        for vertex, weight in adj_list[next_vert]:
            if not in_tree[vertex] and weight < distance[vertex]:
                distance[vertex] = weight
                parent[vertex] = next_vert
        print(in_tree)
        print(distance)
        print(parent)
        print()
    print(distance)
    return parent         
"""--------------------------------------------------------------------------"""
def next_vertex(in_tree, distance):
    """Helper function for both algoithms Prims and dijkstras"""
    possible_next = []
    next_vert = None 
    for index, vertex in enumerate(in_tree): 
        if not vertex:
            possible_next.append(index) 
    min_weight = distance[possible_next[0]] 
    next_vert = possible_next[0]

    for i in possible_next:
        weight = distance[i] 
        if weight < min_weight: 
            min_weight = weight
            next_vert = i
    print(next_vert)
    return next_vert
"""--------------------------------------------------------------------------"""

graph_str = """\
U 7 W
0 1 5
0 2 7
0 3 12
1 2 9
2 3 4
1 4 7
2 4 4
2 5 3
3 5 7
4 5 2
4 6 5
5 6 2

"""

adj = adjacency_list(graph_str)
print(dijkstra(adj, 0))

"""--------------------------------------------------------------------------"""

"""
    Reads a file of a grid from a coin chnaging problem and slove it

"""
INFINITY = float('inf')  # Same as math.inf

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

memo = {}
def grid_cost(grid):
    """The cheapest cost from row 1 to row n (1-origin) in the given
       grid of integer weights.
    """
    n_rows = len(grid)      
    n_cols = len(grid[0])   

    def cell_cost(row, col):
        """The cost of getting to a given cell in the current grid."""
        if row < 0 or row >= n_rows or col < 0 or col >= n_cols:
            return INFINITY  # Off-grid cells are treated as infinities
        else:
            if (row,col) in memo:
                coin = memo[(row,col)]
                return coin
            cost = grid[row][col]
            if row != 0:
                cost += min(cell_cost(row-1, col + delta_col) for delta_col in range(-1, +2))
                memo[(row,col)] = cost
            return cost
            
    best = min(cell_cost(n_rows - 1, col) for col in range(n_cols))
    return best

def file_cost(filename):
    """The cheapest cost from row 1 to row n (1-origin) in the grid of integer
       weights read from the given file
    """
    return grid_cost(read_grid(filename))



"""--------------------------------------------------------------------------"""


