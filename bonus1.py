Bonus
a=0
b=0
def myfun():
    global a,b
    n=int(input("Enter a number"))
    if num==n:
        a=a+1
        
        print(" {} cow\n  {} bull\n".format(a,b))
    elif num<n:
        b=b+1
        print(" {} Cow\n {} bull ".format(a,b))
        
    while 1:
        a=input("do you want to do it again? 1.y or 2.no")
        
        if a==1:
            myfun()
        else:
            break