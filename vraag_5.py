class Customer:
    def __init__(self,name,surname,tc_identification,phone):
       self.name=name
       self.surname=surname
       self.tc_identification=tc_identification
       self.phone=phone
    def display_information(self):
       return(f"Customer Information:\n"
              f"Name:{self.name}\n"
              f"Surname:{self.surname}\n"
              f"TR ID:{self.tc_identification}\n"
              f"Telephone Number:{self.phone}")
       
class Account(Customer):
   def __init__(self,customer,account_nummer,balance=0):
       super().__init__(customer.name, customer.surname,customer.tc_identification,customer.phone)
       self.account_nummer=account_nummer
       self.balance=balance
   
   def deposit(self,amount):
       if amount>0:
           self.balance += amount
           print(f"{amount}TL hesaba eklendi..\nGuncel Bakiye:{self.balance}TL")
       else:
           print("Gecersiz miktar...")

   def money_check(self,amount):
       if 0<amount<=self.balance:
           self.balance -= amount
           print(f"{amount}TL hesaptan cekildi..\nKalan Bakiye:{self.balance}TL")
       else:
            print(f"{amount}TL cekilemedi..Yetersiz bakiye...")

   def display_balance(self):
       print(f"Guncel Bakiye:{self.balance}TL")

musteri=Customer("Ahmet","Yilmaz","12345678","0555 555 5555")
account=Account(musteri,"Tr12345678")
print(account.display_information())
account.display_balance()
account.deposit(1000)
account.money_check(300)
account.money_check(800)
account.display_balance()