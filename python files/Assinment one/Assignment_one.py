def format_sequence(converters_info, source_format, destination_format):
    """Find the shorts path from the source_format (which is the 
    starting node) to the desination_format (which is the end node) using the
    graph that is givien. if there is no path then "No solution!" id returned
    """

    len_adj = len(adj_list)
    
    
  
    
    

    

	
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
#print(format_sequence(converters_info_str, 0, 3) in [[0, 1, 3], [0, 2, 3]])
#print(format_sequence(converters_info_str, 4, 4))
#print(format_sequence(converters_info_str, 3, 3))
#print(format_sequence(converters_info_str, 3, 2))
#print(format_sequence(converters_info_str, 3, 4))


#[1, 3, 0]
#True
#[4]
#[3]
#[3, 0, 2]
#No solution!