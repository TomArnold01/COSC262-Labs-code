# done

def  bubbles(physical_contact_info, start = 0, parent = None, state = None):
    
    result = []
    holder = []
    tracker = []
    info = physical_contact_info.split()

    if len(info) == 2:
        for i in range(int(info[1])):
            result.append([i])
        return result
        
        
    adj_list = adjacency_list(physical_contact_info)

    for i in range(len(adj_list)):
        connections = dfs_tree(adj_list, i , parent=None, state=None)
        for j in range(len(connections)):
            if connections[j] == True:
                if j not in tracker:
                    holder.append(j)
                    tracker.append(j)
        if len(holder) > 0:            
            result.append(holder)
        holder = []
    return result
    



 
def dfs_tree(adj_list, start, parent=None, state=None):

    if parent is None:
        parent = [None]*len(adj_list)
    if state is None:
        state = [False]*len(adj_list)
    state[start] = True

    for item in adj_list[start]:
        if state[item[0]] == False:    
            parent[item[0]] = start
            dfs_tree(adj_list, item[0], parent, state)
    state[start] = True

    return state
  
 
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

   
physical_contact_info = """\
U 1
"""

print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))