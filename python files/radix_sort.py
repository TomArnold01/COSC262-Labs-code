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
    finalList = UnsortedList
    print(UnsortedList)                                  #Framework
    for position in range(1,maxpos+1):
        finalList = sort(finalList, position)
        print(position)                                  #Framework
        print(finalList)                                 #Framework
        print()                                          #Framework

    return finalList
print(radix_sort([31,22,131,44],2))