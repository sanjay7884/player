n=int(input())
result=0
while(n>0):
  num=int(n%10)
  result = int((result*10) +(num))
  n = int(n/10)
print (result)
