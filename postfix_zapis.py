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