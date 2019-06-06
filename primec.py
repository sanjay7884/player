n1,n2=input().split()
p=0
for i in range(int(n1),int(n2)+1):
    s=1
    n=0
    while s<=i:
        if i%s==0:
            n+=1
        s+=1
    if n==2:
        p+=1
print(p)
