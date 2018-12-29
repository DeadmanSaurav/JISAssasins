fun= lambda  x :ord(x)
n=input("Enter character: ")
result = fun(n)
print("ASCII value is {}".format(result))

c= result+1
d= result-1
print("Next value is : {} or Previous value is : {}".format(c,d))
