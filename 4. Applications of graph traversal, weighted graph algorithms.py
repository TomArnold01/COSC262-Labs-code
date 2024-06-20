def transpose(adj_list):
    """takes a adj list and returns a trasposr of the graph"""
    transpose_adj_list = [[] for i in range(0, len(adj_list))]
    for i in range(0, len(adj_list)):

        for j in range(0, len(adj_list[i])):

            transpose_adj_list[adj_list[i][j][0]].append((i, adj_list[i][j][1]))
            
    return transpose_adj_list

def is_strongly_connected(adj_list):
    """ Returns True if the graph is strongly connected otherwise false"""
    result = [[]for i in range(len(adj_list))]
    visited = bfs_tree(adj_list, 0)

    for items in visited:  #base case it any nodes are not connected at all
        if items == False:
            return False

    for i in range(len(adj_list)):
        for items in adj_list[i]:
            result[items[0]].append((i, items[1]))
    
    visited = bfs_tree(result, 0)
    for items in visited: 
        if items == False:
            return False
    else:
        return True

def bfs_tree(adj_list, start):
    """ for the stringly connected function"""
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
    return visited

def next_vertex(in_tree, distance):
    """returns the next vertex for prim and dikstra"""
    count = 0
    completed = False
    sorted_list = sorted(distance)
    while completed == False:
        for i in range(len(distance)):
            smallest = sorted_list[count]
            if distance[i] == smallest:
                if in_tree[i] == False:
                    completed = True
                    return i
                else:
                    count += 1
print(next_vertex([True, True, True, False, True],[float("inf"),0,float("inf"),float("inf"),float("inf")]))
                    
def dijkstra(adj_list, start):
    """Implements dijkstras algorithm"""
    
    def next_vertex(in_tree, distance):
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
        return next_vert
    
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
    return parent, distance