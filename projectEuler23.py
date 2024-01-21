addSUM=[]
def sum_of_divisors(n):
    s=0
    for i in range(2, int(n**0.5)+1):
        if (n % i == 0) and (i == n//i):
            s+=i
        elif n % i == 0:
            s+=(i+n//i)
    return s+1
for i in range(1, 28124):
    if sum_of_divisors(i)>i:
        addSUM.append(i)
t=int(input().strip())
for _ in range(t):
    n=int(input().strip())
    if n<28124:
        i=0
        while n >= addSUM[i]:
            if (n-addSUM[i]) in addSUM:
                print("YES")
                break
            i+=1
        else:
            print("NO")
    else:
        print("YES")
