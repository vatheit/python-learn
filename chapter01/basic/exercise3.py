def e1():
    """
    99乘法表
    """
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(str(j) + '*' + str(i) + '=' + str(i * j), end='\t')
        print()
    return


def e2(n):
    """
    斐波拉切数列：1，1,2,3,5，...
    :return: [1,1,2,3,5]
    """
    arr = []
    for i in range(0, n):

        if i == 0 or i == 1:
            arri = 1
        else:
            arri = arr[i - 1] + arr[i - 2]
        arr.append(arri)
    return arr


if __name__ == "__main__":
    # e1()
    print(e2(20)[2])
    print(e2(20)[6])
    print(e2(102)[100])
