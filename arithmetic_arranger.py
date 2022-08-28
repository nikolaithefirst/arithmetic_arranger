def arithmetic_arranger(calculations, results=None):
    first_string, second_string, prep, result = str(), str(), str(), str()
    for i in range(len(calculations)):

        numbers = calculations[i].split()

        if numbers[0] >= numbers[2]:
            max_len = len(numbers[0])
        else:
            max_len = len(numbers[2])

        first_string += ' ' * (max_len + 2 - len(numbers[0])) + numbers[0] + '    '
        prep += '--' + '-' * max_len + '    '


        if numbers[1] == '+':
            second_string += '+' + ' ' * (max_len + 1 - len(numbers[2])) + numbers[2] + '    '
            result += ' ' * (max_len + 2 - len(str(int(numbers[0]) + int(numbers[2])))) + str(int(numbers[0]) + int(numbers[2])) + '    '
        elif numbers[1] == '-':
            second_string += '-' + ' ' * (max_len + 1 - len(numbers[2])) + numbers[2] + '    '
            result += ' ' * (max_len + 2 - len(str(int(numbers[0]) - int(numbers[2])))) + str(int(numbers[0]) - int(numbers[2])) + '    '

    print(first_string)
    print(second_string)
    print(prep)

    if results == True:
        print(result)