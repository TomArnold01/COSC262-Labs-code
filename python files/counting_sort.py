def counting_sort(A, key):
    """
        this the the count sotr algorithm using a list as the set of keys 
    """
    B = [0] * len(A)
    for i in key:
        if i <0:
            i = i*-1   
    P = key_positions_key_list(A, key)
    print("P = {}".format(P))
    for a in A:
        print("a = {}".format(a))                       #framework
        print("key[a] = {}".format(key[a]))             #framework
        print("P[key[a]] = {}".format(P[key[a]]))       #framework      
        B[P[key[a]]] = a
        P[key[a]] += 1
        print(B)                                        #framework
        print(P)                                        #framework
        print()                                         #framework
    return B

def key_positions_key_list(A, key):
    """
        this is the helper function for count sort using a list as the keys
    """
    k=max(key)
    C = [0] * (k+1)
    for i in range(0,k):
        C[i] = 0
    for a in range(0,len(A)):            
        C[key[a]] = C[key[a]]+1
    total = 0
    for i in range(0,k+1):
        C[i], total = total, total+C[i]
    return C

#print(counting_sort([2,-2,1],[4,4,1]))

#******************************************************************************
#******************************************************************************
#*******Same algorthims but the one below uses the lambda function*************
#******************************************************************************
#******************************************************************************

def sorted_array(seq, key):
    """
       This is count sort
    """
    positions = key_positions(seq, key)
    output= [0] * len(seq)
    for item in seq:
        print("a = {}".format(item))                       #framework
        print("key[a] = {}".format(key(item)))             #framework
        print("P[key[a]] = {}".format(positions[key(item)]))#framework      
        
        output[positions[key(item)]] = item
        positions[key(item)] = positions[key(item)] + 1
        print(output)                                        #framework
        print(positions)                                     #framework
        print()                                              #framework        
    return output

def key_positions(seq, key):
    """
       this is the helper function for count sort using the lambda 
       functions as the key
    """
    largest = 0
    
    for items in seq:
        if key(items) >= largest:
            largest = key(items)
    new_array = [0]*(largest+1)
    
    for item in seq:
        new_array[key(item)] = (new_array[key(item)] + 1)
    total_count = 0

    for i in range(0,largest+1):
        new_array[i], total_count = total_count, total_count + new_array[i]
    return new_array



print(sorted_array([1,2,0,-1], lambda x: abs(x)))