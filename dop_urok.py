# # # функция
# # def div(num1:int, num2:int):
# #     print(num1 / num2)
# # div(10,4)

# def add(num1:int=10, num2:int=20):
#     print(num1 + num2)
# add(20,5)

# def mult(num1:int=5, num2:int=5) -> int :
#     "функция для умножение чисел python"
#     print(num1 *num2)
# mult()


# оператор return
# def welcom(name:str='nurbolot') -> str:
#     return "welcome" + name
# print('welcome', ("jakshylik"))
# print(welcom())


def calculator(num1:int= 1, num2:int=1, operator:str='+')-> int:
    if operator == "+":
        return num1 +num2
    elif operator == "-":
        return num1-num2
    elif operator =='*':
        return num1*num2
    elif operator == '/':
        return num1 /num2
    else :
        return"такого оператра нету"
print(calculator(30,25,'-'))

print("hello git hub")