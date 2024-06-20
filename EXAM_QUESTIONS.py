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

def itinerary(adj_list, start, destination):
    
    result = []
    connected = []
    somthing = dijkstra(adj_list, start)

    if somthing[1][destination] == float("inf"):
        return result
    elif start == destination:
        result.append((destination,0))
        return result
    else:
        result.append((start,0))
        test = destination
        while test != start:
            if somthing[0][test] == start:
                result.append((test,somthing[1][test]))
                break
            else:
                test = somthing[0][test]
    
    return result
        
    

    
    
map_graph_string = """\
U 4 W
0 1 4
1 2 5
"""

adj_list = adjacency_list(map_graph_string)

print(itinerary(adj_list, 0, 2))
print(itinerary(adj_list, 2, 1))
print(itinerary(adj_list, 1, 1))
print(itinerary(adj_list, 1, 3))