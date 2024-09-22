def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_line = ''
    second_line = ''
    dashes_line = ''
    answers_line = ''

    for i, problem in enumerate(problems):
        parts = problem.split()

        if parts[1] not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        if not (parts[0].isdigit() and parts[2].isdigit()):
            return 'Error: Numbers must only contain digits.'
        
        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        width = max(len(parts[0]), len(parts[2])) + 2

        top = parts[0].rjust(width)
        bottom = parts[1] + parts[2].rjust(width - 1)
        dashes = '-' * width

        if show_answers:
            if parts[1] == '+':
                answer = str(int(parts[0]) + int(parts[2])).rjust(width)
            else:
                answer = str(int(parts[0]) - int(parts[2])).rjust(width)

        if i > 0:
            first_line += '    '
            second_line += '    '
            dashes_line += '    '
            if show_answers:
                answers_line += '    '

        first_line += top
        second_line += bottom
        dashes_line += dashes
        if show_answers:
            answers_line += answer

    if show_answers:
        problems = f"{first_line}\n{second_line}\n{dashes_line}\n{answers_line}"
    else:
        problems = f"{first_line}\n{second_line}\n{dashes_line}"

    return problems

print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["1 + 2", "1 - 9380"])}')
print(f'\n{arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])}')
print(f'\n{arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])}')
print(f'\n{arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["3 + 855", "988 + 40"], True)}')
print(f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')