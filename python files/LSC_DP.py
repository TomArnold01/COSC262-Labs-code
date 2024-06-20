def lcs(s1, s2):
    """
    implements a DP veriton of Longest Common Subsequenece without 
    using recurtion
    """
    m = len(s1)
    n = len(s2)
    table = [[0 for x in range(n+1)] for x in range(m+1)]
   
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                table[i][j] = table[i-1][j-1] + 1
            else:
                table[i][j] = max(table[i][j-1], table[i-1][j])

    temp = table[m][n]
    result = [""] * (temp+1)
    result[temp] = ""
    i = m
    j = n
    while i > 0 and j > 0:
      
        if s1[i-1] == s2[j-1]:
            result[temp-1] = s1[i-1]
            i-=1
            j-=1
            temp -=1
        elif table[i-1][j] > table[i][j-1]:
            i-=1
        else:
            j-=1
  
    return("".join(result))