"""
1 打印一个边长为n的正方形
2 求100内所有奇数的和（2500）
3 判断学生成绩，成绩等级A~E。其中，90分以上为'A'，80~89分为'B'，
    70~79分为'C'，60~69分 为'D'，60分以下为'E'
4 求1到5阶乘之和
5 给一个数，判断它是否是素数（质数）
"""


def e1(n):
    print('*' * n)
    for i in range(n - 2):
        print('*' + ' ' * (n - 2) + '*')
    print('*' * n)


def e2():
    count = 0
    for i in range(1, 100, 2):
        count += i
    return count


def e3(grade):
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    else:
        return 'E'


def e4(n):
    rst = 1
    for i in range(1, n):
        rst *= i
    return rst


def e5(num):
    flag = True
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            flag = False
    return flag


if __name__ == "__main__":
    e1(5)
    print(e2())
    print(e4(5))
