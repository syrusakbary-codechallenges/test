#http://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance
def DamerauLevenshteinDistance(s1, s2,_add,_del,_swap):
    d = {}
    lenstr1 = len(s1)
    lenstr2 = len(s2)
    for i in xrange(-1,lenstr1+1):
        d[(i,-1)] = i+1
    for j in xrange(-1,lenstr2+1):
        d[(-1,j)] = j+1
 
    for i in xrange(0,lenstr1):
        for j in xrange(0,lenstr2):
            if s1[i] == s2[j]:
                cost = 0
            else:
                cost = _swap
            d[(i,j)] = min(
                           d[(i-1,j)] + _del, # deletion
                           d[(i,j-1)] + _add, # insertion
                           d[(i-1,j-1)] + cost, # substitution
                          )
            if i>1 and j>1 and s1[i]==s2[j-1] and s1[i-1] == s2[j]:
                d[(i,j)] = min (d[(i,j)], d[i-2,j-2] + cost) # transposition
 
    return d[lenstr1-1,lenstr2-1]

print DamerauLevenshteinDistance('123','345',1,1,1)