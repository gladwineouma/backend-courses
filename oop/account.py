class Account:
    def __init__(self,name):
        self.name = name
        self._balance = 0  #underscore signifies a private fro one to change a an object that is private u create a new method
        self.deposits = []
        self.withdrawal = []
        self.loan = []
        self.is_frozen = True
        self.minimum_balance = 200
        self.transaction = []

    def get_deposit(self,amount):
        self.deposits.append(amount)
        if amount >= 1:
            self.balance += amount            
        
            return f"Hello {self.name} you have received amount {amount} your new balance is {self.balance}"
        else:
            return f"Deposit amount must be positive"        


    def get_withdrawal(self,amount):
        if amount > 0 and self.balance >=amount and self.minimum_balance == 200:
            self.withdrawal.append(amount)
            self.balance -= amount
            return f"Hello {self.name} you have withdrawn Kshs {amount} your new balance is Kshs{self.balance}"

        elif amount <= 0:
            return f"Withdrwable amount must be positive"

        else:
            return f"{amount} not withrawable your account balance is {self.balance} and your minimum account balance is {self.minimum_balance}"

    def transfer(self,amount,name):
        self.amount = amount
        self.name = name
        # if amount transaction fee/balance/withdraw/deposit
        # add repayment on the class
        # deposit extra amount
        # Add encapsulation(balance,loan limit)
        # find out encapsulation as a convention but not forced rule

    def set_balance(self,amount):  #Applicable only when an attribute is private.
        self._balance = amount

    def get_balance(self):
        balance = sum(self.deposits) - sum(self.withdrawal)
        return f"Your account balance is {balance}"


    def loan_limit(self):
        deposit_history = sum(self.deposit)
        return deposit_history//3

    def request_loan(self,amount):
        if amount > self.loan_limit():
            return 


    def request_loan(self,amount):
        loan_amount = self.balance*3      
        if amount <= loan_amount:
            self.balance +=amount
            self.loan.append(amount)
            return f"You loan request of {amount} has been approved and your balance is {self.balance}"
        else:
            return f"Your loan limit is {loan_amount}"

    
    def repay_loan(self,amount):
        total_loan = sum(self.loan)
        outstanding_balance = total_loan - amount
        
        if amount >= total_loan:
            self.loan.append(amount)
            self.balance -=amount
            return f"Your loan is fully settled "
        
        else:        
            return f"Your outstanding balance is {outstanding_balance}"


    def view_account_details(self):        
        return (f"Account Holder: {self.name} your balance is {self.balance} your outstanding loan is {self.loan}")

    
    def change_account_owner(self,new_name):
        self.name = new_name 
        return f"{new_name} you are now the new account"


    def account_statement(self):
        print (f"{self.name} your account balance is {self.balance}") 
        for deposit in self.deposits:
            print(f"Debits: {deposit}")

        for withdrawal in self.withdrawal:
            print(f"Credits: {withdrawal}")

        

    def interest_calculation(self,amount):
        interest = amount * 0.5
        payable_amount = interest + amount
        return f"If you take a loan of {amount} your interst will be {interest} and your total payable amount is {payable_amount}"

    

    def freeze(self):
        if self.is_frozen == True:
            return f"Your account is frozen cannot perform any transaction due to security reasons"
        elif self.is_frozen != True:
            return f"Your account is not frozen"   


    def close_account(self,name):
        self.name = name
        self.balance = 0
        self.deposits = []
        self.withdrawal = []
        self.loan = []        
        return f"Hi {self.name}, Your account is closed"

        




        
       

   
         

        











