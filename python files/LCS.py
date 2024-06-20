

def lcs(s1, s2, memo=None):
    if memo == None:
        memo = {}
    
    if s1 == '' or s2 == '':
        return ''
    elif s1[-1] == s2[-1]: 
        return lcs(s1[:-1], s2[:-1]) + s1[-1]
    else:
        if (s1[:-1], s2) not in memo:
            soln1 = lcs(s1[:-1], s2)
        else:
            return memo[s1[:-1], s2]
        if (s1, s2[:-1]) not in memo:
            soln2 = lcs(s1, s2[:-1])
        else:
            return memo[(s1, s2[:-1])]
        
        
        
        if len(soln1) > len(soln2):
            memo[(s1,s2)] = soln1
            return soln1
        else:
            memo[s1,s2] = soln2
            return soln2





s1 = "Solidandkeen\nSolidandkeen\nSolidandkeen\n"
s2 = "Whoisn'tsick\nWhoisn'tsick\nWhoisn'tsick"
lcs_string = lcs(s1, s2)
print(lcs_string)
print(repr(lcs_string))