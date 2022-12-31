def check_is_string(input_str):
    if input_str.isalpha():
        if check_if_reserved(input_str):
            return False
        else:
            return True


def check_is_digit(input_str):
    if input_str.strip().isdigit():
        return True


def check_if_float1(i1, i2):
    if check_is_digit(i1) and check_is_digit(i2):
        return True


def check_if_float2(i1, i2, i3):
    if check_is_digit(i1) and check_is_digit(i2) and check_is_digit(i3):
        return True


def check_is_operator(input_str):
    operators = ['+', '-', '*', '=', '%', '/', '!', ':=', '<', '>']
    if input_str in operators:
        return True


def check_if_reserved(input_string):
    list1 = ['abstract', 'assert', 'boolean', 'break', 'byte', 'case', 'catch', 'char', 'class', 'const', 'continue',
             'default', 'double', 'do', 'else', 'enum', 'extends', 'false', 'final', 'finally', 'float', 'for', 'goto',
             'if', 'pow'
                   'implements', 'import', 'instanceof',
             'int', 'interface', 'long', 'native', 'new', 'null', 'package', 'private', 'protected', 'public', 'return',
             'short', 'static', 'strictfp',
             'super', 'switch', 'synchronized', 'this', 'throw', 'throws', 'transient', 'true', 'try', 'void',
             'volatile', 'while']
    if input_string in list1:
        return True
    else:
        return False


def check_if_symbol(input_str):
    if input_str == 'π':
        return float(3.14)
    elif input_str == 'e':
        return float(2.71)
    elif input_str == ' √2':
        return float(1.41)
    elif input_str == '√3':
        return float(1.73)
    elif input_str == 'δ' or input_str == 'a':
        return float(2.50)
    elif input_str == 'φ':
        return float(1.61)
    elif input_str == 'Ω':
        return float(0.56)


