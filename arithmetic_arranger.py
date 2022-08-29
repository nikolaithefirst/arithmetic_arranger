def arithmetic_arranger(calculations, results=None):
    digits = '0123456789'
    first_string, second_string, prep, result = str(), str(), str(), str()
    if len(calculations) > 5: return "Error: Too many problems."
    for i in range(len(calculations)):
        numbers = calculations[i].split()
        for digit in numbers[0]:
          if digit not in digits:
            return "Error: Numbers must only contain digits."
        for digit in numbers[2]:
          if digit not in digits:
            return "Error: Numbers must only contain digits."
        if numbers[1] not in '+-': return 'Error: Operator must be \'+\' or \'-\'.'
        if len(numbers[0]) > 4 or len(numbers[2]) > 4: return "Error: Numbers cannot be more than four digits."
        
        if len(numbers[0]) >= len(numbers[2]):
            max_len = len(numbers[0])
        else:
            max_len = len(numbers[2])
          
        if i == len(calculations) - 1:
            first_string += ' ' * (max_len + 2 - len(numbers[0])) + numbers[0]
            prep += '--' + '-' * max_len


            if numbers[1] == '+':
                second_string += '+' + ' ' * (max_len + 1 - len(numbers[2])) + numbers[2]
                result += ' ' * (max_len + 2 - len(str(int(numbers[0]) + int(numbers[2])))) + str(int(numbers[0]) + int(numbers[2]))
            elif numbers[1] == '-':
                second_string += '-' + ' ' * (max_len + 1 - len(numbers[2])) + numbers[2]
                result += ' ' * (max_len + 2 - len(str(int(numbers[0]) - int(numbers[2])))) + str(int(numbers[0]) - int(numbers[2]))

        else:
            first_string += ' ' * (max_len + 2 - len(numbers[0])) + numbers[0] + '    '
            prep += '--' + '-' * max_len + '    '

            if numbers[1] == '+':
                second_string += '+' + ' ' * (max_len + 1 - len(numbers[2])) + numbers[2] + '    '
                result += ' ' * (max_len + 2 - len(str(int(numbers[0]) + int(numbers[2])))) + str(
                    int(numbers[0]) + int(numbers[2])) + '    '
            elif numbers[1] == '-':
                second_string += '-' + ' ' * (max_len + 1 - len(numbers[2])) + numbers[2] + '    '
                result += ' ' * (max_len + 2 - len(str(int(numbers[0]) - int(numbers[2])))) + str(
                    int(numbers[0]) - int(numbers[2])) + '    '

    if results == True:
        return first_string + '\n' + second_string + '\n' + prep + '\n' + result
    else:
        return first_string + '\n' + second_string + '\n' + prep
    
