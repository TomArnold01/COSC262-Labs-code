def format_sequence_helper(dict, source, destination, short_path=[]):
    
    short_path = short_path + [source]
    if source == destination:
        return short_path
    if source not in dict.keys():
        print("No solution!")
        exit()
    req_path = None
    for val in dict[source]:
        if val not in short_path:
            new_path = format_sequence_helper(dict, source, destination, short_path)
            if new_path:
                if not req_path or len(new_path) < len(req_path):
                    req_path = new_path
    
    return req_path

def format_sequence(converters_info, source_format, destination_format):
    
    dict = {}
    
    for line in converters_info.splitlines():
        k, v = line.split()
        if k != "D":
            if k in dict:
                dict[k].append(v)
            else:
                dict[k] = [v]
    res = format_sequence_helper(dict, source_format, destination_format)
    res = [int(i) for i in res]
    return res

converters_info_str = """\
D 5
0 1
0 2
1 2
2 3
1 3
3 0
"""

print(format_sequence(converters_info_str, 1, 0))
print(format_sequence(converters_info_str, 0, 3) in [[0, 1, 3], [0, 2, 3]])
print(format_sequence(converters_info_str, 4, 4))
print(format_sequence(converters_info_str, 3, 3))
print(format_sequence(converters_info_str, 3, 2))
print(format_sequence(converters_info_str, 3, 4))


#[1, 3, 0]
#True
#[4]
#[3]
#[3, 0, 2]
#No solution!