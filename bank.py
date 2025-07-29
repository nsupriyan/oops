from abc import ABC,abstractmethod

class bank(ABC):
    def __init__(self):
        self.balance=20000
        pass
    @abstractmethod
    def deposite(self):
        pass
    @abstractmethod    
    def withdraw(self):
        pass 

class union(bank):
    def deposite(self):
        deposite=int(input('enter the amount to deposite: '))
        self.balance += deposite
        print(f'Updated Balance after deposite: {self.balance}')
    def withdraw(self):
        withdraw_amount = int(input('Enter the amount to withdraw: '))
        if withdraw_amount > self.balance:
            print('Insufficient funds.')
        else:
            self.balance -= withdraw_amount
            print(f'Updated Balance after withdrawal: {self.balance}')

obj=union()
obj.deposite()
print('---------------')
obj.withdraw()