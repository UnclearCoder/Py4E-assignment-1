def arithmetic_arranger(inp, dis):
    solution = []
    for ctx in inp:
        data = []
        raw = ctx.split()
        for obj in raw:
            try:
                obj = int(obj)
                data.append(obj)
            except:
                data.append(obj)
        # Check for integers
        if type(data[0]) != int or type(data[2]) != int:
            print('Error: Numbers must only contain digits.')
            quit()
        num1 = data[0]
        num2 = data[2]
        if len(str(num1)) > 4 or len(str(num2)) > 4:
            print('Error: Numbers cannot be more than four digits.')
            quit()
        # Solving the equation
        if data[1] == '+':
            if dis is True:
                ans = num1 + num2
                data.append('------')
                data.append(ans)
                solution.append(data)
                continue
            else:
                data.append('------')
                data.append(' ')
                solution.append(data)
        if data[1] == '-':
            if dis is True:
                ans = num1 - num2
                data.append('------')
                data.append(ans)
                solution.append(data)
                continue
            else:
                data.append('------')
                data.append(' ')
                solution.append(data)
        else:
            print("'Error: Operator must be '+' or '-'.")
            quit()
    if len(solution) > 4:
        print('Error: Too many problems')
        quit()
    # expancion of the list for better reformat
    while len(solution) < 4:
        add = [' ', ' ', ' ', ' ', ' ']
        solution.append(add)
    # Formating of the answer
    print(solution, '\n')
    test = (f'{solution[0][0]:>7}{solution[1][0]:>7}{solution[2][0]:>7}{solution[3][0]:>7}\n'
            f'{solution[0][1]:>2}{solution[0][2]:>5}{solution[1][1]:>2}{solution[1][2]:>5}{solution[2][1]:>2}{solution[2][2]:>5}{solution[3][1]:>2}{solution[3][2]:>5}\n'
            f'{solution[0][3]:>7}{solution[1][3]:>7}{solution[2][3]:>7}{solution[3][3]:>7}\n'
            f'{solution[0][4]:>7}{solution[1][4]:>7}{solution[2][4]:>7}{solution[3][4]:>7}'
            )
    return test


answer = arithmetic_arranger(["32 + 698", "3801 - 2", "4500 - 43"], True)

print(answer)
