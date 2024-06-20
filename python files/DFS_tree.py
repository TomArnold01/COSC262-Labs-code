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

    return parent

adj_list = [
    [],
    [(2, None), (5, None), (6, None)],
    [(1, None), (3, None), (5, None)],
    [(2, None), (4, None)], 
    [(3, None), (5, None)], 
    [(1, None), (2, None), (4, None)],
    [(1,None)]
]

print(dfs_tree(adj_list, 1))
