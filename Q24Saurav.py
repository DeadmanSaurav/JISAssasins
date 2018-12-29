class Multiplication:
    def mul(self,n):
        self.i=1
        while(self.i<=10):
            print(n,"x",self.i,"=",self.i*n)
            self.i+=1
ss=Multiplication()
n=int(input("Enter a number to print its multiplication table"))
ss.mul(n)
