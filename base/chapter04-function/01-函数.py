"""
函数定义
def fun_name(param_list):
    fun_body
    [return VAL]


"""


def showConfig(*kwargs):
    """
    位置参数的可变参数
    :param kwargs:
    :return:
    """
    for x in kwargs:
        print(x)

    return


def showConfig(**kwargs):
    """
    关键字参数的可变参数
    :param kwargs:
    :return:
    """
    for k, v in kwargs.items():
        print('{} = {}'.format(k, v))


def fn(*, x, y):
    """
    keyword-only参数
    :param x:
    :param y:
    :return:
    """
    print(x, y)


fn(2, 34, x=5, y=6)

"""
缺省参数
def fn(x=1,y):
    return None

在调用fn时，可以不传x

"""


def paramDestruct(x, y):
    return x + y


paramDestruct(*[4, 2])  # 参数解构


"""

"""
