msg=input("Enter a string:")
z=msg.split()
print(z)
i=0
for x in z:
    m=x.split()
    for y in m:
        if y in "aeiou":
            del x[i]
        i+=1
print(msg)
