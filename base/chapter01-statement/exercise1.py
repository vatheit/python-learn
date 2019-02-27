"""
1. 输入2个数字，输出最大数 p
2. 给定一个不超过5位的正整数，判断其有几位
3. 给定一个不超过5位的正整数，判断该数的位数，依次打印出个位、
    十位、百位、千位、万位的数字
"""


def e1():
    a = input("输入两个数，输出大的一个，现在输入第一个数：")
    b = input("现在输入第二个数：")
    if int(a) > int(b):
        return int(a)
    return int(b)


def e2(inte):
    if inte > 10000 or inte <= 0:
        return None
    count = 1
    num = inte
    while num >= 10:
        num = num // 10
        count += 1

    return count


def e3(inte):
    arr = []
    num = inte
    while num >= 1:
        arr.append(num % 10)
        num = num // 10
    return arr


if __name__ == "__main__":
    # print(e1())
    print(e2(24))
    print(e3(23587))
