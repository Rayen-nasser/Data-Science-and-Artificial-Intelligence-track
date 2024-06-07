import datetime
from project_102.Person import Person

class AccountBank(Person):
    def __init__(self, fn, ln, email, balance):
        super().__init__(fn, ln, email)
        self.__balance = balance

    def increase_balance(self, amount):
        self.__balance += amount
        print("deposit has been made",amount, "in your bank balance at", datetime.datetime.now().strftime("%c"))


    def decrease_balance(self, amount):
        self.__balance -= amount
        print("ravil has been made", amount, "in your bank balance at", datetime.datetime.now().strftime("%c"))

    def get_balance(self):
        return self.__balance
    def get_info(self):
        return  super().get_info()+ ",\n" + f"balance: {self.get_balance()}"

# create account
account_khalid = AccountBank("khalid","ben walid", "kalid@gmail.com",50000)
print(account_khalid.get_info())

# decrease balance of khalid
account_khalid.decrease_balance(40000)
print(account_khalid.get_balance())

# increase balance of khalid
account_khalid.increase_balance(90000)
print(account_khalid.get_balance())
