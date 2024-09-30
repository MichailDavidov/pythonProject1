from typing import MutableSet

immutable_var = 234, 'Urban', False
print('Immutable tuple: ', immutable_var)
#immutable_var[0] = 678 - будет ошибкой, т.к. кортеж является неизменяемым объектом, а значит элементы, хранящиеся в нём не могут быть изменены
mutable_list = [256, True, 'False']
mutable_list [1] = False
mutable_list.append('Modified')
mutable_list.extend('2345')
print('Mutable list: ', mutable_list)