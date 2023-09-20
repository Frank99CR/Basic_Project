class Bank_Account:
    balance : int
    amount : int

    def __init__(self, balance, amount):
        self.balance =  balance
        self.amount = amount

    def print_balance(self):
        current_balance = self.balance
        print(f"Your balance is: ${current_balance}")    

    def deposit_money(self):
        new_deposit = 0
        print(f"You made a deposit of: ${self.amount}")
        new_deposit = self.balance + self.amount
        print(f"Your new balance is: ${new_deposit}")

    def withdraw_money(self):
        print(f"You withdraw: ${self.amount}")
        withdrawn_amount = self.balance - self.amount
        if withdrawn_amount <= 0:
            print(f"You don't have enough funds to withdraw money from your savings accont ")
        else:    
            print(f"Your new balance after withdrawing money is: ${withdrawn_amount}")




class Savings_Account(Bank_Account):
    balance : int 
    amount : int

    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount

    def withdraw_money(self):
        return super().withdraw_money()  #?

        



my_bank_account = Bank_Account(1000, 500)
#my_bank_account.print_balance()
#my_bank_account.deposit_money()
#my_bank_account.withdraw_money()

my_savings = Savings_Account(1000, 5000)
#my_savings.print_balance()
#my_savings.withdraw_money()