class Prime:
    def check(self,p):
        print("Prime numbers are\n")
        for self.x in p:
            self.flag=0
            for self.i in range(2,self.x):
                if (self.x%self.i==0):
                    break
                else:
                    
                    print(self.x)
                    break
            
me=[]
n=int(input("Enter how many number you want to insert"))
print("Enter the numbers")
i=0
while(i<n):
    me.append(int(input()))
    i=i+1
ss=Prime()
ss.check(me)
