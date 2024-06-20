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
    """returns a list of the vertices reaching the target"""    

    connected = []
    connected.append(target)
    for i in range(len(adj_list)):
        for j in adj_list[i]:
            if j[0] in connected:
                connected.append(i)
    return connected
    	
graph_string = """\
D 3
0 1
1 2
2 0
"""

adj_list = adjacency_list(graph_string)
for target in range(len(adj_list)):
    print(sorted(reaching_vertices(adj_list, target)))