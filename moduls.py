# модули
# 1 - импортировать сам модуль 
import lesson_8 #без окончание py


lesson_8.welcome('Bayastan')#вызываем функцию welcome из модуля lesson_8
lesson_8.add(100,34)

# 2 импортировать отдельные определение из модуля

from lesson_8 import welcome, add

welcome('Beksultan')
add(200,1234)

# 3-импортировать все содержимое сразу
from lesson_8 import *

welcome("nurbolot")
add(333,4344)