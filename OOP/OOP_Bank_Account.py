class BankAccount:
    balance : int

    def __init__(self, balance):
        self.balance =  balance

    def print_balance(self):
        current_balance = self.balance
        print(f"Your balance is: ${current_balance}")    

    def deposit_money(self, amount):
        print(f"You made a deposit of: ${amount}")
        self.balance = self.balance + amount
        print(f"Your new balance is: ${self.balance}")

    def withdraw_money(self, amount):
        print(f"You withdraw: ${amount}")
        withdrawn_amount = self.balance - amount
        if withdrawn_amount <= 0:
            print(f"You don't have enough funds to withdraw money from your savings accont ")
        else:    
            print(f"Your new balance after withdrawing money is: ${withdrawn_amount}")




class SavingsAccount(BankAccount):
    balance : int 

    def __init__(self, balance):
        self.balance = balance
        

    def withdraw_money(self, amount):
        withdrawn_amount = amount
        new_balance = self.balance - amount

        if withdrawn_amount > self.balance:
            print("Not enough funds to withdraw")
        else:
            print(f"Your balance after withdrawing is: {new_balance}")


    

        



my_bank_account = BankAccount(1000)
my_bank_account.print_balance()
my_bank_account.deposit_money(1500)
my_bank_account.withdraw_money(100)

# my_savings = SavingsAccount(1000)
# my_savings.print_balance()
# my_savings.withdraw_money(900)