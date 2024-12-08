# Сложение вычитание вещественных чисел в 9-й системе счисления


def realise_before(num1, num2):
    i_point_first = num1.index(".")
    i_point_second = num2.index(".")
    if i_point_first >= i_point_second:
        num2 = "0" * abs(i_point_first - i_point_second) + num2
    else:
        num1 = "0" * abs(i_point_first - i_point_second) + num1
    return num1, num2


def rlt(num1, num2):
    i_point_first = num1.index(".")
    i_point_second = num2.index(".")
    if i_point_first >= i_point_second:
        return True
    else:
        return False


def realise_after(num1, num2):
    i_point_first = len(num1) - num1.index(".")
    i_point_second = len(num2) - num2.index(".")
    if i_point_first >= i_point_second:
        num2 += "0" * abs(i_point_first - i_point_second)
    else:
        num1 += "0" * abs(i_point_first - i_point_second)
    return num1, num2


def plus(num1, num2):
    if "." not in num1:
        num1 += ".0"
    if "." not in num2:
        num2 += ".0"
    num1, num2 = realise_after(num1, num2)
    num1, num2 = realise_before(num1, num2)
    res = [0] + len(num1[:num1.index(".")]) * [0] + ["."] + [0] * len(num1[num1.index(".") + 1:])
    for i in range(len(num1) - 1, num1.index("."), -1):
        if num1[i - 1] != ".":
            if int(num1[i]) + int(num2[i]) + res[i + 1] < 9:
                res[i + 1] = res[i + 1] + int(num1[i]) + int(num2[i])
            else:
                res[i + 1] = res[i + 1] + int(num1[i]) + int(num2[i]) - 9
                res[i] += 1
        elif num1[i - 1] == ".":
            if int(num1[i]) + int(num2[i]) + res[i + 1] < 9:
                res[i + 1] = res[i + 1] + int(num1[i]) + int(num2[i])
            else:
                res[i + 1] = res[i + 1] + int(num1[i]) + int(num2[i]) - 9
                res[i - 1] += 1
    for i in range(num1.index(".") - 1, -1, -1):
        if int(num1[i]) + int(num2[i]) + res[i + 1] < 9:
            res[i + 1] = res[i + 1] + int(num1[i]) + int(num2[i])
        else:
            res[i + 1] = res[i + 1] + int(num1[i]) + int(num2[i]) - 9
            res[i] += 1

    res_str = "".join(str(v) for v in res)
    result = float(res_str)
    return result


def minus(num1, num2):
    if "." not in num1:
        num1 += ".0"
    if "." not in num2:
        num2 += ".0"

    if float(num1) > float(num2):
        receive_sign = 1
        flag = 1
    else:
        receive_sign = -1
        flag = 0
    num1, num2 = realise_after(num1, num2)
    num1, num2 = realise_before(num1, num2)
    res = len(num1[:num1.index(".")]) * [0] + ["."] + [0] * len(num1[num1.index(".") + 1:])
    if flag:
        for i in range(len(num1) - 1, num1.index("."), -1):
            if num1[i - 1] != ".":
                if int(num1[i]) - int(num2[i]) > 0:
                    res[i] = res[i] + int(num1[i]) - int(num2[i])
                else:
                    res[i] = res[i] + 9 + int(num1[i]) - int(num2[i])
                    res[i - 1] -= 1
            elif num1[i - 1] == ".":
                if int(num1[i]) - int(num2[i]) > 0:
                    res[i] = res[i] + int(num1[i]) + int(num2[i])
                else:
                    res[i] = res[i] + 9 + int(num1[i]) - int(num2[i])
                    res[i - 2] -= 1
        for i in range(num1.index(".") - 1, -1, -1):
            if int(num1[i]) - int(num2[i]) > 0:
                res[i] = res[i] + int(num1[i]) - int(num2[i])
            else:
                res[i] = res[i] + 9 + int(num1[i]) - int(num2[i])
                res[i - 1] -= 1
    else:
        for i in range(len(num2) - 1, num2.index("."), -1):
            if num2[i - 1] != ".":
                if int(num2[i]) - int(num1[i]) > 0:
                    res[i] = res[i] + int(num2[i]) - int(num1[i])
                else:
                    res[i] = res[i] + 9 + int(num2[i]) - int(num1[i])
                    res[i - 1] -= 1
            elif num2[i - 1] == ".":
                if int(num2[i]) - int(num1[i]) > 0:
                    res[i] = res[i] + int(num2[i]) + int(num1[i])
                else:
                    res[i] = res[i] + 9 + int(num2[i]) - int(num1[i])
                    res[i - 2] -= 1
        for i in range(num2.index(".") - 1, -1, -1):
            if int(num2[i]) - int(num1[i]) > 0:
                res[i] = res[i] + int(num2[i]) - int(num1[i])
            else:
                res[i] = res[i] + 9 + int(num2[i]) - int(num1[i])
                res[i - 1] -= 1
    res_str = "".join(str(v) for v in res)
    result = receive_sign * float(res_str)
    return result




