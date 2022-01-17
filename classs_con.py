class gpay:
    print("WELCOME TO BANK OF LOHARA")
    mob=int(input("Enter the mo number:"))
    upiid= 45613
    ifsc = 123456
    def __init__(self,name,balance = 50000):
        self.name=name
        self.balance=balance
    def d_mob(self,amount):
        import time
        print("for online mobile banking mobile no is:",self.mob)
        time.sleep(3)
        self.balance=self.balance+amount
        time.sleep(3)
        print(self.name, "your ifsc is ",self.ifsc)
        print("Your acc balnce is :",self.balance)
    def with_D(self):
        import time
        pin = 1234
        mypin=int(input("please enter the pin:"))
        time.sleep(3)
        amount=int(input("enter withdraw amount:"))
        print("loading...............................")
        time.sleep(4)
        if pin == mypin:
            self.balance=self.balance-amount
            print("cash withdrawl succefful:",amount,"INR")
            print("your available balance is:",self.balance,"INR")
        else:
            print("please check pin")

x = input("Enter the name:")
y = int(input("Enter the deposit amount:"))

k=gpay(x)
k.d_mob(y)
k.with_D()








