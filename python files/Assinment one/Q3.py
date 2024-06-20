#done

def build_order(dependencies):
    
    graphInput = dependencies.split("\n")
    
    n = (int)(graphInput[0].split(" ")[1])
    
    graph = [[] for _ in range(n)]
    
    for line in range(1, len(graphInput) - 1):
        edge = graphInput[line].split(" ")
        graph[(int)(edge[0])].append((int)(edge[1]))
    
    def dfs(u, visited, stack):
        visited[u] = True
        
        for v in graph[u]:
            if visited[v] == False:
                dfs(v, visited, stack)
        stack.insert(0, u)
    
    stack = []
    visited = [False] * n
    
    for u in range(n):
        if visited[u] == False:
            dfs(u, visited, stack)
    return stack


dependencies = """\
D 3
"""
# any permutation of 0, 1, 2 is valid in this case.
solution = build_order(dependencies)
if solution is None:
    print("Wrong answer!")
else:
    print(sorted(solution))