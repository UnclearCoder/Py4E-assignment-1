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
        if type(data[0]) != int or type(data[2]) != int:
            print('Error: Numbers must only contain digits.')
            quit()
        num1 = data[0]
        num2 = data[2]
        if len(str(num1)) > 4 or len(str(num2)) > 4:
            print('Error: Numbers cannot be more than four digits.')
            quit()
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
    while len(solution) < 4:
        test = [' ', ' ', ' ', ' ', ' ']
        solution.append(test)
    return solution


solution = arithmetic_arranger(["32 + 698", "3801 - 2", "4500 - 43"], True)
print(solution[0][2])