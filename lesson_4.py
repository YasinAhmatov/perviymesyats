# списки -list
# 4 str, int, float, bool, list

# name1 = "kurmanbek"
# name2 = "syimyk"
# name3 = "beksultan"
# name4 = "nurbolot"
# print(name1, name2, name3, name4)


names = ["kumanbek", "siymyk", "beksultan", "nurbolot"]
print(names)
list = [10, 0,1, "geeks" ,False]
print(list)


# it = ["Google", "Amazon", "MAd Devs"]
# print(it)
# it.append("geeks studio") #метод append добавляет в конец списка значение
# print(it)
# it.append("apple")
# print(it)
# it.remove("Amazon") #метод remove удаляет значение из списка
# print(it)
# # it.remove("bayas")#если значение которую нужно удалит в списке нету,то выводится ошибка
# # print(it)
cars = ["bmw", "tesla", "byd","mers"]
# print(cars)
print(cars[1][4])
# print(cars[0:4])#в списках можно использовать срезы и индексы
# cars[2] = "zeekr"#обновление значение из списка с помощью индексов
# print(cars)
# cars.pop(2)#метод pop удаляет из списка по индексу
# print(cars)


# numbers = [101, 202, 303, 708, 1992]
# print(numbers)
# numbers.insert (0, "bayas")#метод insert добавляет значение по индексу
# print(numbers)
# del numbers[0] #оператор del удаляет значение по индексу и срезу
# print(numbers)

# nums = [354,854,394,104,75,45,3]
# nums.sort(reverse=True)#метод sort сортитирует данные внутри списка
# print(nums)

# lst = ["geeks", "hello", "world", "abc","bayas"]
# lst.sort()
# print(lst)


#tuple -кортежы
numbers = ("asus", "lenovo","apple","hp","acer")
# #ТИП ДАННЫХ TUPLE (КОРТЕЖЫ) ОБОЗНАЧАЮТСЯ В КРУГЛЫХ СКОБКАХ И ЯВЛЯЮТСЯ НЕИЗМЕННЕНЫМИ
# print(numbers)
# print(numbers.count('acer'))
print(numbers.index('acer'))
# print(numbers[2])
# print(numbers[::-1])
# tup = (10, 3.0, "hello", True)
# print(tup)

# students = ["nurbolot", "bayastan","Syimyk","beksultan", "janysh"]
# name = input("Имя: ").title()
# if name in students:
#     print(name, "есть в спискпе")
# else:
#     print("К сожелению такого студента нету в списке")


# import random
# random_number  = random.randint(1,3)
# user_number = int(input("введите число: 2"))
# if random_number == user_number:
#     print("ПОБЕДА")
# else: 
#     print("ВЫ ПРОИГРАЛИ!!!")
