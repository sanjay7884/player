str1=str(input())
l=list(str1)
l[::2],l[1::2] =l[1::2],l[::2]
print (''.join(l))
