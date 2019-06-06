str1=str(input())
str2=str(input())
a=[char for char in str1]
b=[char for char in str2]
x=len(set(a))
y=len(set(b))
if x==y:
  print("yes")
else:
  print("no")
