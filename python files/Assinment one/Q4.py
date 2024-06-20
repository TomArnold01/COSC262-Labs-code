#done

def which_segments(city_map):
    
    result = []
    graphInput = city_map.split("\n")    
    adj_list = adjacency_list(city_map)
    parents = prim(adj_list, 0)  
    for i in range(len(parents)):
        if parents[i] != None:
            first = min(parents[i], i)
            last = max(parents[i], i)
            result.append((first, last))
    return result
    
    
def prim(adj_list, start):
    """Implements prim algorithm"""
    
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
            if not in_tree[vertex] and weight < distance[vertex]:
                distance[vertex] = weight
                parent[vertex] = next_vert
    return parent


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
	
	
	
city_map = """\
U 3 W
0 1 1
2 1 2
2 0 4
"""

print(sorted(which_segments(city_map)))