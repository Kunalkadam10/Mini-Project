import random
import json
class Bank:
    account_no = {}
    customer_id = {}
    a = 0
    def __init__(self, balance=0):
        self.balance = balance
        self.acc_pin = 0
        self.accno = 0

    @staticmethod
    def generate_acc_no():
        return random.randint(100000, 999999)

    def create_acc(self):
        self.accno = self.generate_acc_no()
        self.acc_pin = self.set_pin()
        Bank.account_no[str(self.accno)] = {"Pin" : self.acc_pin , "Balance" : self.balance}
        print(f"your account no : {self.accno}")
        self.save_data()
        return Bank.account_no
    
    def display(self):
        #Bank.account_no[self.accno] = {"Pin" : self.acc_pin , "Balance" : self.balance}
        print(f"your balance : {Bank.account_no[str(self.accno)]["Balance"]} ")
        return 
        
    @staticmethod
    def set_pin():  
        while True:
            try:
                a = int(input("Set four digit pin : "))
                if  1000 <=a <= 9999:
                    print("pin set succesfully")
                    return a
                else:
                    print("enter valid pin ")
            except:
                print("enter 4 digit pin")

    def credit(self): 
        self.amount = int(input("Enter amount : "))
        self.balance += self.amount
        print(f"Credited : {self.amount}...")
        self.bal()
        return self.balance

    def debit(self):
        self.amount = int(input("Enter amount : "))
        if self.amount > self.balance:
            print("Insufficient balance .")
        else:
            self.balance -= self.amount
            print(f"Debited : {self.amount}...")
        self.bal()
        return self.balance


    def login(self):
        self.id = input("enter acc_no : ")
        self.p = int(input("enter pin : "))
        if self.id in Bank.account_no and Bank.account_no[self.id]["Pin"] == self.p:
                print("Login successful.")
                self.accno = self.id
                self.acc_pin = self.p
                self.balance = Bank.account_no[self.id]["Balance"]
                return True
        else:
            print("incorrect account_no or pin .")
            return False
        
    
    def bal(self):
        self.account_no[self.accno]["Balance"] = self.balance
        self.save_data()
        # with open('acc_details.txt' , 'w') as f :
            # json.dump(self.account_no , f , indent = 2)
        print(f"your update balance : {self.account_no[self.accno]["Balance"]}")

    @classmethod
    def save_data(cls):
         with open('acc_details.txt' , 'w') as f:
             json.dump(cls.account_no,f ,indent = 2)

    @classmethod
    def load_data(cls):
        try:
            with open('acc_details.txt','r') as f:
                cls.account_no = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            cls.account_no = {}


def main():
    user = None
    while True:
        print("\nWelcome to the Bank System")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            user = Bank()
            user.create_acc()
            

        elif choice == "2":
            user = Bank()
            if user.login():
                while True:
                    print("\n1. Deposit Money")
                    print("2. Withdraw Money")
                    print("3. Display Balance")
                    print("4. Logout")

                    action = int(input("Choose action: "))

                    if action == 1:
                        user.credit()

                    elif action == 2:
                        user.debit()

                    elif action == 3:
                        user.display()
                        

                    elif action == 4:
                        print("Log OUT ")
                        break

                    else:
                        print("enter valid option")
        elif choice == "3":
            print("Thank YOU")
            break
        else:
            print("enter valid option")

if __name__ == "__main__":
    Bank.load_data()
    main()

