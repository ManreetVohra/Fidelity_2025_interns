#Create a class "Customer" with data members: name,balance and methods: deposit,withdraw

class Customer:
    """This is a class demonstrating a bank customer having name and a certain balance in his account with the 
    functions he can perform like withdrawing and depositing money"""
    def __init__(self,name):
        """This is a constructor that initialises the account balance of a customer with zero"""
        self.name=name
        self.__balance=0 #private attribute
    def deposit(self,money):
        """This method is used to deposit money to the customer's account"""
        self.__balance+=money
        print("Your bank balance is now Rs.",self.__balance)
    def withdraw(self,money):
        """This method is used to withdraw money from the bank account if the withdrawal money is greater than or 
        equal to the balance"""
        if(self.__balance>=money):
            self.__balance-=money
            print("Your bank balance is now Rs.",self.__balance)
        else:
            print("Your account does not have sufficient balance")
    

c1=Customer("Manreet")
c1.deposit(1000)
c1.withdraw(500)
c1.withdraw(1000)