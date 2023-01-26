n = '14 + 3 * 6 * 8 - 9'
m = '8 * 3 / 6 - 8 * 2 - 6'


def calc(a, b, operation):
    match operation:
        case '+':
            return a+b
        case '-':
            return a-b
        case '*':
            return a*b
        case '/':
            return a/b


def count_expression(expression):
    expr_list = expression.split()
    print(expr_list)
    new_list = [int(expr_list[0])]
    for i in range(1, len(expr_list)-1, 2):
        if expr_list[i] == '*' or expr_list[i] == '/':
            last_index = len(new_list)-1
            item = calc(new_list[last_index],
                        int(expr_list[i+1]), expr_list[i])
            new_list.append(item)
            new_list.pop(last_index)
        else:
            new_list.append(expr_list[i])
            new_list.append(int(expr_list[i+1]))
    result = int(new_list[0])
    for i in range(1, len(new_list)-1, 2):
        result = calc(result, new_list[i+1], new_list[i])
    return result


print(count_expression(n))
print(count_expression(m))
