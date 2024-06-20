def line_edits(str1, str2):
    """
        Is the bottom-up version of the line_edits algoithm, substitution is 
        preferred over deletion which in turn is preferred over insertion
    """
    str1 = str1.splitlines()
    str2 = str2.splitlines()
    m = len(str1)
    n = len(str2)
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j   
            elif j == 0:
                dp[i][j] = i   
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                movement = min(dp[i][j-1] , dp[i-1][j], dp[i-1][j-1] )
                dp[i][j] = 1 + movement

    return traverse(dp, str1, str2)


def traverse(dp, str1, str2):
    """
        Takes a table of for line_edits then traverses the table, returns a 
        list of tuples containing the movement and the strings
    """
    memo = []
    done = False
    m = len(str1)
    n = len(str2)    
    
    while done != True:
        movement = min(dp[m][n-1], dp[m-1][n], dp[m-1][n-1])    
        if m == 0 and n == 0:
            done = True     
        elif len(str2) == 0:
            memo.append(("D",str1[m-1], ""))
            break
        elif len(str1) == 0:
            memo.append(("I", "", str2[n-1]))
            break
        
        elif movement == dp[m-1][n-1]:
            if str1[m-1] == str2[n-1]:
                memo.append(("C",str1[m-1], str2[n-1]))
            else:
                memo.append(("S",str1[m-1], str2[n-1]))
            m -= 1
            n -= 1
        elif movement == dp[m-1][n] :
            memo.append(("D",str1[m-1], ""))
            m -= 1
        elif movement == dp[m][n-1]  :
            memo.append(("I", "", str2[n-1]))
            n -= 1
    return memo[::-1]
    

s1 = "Line1\nLine2\nLine3\nLine4\n"
s2 = "Line1\nLine3\nLine4\nLine5\n"
table = line_edits(s1, s2)
for row in table:
    print(row)

print("---------------------")

s1 = "Line1\nLine2\nLine3\nLine4\n"
s2 = "Line5\nLine4\nLine3\n"
table = line_edits(s1, s2)
for row in table:
    print(row)
    
print("-----------------")

s1 = "Line1\n"
s2 = ""
table = line_edits(s1, s2)
for row in table:
    print(row)