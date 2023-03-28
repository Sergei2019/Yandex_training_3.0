"""
В постфиксной записи (или обратной польской записи) операция записывается после двух операндов.
Например, сумма двух чисел A и B записывается как A B +.
Запись B C + D * обозначает привычное нам (B + C) * D, а запись A B C + D * + означает A + (B + C) * D.
Достоинство постфиксной записи в том,
что она не требует скобок и дополнительных соглашений о приоритете операторов для своего чтения.

8 9 + 1 7 - *
-102

"""

p = input().split(' ')
stack = []
for el in p:
    if el =='*':
        a = int(stack.pop())
        b = int(stack.pop())
        stack.append(a*b)
    elif el =='+':
        a = int(stack.pop())
        b = int(stack.pop())
        stack.append(a+b)
    elif el =='-':
        a = int(stack.pop())
        b = int(stack.pop())
        stack.append(b-a)
    else:
        stack.append(el)
print(stack.pop())