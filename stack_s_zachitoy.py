"""Научитесь пользоваться стандартной структурой данных stack для целых чисел.
Напишите программу, содержащую описание стека и моделирующую работу стека, реализовав все указанные здесь методы.
Программа считывает последовательность команд и в зависимости от команды выполняет ту или иную операцию.
После выполнения каждой команды программа должна вывести одну строчку. Возможные команды для программы:

push n
Добавить в стек число n (значение n задается после команды). Программа должна вывести ok.

pop
Удалить из стека последний элемент. Программа должна вывести его значение.

back
Программа должна вывести значение последнего элемента, не удаляя его из стека.

size
Программа должна вывести количество элементов в стеке.

clear
Программа должна очистить стек и вывести ok.

exit
Программа должна вывести bye и завершить работу.

Перед исполнением операций back и pop программа должна проверять, содержится ли в стеке хотя бы один элемент. Если во входных данных встречается операция back или pop, и при этом стек пуст, то программа должна вместо числового значения вывести строку error.

Формат ввода
Вводятся команды управления стеком, по одной на строке

Формат вывода
Программа должна вывести протокол работы стека, по одному сообщению на строке
"""
def push(items, item):
    items.append(item)

def pop(items):
    items.pop()

def back(items):
    return items[-1]

def size(items):
    return len(items)

def clear(items):
    items.clear()
  
def exit():
    return 'bye'


res = []
stack = []

while True:
    command = input()
    if command == "size":
        res.append(size(stack))
    elif command == "back":
        if len(stack) == 0:
            res.append('error')
        else:  
            res.append(back(stack))
    elif command == "pop":
        if len(stack) == 0:
            res.append('error')
        else:  
            res.append(stack[-1])
            pop(stack)
    elif command == "clear":
        clear(stack)
        res.append("ok")
    elif "push" in command:
        i = command.split(' ')[-1]
        push(stack, i)
        res.append('ok')
    elif command == "exit":
        res.append("bye")
        break
print(*res,sep='\n')

