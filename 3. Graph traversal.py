def adjacency_list(graph_str):
    """Creates a adjacency list out of a string"""
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

def adjacency_matrix(graph_str):
    """Creates a adjacency matrix out of a string"""
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
    
def bfs_tree(adj_list, start):
    """does a BFS search on a adj_list froma starting point"""
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
    return parent

def dfs_tree(adj_list, start, parent=None, state=None):
    """performs a DFS search on a adj list from a starting point"""
    if parent is None:
        parent = [None]*len(adj_list)
    if state is None:
        state = [False]*len(adj_list)
    state[start] = True

    for item in adj_list[start]:
        if state[item[0]] == False:    
            parent[item[0]] = start
            dfs_tree(adj_list, item[0], parent, state)
    state[start] = True

    return parent
