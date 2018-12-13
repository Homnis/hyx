class Account:
    id = 0
    personId = "123456"
    __balance = 0.0

    def __init__(self, id, password, name, personId, email, balance):
        self._id = id
        self.__password = password
        self.name = name
        self.__personId = personId
        self.email = email
        self.__balance = balance

    def setMoney(self, balance):
        self.__balance = balance

    def getMoney(self):
        return self.__balance

    def setPsw(self, psw):
        self.__password = psw

    def getPsw(self):
        return self.__password

    def setPersonId(self, id):
        self.__personId = id

    def getPersonId(self):
        return self.__personId

    def deposit(self, money):
        if money >= 0:
            self.setMoney(self.getMoney() + money)
        else:
            print("something wrong happened")

    def withdraw(self, money):
        # if money >= 0:
        #     if self.__balance - money >= 0:
        #         self.__balance -= money
        #     else:
        #         print("something wrong happened")
        # else:
        #     print("something wrong happened")
        pass


class SavingAccount(Account):

    def __init__(self, id, password, name, personId, email, balance):
        super().__init__(id, password, name, personId, email, balance)

    def withdraw(self, money):
        if money >= 0:
            if self.getMoney() - money >= 0:
                self.setMoney(self.getMoney() - money)
            else:
                print("something wrong happened")
        else:
            print("something wrong happened")


class CreditAccount(Account):

    def __init__(self, id, password, name, personId, email, balance, ceiling):
        super().__init__(id, password, name, personId, email, balance)
        self.__ceiling = ceiling

    def setCeiling(self, ceiling):
        self.__ceiling = ceiling

    def getCeiling(self):
        return self.__ceiling

    def withdraw(self, money):
        if self.getMoney() + self.getCeiling() >= money:
            if self.getMoney() >= money:
                self.setMoney(self.getMoney() - money)
            else:
                x = money - self.getMoney()
                self.setMoney(0)
                self.setCeiling(self.getCeiling() - x)
        else:
            print("something wrong happened")


class Bank:
    list1 = []

    def __init__(self, list1, num):
        self.list1 = list1
        self.num = num

    def getList(self):
        return self.list1

    def addAccount(self):  # 不让用appened
        self.getList().append("111")


a = CreditAccount(123456, "123456", "hyx", 410702, "email@email.com", 5000, 1000)
a1 = CreditAccount(1234567, "1234567", "hyx1", 4107021, "email1@email.com", 5000, 1000)
list1=[a,a1]
b=Bank(list1,2)
print(b.getList())
b.addAccount()
print(b.getList())
# a.withdraw(5500)
# print(a.getCeiling())
