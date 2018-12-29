class Number:
    def check(self,ch):
        if (ch>='a'and ch<='z'):
            print("Its an alphabet")
        elif(int(ch)>=0 and int(ch)<=9):
            print("Its an number")
            
ss=Number()
ch=input("Enter a charcater")
ss.check(ch)
