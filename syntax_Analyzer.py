import operator
import random

from treelib import Node, Tree


def check_is_string(input_str):
    if input_str.isalpha():
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
    global p
    operators = []
    identifiers = []
    numbers = []
    reserved_words = []
    list1 = []
    count = 0
    # here
    types_list = []
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
        o = list(input_string)
        for i in range(0, 8):
            del (o[index])
        y = to_be_replaced + "*" + to_be_replaced
        o.insert(index, y)
        input_string = ''.join(o)
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
                    output_number = float(list1[s - 2]) - float(list1[s])
                    n1 = float(list1[s - 2])
                    n2 = float(list1[s])
                else:
                    output_number = int(list1[s - 2]) - int(list1[s])
                    n1 = int(list1[s - 2])
                    n2 = int(list1[s])
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
    return list1


def build_parse_tree(expression):
    tree2 = {}
    list1 = [tree2]
    node = tree2
    Ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv, '=': operator.eq}
    pren = ['(', ')']
    for x in expression:
        if x == pren[
            0]:  # if it is a left pren.كل ما يلاقي فتحه براكتس يعمل ايه يعمل اتشيالد ناحية الشمال علشان اكيد هيبقى في اوبيراتور هيبقى في الروت و الرقم اللي جاي بعد البراكتس هو اللي هيتحط في الشمال
            node['left'] = {}  # create a left empty node
            list1.append(node)
            node = node['left']
        elif x == pren[1]:
            node = list1.pop()
        elif x in Ops:
            node[
                'val'] = x  # the one in the middle always (root) then create right node from it علشان الليفت اصلا خلاص اتعمل و هي كانت الخطوة اللي قبليه
            node[
                'right'] = {}  # لما الاوبيراتور بتيحط في النص خلاص بيبدء يعمله رايت بقى علشان يبقى خارج منه اتنين واحده في الليفت اتعملت قبل كدا و واحدة جديدة اهي في الريت هتشيل الرقم الجاي
            list1.append(node)
            node = node['right']

        elif expression.index(x) == 0:  # هنا علشان نحط اول حاجة خالص ك ليفت اتشايلد
            node['left'] = {}
            list1.append(node)
            node = node['left']
            node['val'] = x
            parent = list1.pop()
            node = parent

        else:
            node['val'] = x  # دا الرقم اللي بيجي بعد البراكتس اللي بيتتحط في نود بتاعت الليفت
            parent = list1.pop()
            node = parent

    level = -1
    return tree2


tree = Tree()
tree.create_node(str('='), str('='))


def draw(tree2, operator):
    left = tree2.get('left')
    Le = str(left.get('val'))
    if len(left.values()) == 3:
        if tree.__contains__(Le):
            Lee = str(Le * int(len(tree.all_nodes()) / 2))
            tree.create_node(Lee, Lee, parent=operator)
            draw(left, Lee)
        else:
            tree.create_node(Le, Le, parent=operator)
            draw(left, Le)

    else:
        if tree.__contains__(Le):
            Le = Le + "_" * int(random.randint(0, 5))
        tree.create_node(Le, Le, parent=operator)
    #     -------------------------------------------------------
    right = tree2.get('right')
    Ri = str(right.get('val'))
    if len(right.values()) == 3:
        if tree.__contains__(Ri):
            Rii = str(Ri * int(len(tree.all_nodes()) / 2))
            tree.create_node(Rii, Rii, parent=operator)
            draw(right, Rii)
        else:
            tree.create_node(Ri, Ri, parent=operator)
            draw(right, Ri)
    else:
        if tree.__contains__(Ri):
            Ri = Ri + "_" * int(random.randint(0, 5))
        tree.create_node(Ri, Ri, parent=operator)


string_input = input()
print(build_parse_tree(lexical_Analyzer(string_input)))
draw(build_parse_tree(lexical_Analyzer(string_input)), '=')
tree.show()
