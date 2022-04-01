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
            print('Error: Numbers must only contain digits.')
            quit()
        if data[1] == '+':
            ans = ' '
            if dis is True:
                ans = num1 + num2
            solution.append('    {}\n+    {}\n------\n   {}'.format(num1, num2, ans))
            continue
        if data[1] == '-':
            ans = ' '
            if dis is True:
                ans = num1 - num2
            solution.append('    {}\n+    {}\n------\n   {}'.format(num1, num2, ans))
            continue
        else:
            print("'Error: Operator must be '+' or '-'.")
    if len(solution) > 4:
        print('Error: Too many problems')
    print(solution)

arithmetic_arranger(['32 + 8', '32 - 8'], True)
