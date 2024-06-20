def adjacency_list(graph_str):
    
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

def bfs_tree(adj_list, start):

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


def is_strongly_connected(adj_list):
    """ Returns True if the graph is strongly connected otherwise false
    
    """

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

