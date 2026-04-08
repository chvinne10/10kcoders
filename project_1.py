class Bank_Management_System:

    def __init__(self):
        self.accounts = {}
        self.trans = []

    def createaccount(self, acc_no, name, bal, type):

        self.accounts[acc_no] = {
            "name": name,
            "bal": bal,
            "type": type,
        }

    def Deposite(self, acc_no, amount):

        self.accounts[acc_no]["bal"] += amount
        self.trans.append(f"{acc_no} deposit {amount}")

    def Withdraw(self, acc_no, amount):

        if self.accounts[acc_no]["bal"] < amount:
            print("Insufficient")

        else:
            self.accounts[acc_no]["bal"] -= amount

    def Check_balance(self, acc_no):

        print(self.accounts[acc_no]["bal"])

    def Transaction_history(self):

        print(self.trans)
bms=Bank_Management_System()
while True:
    print("1. Create Account\n2. Deposit\n3. Withdraw\n4. Check Balance\n5. Transaction History")
    x=input("Enter your choice: ")
    match x:
        case "1":
            acc_no = input("Enter account number: ")
            name = input("Enter name: ")
            bal = float(input("Enter balance: "))
            type = input("Enter account type: ")
            bms.createaccount(acc_no, name, bal, type)

        case "2":
            acc_no = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            bms.Deposite(acc_no, amount)

        case "3":
            acc_no = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            bms.Withdraw(acc_no, amount)

        case "4":
            acc_no = input("Enter account number: ")
            bms.Check_balance(acc_no)

        case "5":
            bms.Transaction_history()
        
        case "6":
            break
        case _:
            print("Invalid choice")