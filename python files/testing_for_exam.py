num_calls = 0  # Global counter of mat_mul calls

def mat_mul(m1, m2):
    """Return m1 * m2 where m1 and m2 are square matrices of numbers, represented
       as lists of lists.
    """
    global num_calls # Counter of calls (for marking)
    num_calls += 1   # Increment the count of calls
    n = len(m1)    # Size of the matrix
    assert len(m1[0]) == n and len(m2) == n and len(m2[0]) == n
    mprod = [[sum(m1[i][k] * m2[k][j] for k in range(n)) for j in range(n)]
        for i in range(n)]
    return mprod


#m1 = [[1, 2, -1],
      #[2, 3, 1], 
      #[-3, -2, -1]]

#m2 = [[4, 2, 1], 
      #[1, 3, 5], 
      #[2, 1, -1]]
#product = mat_mul(m1, m2)
#print(product)

def mat_power(m, p):
    A=[]
    B=[]
    for row in m:
        temp=[]
        for col in row:
            temp.append(col)
        A.append(temp)
        B.append(temp)
   
    for i in range(p-1):
        A=mat_mul(A,B)
   
    return A    
	
## Simple case of squaring a matrix
#m = [[1, 2, 3], [0, -1, 3], [2, 4, 1]]
#print(mat_power(m, 2))    

def fractional_knapsack(capacity, items):
    
    in_order = []
    #sorts the list in the format of "profit/weight, name, profit, weight"
    for item in items: 
        devision = item[1] / item[2]
        in_order.append((devision, item[0], item[1], item[2]))
    in_order = sorted(in_order)[::-1] #puts the list in highest to lowest order

    count = 0
    weight = 0
    #uses one of each item until the weight equals the capacity 
    for each in in_order:
    
        if weight <= capacity:
    
            if each[3] > (capacity-weight): #for when fractions are needed
                test = 0
                item_weight =each[3] 
                # if the weight of the item is too big to fit this will
                # fractionizes it
                while item_weight !=(capacity-weight):
                    test +=1
                    item_weight -= 1
                weight += item_weight
                count += (each[2] / each[3])*item_weight 
                break
    
            weight += each[3]
            count += each[2]
        else: break
    
    return count
    
    
# The example from the lecture notes
items = [
    ("Chocolate cookies", 20, 5),
    ("Potato chips", 15, 3),
    ("Pizza", 14, 2),
    ("Popcorn", 12, 4)]
print(fractional_knapsack(9, items))