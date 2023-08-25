# nums1 = [1,2,3,4,5] 
# nums2 = [3,4,5,6,7]
# nums3 = nums1+nums2
# print(set(nums3))
# names = {'nurbolot', 'kurmanbek', 'baystan', 'murat', 'nurbolot'}
# print(names)


# numbers = {10,20,30,40,50,60,70,70}
# print(numbers)


# cars = {'bmw', 'mers', 'tesla'}
# print(cars)
# cars.add("honda")
# print(cars)
# cars.add('bmw')
# print(cars)
# cars.remove('tesla')
# print(cars)
# cars.pop()
# print(cars)

# st = {1,2.0,False,"1"}
# print(st)


# frozenset

# frzn= frozenset({1,2,3,3,3,3,3,4,5,5,5,5})
# print(frzn)
# frzn.add(100)
# print(frzn)

# dictionari - словари
student = {'name':'Askhat', 'age':20}
print(student)
print(student['name'])
print(student['age'])
student.setdefault('language', 'python')#метод setfould добовляет в словарь ключ и значение
print(student)
student.pop('age')#метод pop,удаляет ключ из словаря и за одно значение 
print(student)
student['languge'] = 'javascript'#таким образом можно обновлять значение в словах python
print(student)

# tesla_model_x = {'brand':'tesla', 'model':'modelX', 'year':2023, 'color':'white'}
# print(tesla_model_x)
# print(tesla_model_x.keys())#Метод keys() возвращает специальную коллекцию ключей в словаре.
# print(tesla_model_x.items())#Метод items() возвращает пары «ключ — значение» в формате кортежей.
# print(tesla_model_x.values())#Метод values() возвращает специальную коллекцию значений в словаре.

# for key,values in tesla_model_x.items():
#     print(key,values)


# contact ={ 'mchs':'112', }
# while True:
#     command = input("1 - посмотреть, 2 - добавит, 3 - удалить , 4 - обновить: ")
#     if command == "1":
#         print(contact)
#     elif command == "2":
#         add_name = input("имя: ")
#         if add_name in contact.keys():
#             print("такой контакт уже существует")
#         else:
#             add_number = input("номер: ")
#             contact.setdefault(add_name,add_number)
#             print("контакты", add_name, "успешно добавлен")
#     elif command == "3":
#         delete_name = input("кого удалить: ")
#         contact.pop(delete_name)
#         print(delete_name, "успешно удален")
#     elif command =="4":
#         update_name = input("кого обновить: ")
#         nem_number = input("новый номер: ")
#         contact[update_name] = nem_number
#         print("контакт", update_name, "успешно обновлен")
#     else:
#         print("такой команды нету")