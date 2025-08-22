def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    for problem in problems:
        seperate = problem.split(' ')
        operator = seperate[1]
        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."
        left, operator, right = seperate
        if not (left.isdigit() and right.isdigit()):
            return 'Error: Numbers must only contain digits.'
        if len(left) > 4 or len(right) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        value_one = int(seperate[0])
        value_two = int(seperate[2])
        if seperate[1] == '+':
            result = value_one + value_two

        else:
            result = value_one - value_two

    return problems


print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')