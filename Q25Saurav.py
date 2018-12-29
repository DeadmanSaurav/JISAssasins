class Number:
    def check(self,ch):
        if (ch>='a'and ch<='z'):
            print("Its an alphabet")
        elif(int(ch)>=0 and int(ch)<=9):
            print("Its an number")
            
gk=Number()
ch=input("Enter a charcater")
gk.check(ch)
