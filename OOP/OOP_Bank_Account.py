class Bank_Account:
    balance : int

    def __init__(self, balance):
        self.balance =  balance

    def print_balance(self, balance):
        current_balance = self.balance
        print(f"Your balance is: ${current_balance}")    

    def deposit_money(self, balance):
        new_deposit = 0
        print(f"You made a deposit of: ${balance}")
        new_deposit = self.balance + balance
        print(f"Your new balance is: ${new_deposit}")

    def withdraw_money(self, balance):
        print(f"You withdraw: ${balance}")
        withdrawn_amount = self.balance - balance
        if withdrawn_amount <= 0:
            print(f"You don't have enough funds to withdraw money from your savings accont ")
        else:    
            print(f"Your new balance after withdrawing money is: ${withdrawn_amount}")




class Savings_Account(Bank_Account):
    balance : int 

    def __init__(self, balance):
        self.balance = balance



#my_bank_account = Bank_Account(1000)
#my_bank_account.print_balance(1000)
#my_bank_account.deposit_money(500)
#my_bank_account.withdraw_money(100)

my_savings = Savings_Account(1000)
my_savings.print_balance(1000)
my_savings.withdraw_money(2000)