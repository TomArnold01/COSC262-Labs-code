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



def transpose(adj_list):
    
    transpose_adj_list = [[] for i in range(0, len(adj_list))]
    for i in range(0, len(adj_list)):

        for j in range(0, len(adj_list[i])):

            transpose_adj_list[adj_list[i][j][0]].append((i, adj_list[i][j][1]))

    return transpose_adj_list


graph_string = """\
U 17
1 2
1 15
1 6
12 13
2 15
13 4
4 5
"""

graph_adj_list = adjacency_list(graph_string)
graph_transposed_adj_list = transpose(graph_adj_list)
for i in range(len(graph_transposed_adj_list)):
    print(i, sorted(graph_transposed_adj_list[i]))