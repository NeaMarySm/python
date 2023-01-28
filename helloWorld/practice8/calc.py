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


def count_simple_expression(expression_list):
    result = int(expression_list[0])
    for i in range(1, len(expression_list)-1, 2):
        result = calc(result, int(expression_list[i+1]), expression_list[i])
    return result


def parse_to_simple(expression_list):
    new_list = [int(expression_list[0])]
    for i in range(1, len(expression_list)-1, 2):
        if expression_list[i] == '*' or expression_list[i] == '/':
            last_index = len(new_list)-1
            item = calc(new_list[last_index],
                        int(expression_list[i+1]), expression_list[i])
            new_list.append(item)
            new_list.pop(last_index)
        else:
            new_list.append(expression_list[i])
            new_list.append(int(expression_list[i+1]))
    return new_list


def parse_expression_with_brackets(expr_list):
    new_list = []
    temp = []
    i = 0
    while i < len(expr_list):
        if expr_list[i] != '(':
            new_list.append(expr_list[i])
            i += 1
        else:
            while expr_list[i] != ')':
                i += 1
                temp.append(expr_list[i])
            new_list.append(count_simple_expression(temp))
            temp = []
    for item in new_list:
        if item == ')' or item == '(':
            new_list.remove(item)
    return new_list


def count_all(expression):
    expr_list = expression.split()
    print(expr_list)
    no_brackets = parse_expression_with_brackets(expr_list)
    simple_expression = parse_to_simple(no_brackets)
    result = count_simple_expression(simple_expression)
    return result


n = '14 + 3 * 6 * 8 - 9'
m = '8 * 3 / 6 - 8 * 2 - 6'
br = '8 + 3 / ( 6 - 8 ) * ( 2 - 6 )'

print(count_all(br))
print(count_all(n))
print(count_all(m))
