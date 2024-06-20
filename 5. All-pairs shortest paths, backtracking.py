def adjacency_list(graph_str):
    """creates a adj list from a str"""
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
    """creates a distance matrix froma adj_list"""  
    result = [[]for i in range(len(adj_list))]
    
    for i in result:
        for j in range(len(result)):
            i.append(float("inf"))

    for i in range(len(adj_list)):
        result[i][i] = 0

        for j in adj_list[i]:            
            result[i][j[0]] = (j[1])
            
    return result

def floyd(distance):
    """flouds algorithm needs distacne matix as well as afj_lsit maker"""
    n = len(distance)
    for k in range(0, n):
        for i in range(0, n):
            for j in range(0, n):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
    
    return distance
#-----------------------------------------------------------------------------
def permutations(s):
    solutions = []
    dfs_backtrack((), s, solutions)
    return solutions


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

def is_solution(candidate, input_data):
    """Returns True if the candidate is complete solution"""
    if set(candidate) == set(input_data):
        return True
    else:
        return False


def children(candidate, input_data):
    """Returns a collestion of candidates that are the children of the given
    candidate."""
    
    child = []
    
    for item in input_data:
        if item not in candidate:
            child.append(candidate+(item,))
            
    return child

def should_prune(candidate):
    return False
#------------------------------------------------------------------------------