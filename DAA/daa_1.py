def fiboRecursive(n):
    if n == 0 or n==1:
        return n
    else:
        return fiboRecursive(n-1) + fiboRecursive(n-2)
    
def fiboIterative(n):
    if n == 0 or n==1:
        return n
    else:
        n1 = 0
        n2 = 1
        for i in range(2, n+1):
            n3 = n1 + n2
            n1 = n2
            n2 = n3
    return n3
        
print(fiboIterative(6))
print(fiboRecursive(7))
