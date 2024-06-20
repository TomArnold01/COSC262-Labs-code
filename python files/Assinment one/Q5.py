#done

def  min_capacity(city_map, depot_position):
    
    graphInput = city_map.split("\n")    
    adj_list = adjacency_list(city_map)
    distance = dijkstra(adj_list, depot_position)
    max_dis = 0 
    for item in distance:
        if item != float("inf"):
            if item >=  max_dis:
                max_dis = item
    max_dis += max_dis*3 
    
    return max_dis

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
              
    return distance


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
U 4 W
0 2 5
0 3 2
3 2 2
2 1 10
"""

print(min_capacity(city_map, 0))
print(min_capacity(city_map, 1))
print(min_capacity(city_map, 2))
print(min_capacity(city_map, 3))