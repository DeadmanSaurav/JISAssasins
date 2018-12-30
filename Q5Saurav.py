#not completed

class Customer:
    acc_no=[]
    names=[]
    balance=[]
    def __init__(self,ac=[],name=[],bal=[]):
        self.acc_no=ac
        self.names=name
        self.balance=bal
    def check(self):
        for x in self.balance:
            if x<100:
                print("Account number:",acc_no)
                print("Name:",names)

ac_no=[]
names=[]
balance=[]
for x in range(1,4):
    ac=int(input("Account no:"))
    ac_no.append(ac)
    name=input("Enter Name:")
    names.append(name)
    bal=int(input("Enter Balance"))
    balance.append(bal)
print("Acc_no={}, Name={}, balance={}".format(ac_no,names,balance))
c=Customer(ac_no[:],names=[],balance=[])
c.check()
