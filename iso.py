str1,str2=list(map(str,input().split()))
x=len(set(str1))
y=len(set(str2))
if x==y:
  print("yes")
else:
  print("no")
