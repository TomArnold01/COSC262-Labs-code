def next_vertex(in_tree, distance):
    count = 0
    completed = False
    sorted_list = sorted(distance)
    while completed == False:
        for i in range(len(distance)):
            smallest = sorted_list[count]
            if distance[i] == smallest:
                if in_tree[i] == False:
                    completed = True
                    return i
                else:
                    count += 1
    


from math import inf
in_tree = [False, True, True, False, False]
distance = [float('inf'), 0, 3, 12, 5]
print(next_vertex(in_tree, distance))

