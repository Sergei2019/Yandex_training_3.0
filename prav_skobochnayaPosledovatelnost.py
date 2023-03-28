lt = [s for s in input()]

def is_correct_bracket_seq(lst):
    if lst is None or len(lst) == 0:
        return 'yes'
    if lst[-1] == '[' or lst[-1] == '{' or lst[-1] == '(':
        return 'no'
    if lst[0] == ']' or lst[0] == '}' or lst[0] == ')':
        return 'no'
    stack = []
    for i in range(len(lst), 0, -1):
        if lst[i-1] == ')' or lst[i-1] == ']' or lst[i-1] == '}':
            stack.append(lst[i-1])
        if lst[i-1] == '(':
            if len(stack) == 0 or stack[-1] != ')':
                return 'no'
            else:
                lst.pop()
                stack.pop()
        if lst[i-1] == '[':
            if len(stack) == 0 or stack[-1] != ']':
                return 'no'
            else:
                lst.pop()
                stack.pop()
        if lst[i-1] == '{':
            if len(stack) == 0 or stack[-1] != '}':
                return 'no'
            else:
                lst.pop()
                stack.pop()
    if len(stack) == 0:
        return 'yes'
    return 'no'       
    
print(is_correct_bracket_seq(lt))