import calendar

print("Добро пожаловать в календарь \n")

# a = input("Something: ")

year = int(input("Enter Пожалуйста, введите год: "))
month = int(input("Пожалуйста номер любого месяц: "))

print(calendar.month(year, month))

print("Всего хорошего!")
