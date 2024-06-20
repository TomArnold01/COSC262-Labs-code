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


def distance_matrix(adj_list):
    #print(adj_list)    
    result = [[]for i in range(len(adj_list))]
    for i in result:
        for j in range(len(result)):
            i.append(float("inf"))

    for i in range(len(adj_list)):

        result[i][i] = 0

        for j in adj_list[i]:

            
            result[i][j[0]] = (j[1])
    return result


graph_str = """\
U 4 W
0 1 3
1 2 1 
2 3 2
2 0 3
3 0 6
3 1 4
"""

adj_list = adjacency_list(graph_str)
print(distance_matrix(adj_list))

#more readable output (less readable code):
print("\nEach row on a new line:")
print("\n".join(str(lst) for lst in distance_matrix(adj_list)))