def lexical_Analyzer(input_string):
    global p
    operators = []
    identifiers = []
    numbers = []
    reserved_words = []
    list1 = []
    count = 0
    # here
    types_list = []
    #
    # if "pow" in input_string:
    #     list2 = input_string.split()
    #     for x in range(0, len(list2)):
    #         if check_is_string(list2[x]) and list2[x] != 'pow':
    #             if list2[x] in identifiers:
    #                 list1.append("id" + str(identifiers.index(list2[x]) + 1))
    #             else:
    #                 count += 1
    #                 list1.append(("id" + str(count)))
    #                 identifiers.append(list2[x])
    #         if check_is_operator(list2[x]):
    #             operators.append(list2[x])
    #             list1.append(list2[x])
    #         if check_is_digit(list2[x]):
    #             numbers.append(list2[x])
    #             list1.append(list2[x])
    #     for i in range(0, len(list1)):
    #         p = ""
    #         if list1[i] == '=':
    #             while i != len(list1) - 2:
    #                 i += 1
    #                 p += list1[i] + " "
    #         times = list1[len(list1) - 1]
    #         if p != "":
    #             list1 = [list1[0], list1[1]]
    #             for y in range(0, int(times)):
    #                 pp = p.split()
    #                 list1.append("( ")
    #                 list1.extend(pp)
    #                 list1.append(" )")
    #                 if y < int(times) / 2:
    #                     list1.append("*")
    #             break
    #
    if 'pow' in input_string:
        index = input_string.index('pow')
        to_be_replaced = input_string[index + 4]
        l = list(input_string)
        for i in range(0, 8):
            del (l[index])
        y = to_be_replaced + "*" + to_be_replaced
        l.insert(index, y)
        input_string = ''.join(l)
    for x in range(0, len(input_string)):
        if input_string[x] == '(' or input_string[x] == ')' or input_string[x] == '{' or input_string[x] == '}' or \
                input_string[x] == ';':
            list1.append(input_string[x])
            types_list.append(input_string[x])  # Here

        elif check_if_symbol(input_string[x]):
            list1.append(str(check_if_symbol(input_string[x])))
            types_list.append("Number")  # Here
            numbers.append(float(check_if_symbol(input_string[x])))
        elif check_if_reserved(input_string[x]):
            list1.append(str(input_string[x]))
            types_list.append("Reserved")  # Here
            reserved_words.append(input_string[x])
        elif check_is_string(input_string[x]):
            if input_string[x] in identifiers:
                list1.append("id" + str(identifiers.index(input_string[x]) + 1))
                types_list.append("Identifier")  # Here
            else:
                count += 1
                list1.append(("id" + str(count)))
                types_list.append("Identifier")  # Here
                identifiers.append(input_string[x])
        elif check_is_digit(input_string[x]):
            if input_string[x - 1] == '.' or input_string[x - 2] == '.' or check_is_digit(input_string[x - 1]):
                continue
            if x < len(input_string) - 1:
                if input_string[x + 1] == '.':
                    if check_if_float2(input_string[x], input_string[x + 2], input_string[x + 3]):
                        list1.append(input_string[x] + "." + input_string[x + 2] + input_string[x + 3])
                        types_list.append("Number")  # Here
                        numbers.append(float(input_string[x] + "." + input_string[x + 2] + input_string[x + 3]))
                    elif check_if_float1(input_string[x], input_string[x + 2]):
                        list1.append(input_string[x] + "." + input_string[x + 2])
                        types_list.append("Number")  # Here
                        numbers.append(float(input_string[x] + "." + input_string[x + 2]))
                    else:
                        list1.append(input_string[x])
                        types_list.append("Number")  # Here
                        numbers.append(int(input_string[x]))
                elif check_is_digit(input_string[x + 1]):
                    list1.append(input_string[x] + input_string[x + 1])
                    types_list.append("Number")  # Here
                    numbers.append(input_string[x] + input_string[x + 1])
                else:
                    list1.append(input_string[x])
                    types_list.append("Number")  # Here
                    numbers.append(int(input_string[x]))
            else:
                list1.append(input_string[x])
                types_list.append("Number")  # Here
                numbers.append(int(input_string[x]))
        elif check_is_operator(input_string[x]):
            list1.append(input_string[x])
            types_list.append(input_string[x])
            operators.append(input_string[x])
    # Here
    numbers_found = [[]]
    output_number = 0
    f = False
    n1 = 0
    n2 = 0
    for i in numbers:
        if isinstance(i, float):
            f = True
    flag2 = False
    x = len(types_list)
    for s in range(0, x):
        if types_list[s] == 'Number':
            flag2 = False
            if types_list[s - 1] == '+' and types_list[s - 2] == 'Number':
                numbers_found.append([s, s - 2])
                if f:
                    output_number = float(list1[s]) + float(list1[s - 2])
                    n1 = float(list1[s])
                    n2 = float(list1[s - 2])
                else:
                    output_number = int(list1[s]) + int(list1[s - 2])
                    n1 = int(list1[s])
                    n2 = int(list1[s - 2])
                flag2 = True
            elif types_list[s - 1] == '-' and types_list[s - 2] == "Number":
                numbers_found.append([s, s - 2])
                if f:
                    output_number = float(list1[s]) - float(list1[s - 2])
                    n1 = float(list1[s])
                    n2 = float(list1[s - 2])
                else:
                    output_number = int(list1[s]) - int(list1[s - 2])
                    n1 = int(list1[s])
                    n2 = int(list1[s - 2])
                flag2 = True
            if types_list[s - 1] == '*' and types_list[s - 2] == 'Number':
                numbers_found.append([s, s - 2])
                if f:
                    output_number = float(list1[s]) * float(list1[s - 2])
                    n1 = float(list1[s])
                    n2 = float(list1[s - 2])
                else:
                    output_number = int(list1[s]) * int(list1[s - 2])
                    n1 = int(list1[s])
                    n2 = int(list1[s - 2])
                flag2 = True
            elif types_list[s - 1] == '/' and types_list[s - 2] == "Number":
                numbers_found.append([s, s - 2])
                if f:
                    output_number = float(list1[s]) / float(list1[s - 2])
                    n1 = float(list1[s])
                    n2 = float(list1[s - 2])
                else:
                    output_number = int(list1[s]) / int(list1[s - 2])
                    n1 = int(list1[s])
                    n2 = int(list1[s - 2])
                flag2 = True
            if flag2:
                list1.insert(s + 1, str(output_number))
                list1.remove(list1[s])
                list1.remove(list1[s - 1])
                list1.remove(list1[s - 2])
                types_list.insert(s + 1, "Number")
                types_list.remove(types_list[s - 1])
                types_list.remove(types_list[s - 1])
                types_list.remove(types_list[s - 1])
                numbers.remove(n1)
                numbers.remove(n2)
                numbers.append(output_number)
                break

    print("identifiers -->", identifiers)
    print("operators -->", operators)
    print("numbers -->", numbers)
    print(list1)
    print("lexical Analyzer output -->", ''.join(list1))
    print("type list --> ", ''.join(types_list))


string_input = input()
lexical_Analyzer(string_input)