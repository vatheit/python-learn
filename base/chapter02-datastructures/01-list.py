import datetime
import math


def e1(num):
    """
    求100内的素数
    :return:  数组

    """
    arr = []
    for i in range(2, num + 1):
        flag = True
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                flag = False
                break
        if flag:
            arr.append(i)
    return arr


def e1_1(num):
    """
    求100内的素数
    :return:  数组
    """
    arr = []
    flag = True
    for x in range(2, num):
        for i in arr:
            if x % i == 0:
                flag = False
                break
            if i >= math.ceil(math.sqrt(x)):
                flag = True
                break
        if flag:
            arr.append(x)
    return arr


def e2(n):
    """
    计算杨辉三角前n行
    :param n:
    :return:
    """
    triangle = []
    if n >= 1:
        triangle.append([1])
    if n >= 2:
        triangle.append([1, 2])
    for i in range(2, n):
        cur = [1]
        pre = triangle[i - 1]
        for j in range(len(pre) - 1):
            cur.append(pre[j] + pre[j + 1])
        cur.append(1)
        triangle.append(cur)
    return triangle


def e3(matrix):
    """
    给定任何一个矩阵，求转置矩阵
    1 2 3           1 4
    4 5 6   ==>     2 5
                    3 6
    :param matrix:
    :return:
    """
    tm = []
    count = 0
    for row in matrix:
        for i, col in enumerate(row):
            if len(tm) < i + 1:
                tm.append([])
            tm[i].append(col)
            count += 1
    return tm


def e3_1(matrix):
    """
    给定任何一个矩阵，求转置矩阵
    1 2 3           1 4
    4 5 6   ==>     2 5
                    3 6
    :param matrix:
    :return:
    """
    tm = [[0 for col in range(len(matrix))] for row in range(len(matrix[0]))]
    count = 0
    for i, row in enumerate(tm):
        for j, col in enumerate(row):
            tm[i][j] = matrix[j][i]
            count += 1
    return tm


if __name__ == "__main__":
    # print(e1(100))
    # print(e1_1(100))

    print(e2(6))

    matrix = [[1, 2, 3, 5, 9, 5434], [4, 5, 6, 1, 123, 555], [3, 3, 4, 4, 5, 5]]

    start = datetime.datetime.now()
    print(e3(matrix))
    p1 = datetime.datetime.now()

    print(e3_1(matrix))
    p2 = datetime.datetime.now()
    print("method 1: " + str(p1.timestamp() - start.timestamp()))
    print("method 2: " + str(p2.timestamp() - p1.timestamp()))
