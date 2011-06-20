def primes(n): 
    if n==2: return [2]
    elif n<2: return []
    s=range(3,n+1,2)
    mroot = n ** 0.5
    half=(n+1)/2-1
    i=0
    m=3
    while m <= mroot:
        if s[i]:
            j=(m*m-3)/2
            s[j]=0
            while j<half:
                s[j]=0
                j+=m
        i=i+1
        m=2*i+3
    return [2]+[x for x in s if x]

def ispalindrome(x):
    string=str(x)
    if string==string[::-1]:
        return True
    else:
        return False
       
n=200
p = primes(n)
l = []
k = []
for i in p:
	b = str(i)
	reversed = int(b[::-1])

	if ispalindrome(i): k.append(i)
	if reversed in p: l.append(i)

n = 100
k = filter(lambda x:x<200,k)
l = filter(lambda x:x<200,l)
u = sum(k)
b = sum(l)
print b-u