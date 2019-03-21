"""
编写一个函数，能够接受至少2个参数，返回最小值和最大值
"""


def fun1(*args):
    length = len(args)

    if length == 1:
        return [args[0], args[1]]
    if length > 1:
        max_val = min_val = args[0]
        for x in args:
            if x > max_val:
                max_val = x
            if x < min_val:
                min_val = x
        return [min_val, max_val]
    return None


"""
编写一个函数，接受一个参数n，n为正整数，左右两种打印方式。要求数字必须对齐
"""


def fun2(n):
    tail = " ".join([str(i) for i in range(n, 0, -1)])
    width = len(tail)
    for i in range(1, n + 1):
        print("{:>{}}".format(" ".join([str(j) for j in range(i, 0, -1)]), width))
    # print(tail)


if __name__ == "__main__":
    fun2(5)
