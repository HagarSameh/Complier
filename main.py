import re


def check_is_string(input_str):
    if input_str.isalpha():
        return True


def check_is_digit(input_str):
    if input_str.strip().isdigit():
        return True


def check_if_float(i1, i2):
    if check_is_digit(i1) and check_is_digit(i2):
        return True


def check_is_operator(input_str):
    operators = ['+', '-', '*', '=', '%', '/', '!', ':=', '<', '>', '^']
    if input_str in operators:
        return True


def check_if_reserved(input_string):
    list1 = ['abstract', 'assert', 'boolean', 'break', 'byte', 'case', 'catch', 'char', 'class', 'const', 'continue',
             'default', 'double', 'do', 'else', 'enum', 'extends', 'false', 'final', 'finally', 'float', 'for', 'goto',
             'if',
             'implements', 'import', 'instanceof',
             'int', 'interface', 'long', 'native', 'new', 'null', 'package', 'private', 'protected', 'public', 'return',
             'short', 'static', 'strictfp',
             'super', 'switch', 'synchronized', 'this', 'throw', 'throws', 'transient', 'true', 'try', 'void',
             'volatile', 'while']
    if input_string in list1:
        return True


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
    operators = []
    identifiers = []
    numbers = []
    reserved_words = []
    list1 = []
    count = 0
    for x in range(0, len(input_string)):
        if input_string[x] == '(' or input_string[x] == ')' or input_string[x] == '{' or input_string[x] == '}' or \
                input_string[x] == ';':
            list1.append(input_string[x])
        elif check_if_symbol(input_string[x]):
            list1.append(str(check_if_symbol(input_string[x])))
            numbers.append(float(check_if_symbol(input_string[x])))
        elif check_if_reserved(input_string[x]):
            list1.append(str(input_string[x]))
            reserved_words.append(input_string[x])
        elif check_is_string(input_string[x]):
            if input_string[x] in identifiers:
                list1.append(("id" + str(identifiers.index(input_string[x]) + 1)))
            else:
                count += 1
                list1.append(("id" + str(count)))
                #identifiers.append(input_string[x])
        elif check_is_digit(input_string[x]):
            if input_string[x - 1] == '.':
                continue
            if x < len(input_string) - 1:
                if input_string[x + 1] == '.':
                    if check_if_float(input_string[x], input_string[x + 2]):
                        list1.append(input_string[x] + "." + input_string[x + 2])
                    else:
                        list1.append(input_string[x])
                else:
                    list1.append(input_string[x])
            else:
                list1.append(input_string[x])
        elif check_is_operator(input_string[x]):
            list1.append(input_string[x])
            operators.append(input_string[x])

    result = re.findall(r"[-+]?\d*\.\d+|\d+", input_string)
    numbers = result
    res = re.findall(r'\w+', input_string)
    identifiers = res
    print("identifiers -->", identifiers)
    print("operators -->", operators)
    print("numbers -->", numbers)
    print("lexical Analyzer output -->", ''.join(list1))


string_input = input()
lexical_Analyzer(string_input)
