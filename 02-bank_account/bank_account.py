#1 Create a bank account class 
class BankAccount: 

    interest_rate = .01 #2 Add a class variable called interest-rate
    accounts = [] #3 class variable called accounts that starts as an empty string 

    def __init__(self, balance = 0): #constructor instance method with default balance of 0 
        self.balance = balance 

    def deposit(self, amount): #deposit instance method 
        self.balance += amount
        return self.balance

    def withdraw (self, amount):
        self.balance -= amount
        return self.balance 

    @classmethod #add a classmethod called create that makes a new instance using BankAccount()and adds new object to the accounts class variable. 
    def create(cls): 
        new_account = BankAccount() #new acccount is an instance of bank account 
        cls.accounts.append(new_account) #add the new account to the accounts list 
        return new_account

    @classmethod # classmethod that returns the sum of all balances across all accounts in the accounts class variable.
    def total_funds(cls): 
        total = 0
        print('\t Total Funds \t')
        for account in cls.accounts: 
            total += account.balance
        return total 
    
    @classmethod #interest_time that iterates through all accounts and increases their balances according to the class interest_rate
    def interest_time(cls): 
        print ('\n \t Total with Interest\t \n')
        for account in cls.accounts:
            account.balance += account.balance * cls.interest_rate #the account balance calculated in the deposit and withdraw class methods
        return cls.accounts 



my_account = BankAccount.create()
your_account = BankAccount.create()
print(f'Your balance is: {my_account.balance}\n') # 0

my_account.deposit(200)
your_account.deposit(1000)
print(f'{my_account.balance} was deposited\n') # 200
print(f'{your_account.balance} was deposited\n') # 1000
print(BankAccount.total_funds()) # 1200
BankAccount.interest_time()
print(my_account.balance) # 202.0 
print(your_account.balance) # 1010.0
print(BankAccount.total_funds()) # 1212.0
my_account.withdraw(50)
print(my_account.balance) # 152.0
print(BankAccount.total_funds()) # 1162.0



