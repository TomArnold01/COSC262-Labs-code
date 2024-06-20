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
#------------------------------------------------------------------------------

def all_paths(adj_list, source, destination):
    paths = []
    dfs_backtrack((source,), adj_list, paths)


def dfs_backtrack(candidate, input_data, output_data):
    if should_prune(candidate):
        return
    if is_solution(candidate, input_data):
        add_to_output(candidate, output_data)
    else:
        for child_candidate in children(candidate, input_data):
            dfs_backtrack(child_candidate, input_data, output_data)


def add_to_output(candidate, output_data):
    output_data.append(candidate)


def should_prune(candidate):
    return False


def is_solution(candidate, input_data):
    return len(candidate) == len(input_data)


def children(candidate, input_data):
    result = []
    holder = []
    for items in input_data:
        for j in items:
            holder.append(j[0])
    for items in candidate:
        if items in holder:
            result.append(candidate + (items,))

    return result
triangle_graph_str = """\
U 4
0 1
1 2
2 0
"""

adj_list = adjacency_list(triangle_graph_str)
print((all_paths(adj_list, 0, 2)))
