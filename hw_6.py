# def chatbot():
#     while True:
#         text = input("Введите что то: ")
#         if text.find("?")>=0:
#             print("Конечно!")
#         elif text.find("ВОТ ТАК!")>=0:
#             print("Успокойся")
#         elif text == "":
#             print("Как классно, когда ты молчишь. Продолжай в том же духе!")
#         else:
#             print("Ну и что")
# chatbot()

# # 2
# def words(sentence):
#     words = sentence.lower().split()
#     word_counts = {}
#     for word in words:
#         if word in word_counts:
#             word_counts[word] += 1
#         else:
#             word_counts[word] = 1
#     return word_counts
# sentence = """Money, money, money, it’s always sunny, in
# the richmen’s world”"""
# word_counts = words(sentence)
# print(word_counts)

# 3
# n = 27
# reversed_n = str(n)[::-1]
# result = int(reversed_n)
# print(reversed_n)


# ДП

# Задача 1
# set1 = {23, 56, 45, 89, 231, 456}
# set2 = {85, 57, 987, 789, 326, 256}
# set3 = set1.union(set2)
# print(set3)

#Задача 2
# fruits = {"клубника","яблоко", "банан", "виноград", "арбуз"}
# if "яблоко" in fruits:
#     print("В множестве есть яблоко!")
# else:
#     print("Яблоко не найдено!")

#Задача 3
even_numbers = set(range(2, 21, 2))
divisible_by_three = set(range(3, 31, 3))
set1 = even_numbers.intersection(divisible_by_three)
print(set1)


