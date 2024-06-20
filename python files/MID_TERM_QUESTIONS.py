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

def reaching_vertices(adj_list, target):
    
  
    queue = bfs_tree(adj_list, target)

    return queue
    
def bfs_tree(adj_list, start):
    """Runs a BFS on an adj_list this will return parent"""
    length = len(adj_list)
    parent = [None] * length
    visited = [False] * length
  
    visited[start] = True
    test = []
    queue = []
    queue.append(start)
    test.append(start)
    while len(queue) != 0:
        node_pop = queue.pop(0)
        neighbours = adj_list[node_pop]
        for node_v, weight in neighbours:
            if visited[node_v] is False:
                visited[node_v] = True
                parent[node_v] = node_pop
                queue.append(node_v)
                test.append(node_v)
    return test

graph_string = """\
D 3
0 1
1 0
0 2
"""

adj_list = adjacency_list(graph_string)
print(sorted(reaching_vertices(adj_list, 0)))
print(sorted(reaching_vertices(adj_list, 1)))
print(sorted(reaching_vertices(adj_list, 2)))

