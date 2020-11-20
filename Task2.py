# Task2--Week6----> ATABEK
# 1)

# class Student:
#     def __init__(self, name, lastname, department, year_of_intrance):
#         self.name = name
#         self.lastname = lastname
#         self.department = department
#         self.year_of_intrance = year_of_intrance

#     def get_student_info(self):
#         print(f'{self.name} {self.lastname} поступил в {self.year_of_intrance} г. на факультет: {self.department}')

# my_student = Student('Вася', 'Иванов', 'Программирование.', '2017')
# my_student.get_student_info()

# 2)
# class BankAccount:
    
#     def __init__(self):
#         self.balance = 0

#     def withdraw(self, amount):
#         amount = int (input("How much you money you wanna put your card? : "))
#         if self.balance > amount:
#             print(f'Your current balance is {self.balance - amount}')

#         else:
#             print("You don't have enough money")



#     def deposit(self, amount):
#         amount = int(input("How much you want to deposit : "))
#         print(f'Your current balance is {self.balance + amount}')


# account = BankAccount()
# account.deposit(int)

# 3)
# class Airplane:

#      def __init__(self,mark,model,year,max_speed):
#          self.mark = mark
#          self.model = model
#          self.year = year
#          self.max_speed = max_speed
#          self.odometer = 0
#          self.is_flying = False

#      def take_off(self):
#         self.is_flying = True
#         about_off = f"{self.mark} {self.model} was take off."
#         return about_off

#      def fly(self, km):
#         self.odometer += km
#         about_to_fly = f"{self.mark}f lew {self.odometer}km during the flying {self.max_speed} km/h."
#         return about_to_fly

#      def land(self):
#             self.is_flying = False
#             about_land = f"{self.mark} landed, the odometer shows {self.odometer}km."
#             return about_land

# start = Airplane("Turkish Airlines","342-545","1995",675)
# print(start.take_off())
# print(start.fly(100))
# print(start.land())














