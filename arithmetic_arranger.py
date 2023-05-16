def arithmetic_arranger(problems, show_answer=False):
    arranged_problems = ""
    # check if there are more than 5 problems
    if len(problems) > 5:
        return "Error: Too many problems."
    
    # split the problems into parts
    for i in range(len(problems)):
        problems[i] = problems[i].split()


    for problem in problems:
        # check if there are 3 parts in the problem
        if len(problem) != 3:
            return "Error: Problem must contain two numbers and an operator."
        # check if the operator is + or -
        if problem[1] not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        # check if the numbers are digits
        if not problem[0].isdigit() or not problem[2].isdigit():
            return "Error: Numbers must only contain digits."
        # check if the numbers are less than 4 digits
        if len(problem[0]) > 4 or len(problem[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        # preform the operation and store the result
        if problem[1] == "+":
            problem.append(str(int(problem[0]) + int(problem[2])))
        else:
            problem.append(str(int(problem[0]) - int(problem[2])))

    # structure the problems
    first_line = ""
    second_line = ""
    third_line = ""
    fourth_line = ""

    for problem in problems:
        # find the longest number
        if len(problem[0]) > len(problem[2]):
            longest = len(problem[0])
        else:
            longest = len(problem[2])
        # add the first line
        first_line += " " * (longest - len(problem[0]) + 2) + problem[0] + "    "
        # add the second line
        second_line += problem[1] + " " * (longest - len(problem[2]) + 1) + problem[2] + "    "
        # add the third line
        third_line += "-" * (longest + 2) + "    "
        # add the fourth line
        fourth_line += " " * (longest - len(problem[3]) + 2) + problem[3] + "    "
        

    # remove the extra spaces
    first_line = first_line.rstrip()
    second_line = second_line.rstrip()
    third_line = third_line.rstrip()
    fourth_line = fourth_line.rstrip()

    # combine the lines
    arithmetic_arranger = first_line + "\n" + second_line + "\n" + third_line
    if show_answer:
        arithmetic_arranger += "\n" + fourth_line
    else:
        arithmetic_arranger += ""
    
        

    return arithmetic_arranger

if __name__ == "__main__":
    print(arithmetic_arranger(["3801 - 2", "123 + 49"]) == '  3801      123\n-    2    +  49\n------    -----')
    print('  3801      123\n-    2    +  49\n------    -----')
    print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
