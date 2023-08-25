# # работа с файламиf
# f = open('geeks.txt', 'w')
# f.write("hello world and geeks it courses!")
# f.close()

# read_txt_file = open('geeks.txt', 'r')
# print(read_txt_file.read())
# read_txt_file.close()

# read_python_code_file = open('lesson_7.py', 'r', encoding='utf-8')
# print(read_python_code_file.read())
# # read_python_code_file.close

# text = """Образовательный центр Geeks (Гикс) был основан Fullstack-разработчиком Айдаром Бакировым и Android-разработчиком Нургазы Сулаймановым в 2018-ом году в Бишкеке с целью дать возможность каждому человеку, даже без опыта в технологиях, гарантированно освоить IT-профессию."""
# about = open('about.txt', 'w', encoding='utf-8')
# about.write(text)
# about.close()

# read_text = open('about.txt','r', encoding='utf-8')
# print(read_text.read())
# read_text.close()

# car_txt = open('cars.txt','w',encoding='utf-8')
# car_txt.write('tesla\n')
# car_txt.write('acura\n')
# car_txt.write('zeekr\n')
# car_txt.close()

# new_car_txt = open('cars.txt', 'a+', encoding='utf-8')
# new_car_txt.write('jetour\n')
# new_car_txt.close()

# with open('courses.txt', 'w', encoding='utf-8') as courses:
#     courses.write('geeks\n')
#     courses.write('mad devs\n')

# with open('courses.txt', 'r') as read_courses:
#     print(read_courses.read())

# with open('hello.py', 'w', encoding='utf_8') as py:
#         py.write("print('hello world')")


# # with open('lesson_8.py', 'a', encoding='utf-8') as lesson:
# #     lesson.write('name =  "nurbolot"\n ')
# #     lesson.write('print ("name")\n')


# def welcome(name:str):
#     print("здравствуйте", name)

# def add(number1, number2):
#     print(number1+number2)