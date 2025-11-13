class BankAccount:
    def __init__(self, account_number, customer_name, balance=0):
        self.__account_number = account_number
        self.__customer_name = customer_name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Yaroqsiz summa!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Yetarli mablag‘ yo‘q yoki noto‘g‘ri summa!")

    def get_balance(self):
        return self.__balance


class PremiumAccount(BankAccount):
    def __init__(self, account_number, customer_name, balance=0, discount_rate=0.02):
        super().__init__(account_number, customer_name, balance)
        self.discount_rate = discount_rate

    def get_discounted_balance(self):
        return self.get_balance() * (1 - self.discount_rate)
