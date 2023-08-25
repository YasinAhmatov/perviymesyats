# 1
# password = input("Password: ")
# if password  == "geek":
#     print("Password is correct. You are welcome")
# else:
#     print("password is incorrect.Please try again")



2
operator = int(input("Введите температуру: "))
if operator <= -30:
   print("Там холодно лучше сидет дома: ")
elif operator <0 and operator >-30:
    print("Холодновато. Оденься потеплее!")
elif operator >= 0 and operator<15:
    print("Прохладно. Куртку накинь!")
elif  operator >= 15 and operator<30:
    print("Тепло.Иди погуляй в парке!")
elif operator >= 30 and operator<50:
    print("Ого, жарко!")
elif operator >=50 and operator <100:
    print("Там такая жара, лучше сиди дома!")
else:
    print("Ошибка")


# # 3 
# hour = int(input("Введите текущий час (от 0 до 23): "))
# if 0 <= hour < 7:
#     print("Ночь (0 - 6)")
# elif 7 <= hour < 13:
#     print("Утро (7 - 12)")
# elif 13 <= hour < 19:
#     print("День (13 - 18)")
# else:
#     print("Вечер (18 - 23)")



# Доп задание

# grade = int(input("Введите оценку студента (от 0 до 100): "))

# if grade >= 90:
#     print("Отлично")
# elif 80 <= grade < 90:
#     print("Хорошо")
# elif 70 <= grade < 80:
#     print("Удовлетворительно")
# elif 60 <= grade < 70:
#     print("Неудовлетворительно")
# else:
#     print("Студент должен пересдать экзамен")