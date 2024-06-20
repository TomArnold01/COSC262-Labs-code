def key_positions(seq, key):
    """returns an array (list) such that the i-th element of the array is the
    starting position (in the sorted output of the counting sort algorithm)
    of objects in seq whose key is i."""
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

def sorted_array(seq, key, positions):
    """uses key_positions, produces an array (list) containing the elements of seq sorted according to the key function"""
    output= [0] * len(seq)
    for item in seq:
        output[positions[key(item)]] = item
        positions[key(item)] = positions[key(item)] + 1
    return output

def sort(UnsortedList,position):
    bucket = []
    for i in range(0,10):
        poslist = []
        bucket.append(poslist)

    for num in UnsortedList:
        numstr = str(num)
        posval = 0
        if(len(numstr) >= position): 
            posval = ord(numstr[-position]) - ord('0') 
            bucket[posval].append(num)
        else:
            bucket[0].append(num)

    sortedList = []
    for poslist in bucket:
        for num in poslist:
            sortedList.append(num)

    return sortedList
    
def radix_sort(UnsortedList,maxpos):
    """takes a sequence of natural numbers called numbers and uses counting 
    sort iteratively to sort the sequence up to the d-th digit from the
    right."""
    finalList = UnsortedList
    for position in range(1,maxpos+1):
        finalList = sort(finalList, position)

    return finalList


