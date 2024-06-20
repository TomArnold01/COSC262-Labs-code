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

def dijkstra(adj_list, start):
    """Implements dijkstras algorithm"""
    
    def next_vertex(in_tree, distance):
        """Helper function to gain the next vertex to
        be used in Prim's and Dijkstra's algorithm"""
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
    
    
    
graph_string = """\
D 3 W
1 0 3
2 0 1
1 2 1
"""

print(dijkstra(adjacency_list(graph_string), 1))
