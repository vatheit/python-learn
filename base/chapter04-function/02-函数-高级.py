"""
自由变量：未在本地作用域定义的变量
闭包：内层函数引用了外层函数的自由变量

"""
import datetime
import time


def counter():
    c = [0]

    def inc():
        c[0] += 1
        return c[0]

    return inc


"""
foo = counter()
print(foo(), foo())
c = 100
print(foo())
"""


def counter1():
    count = 0

    def inc():
        nonlocal count
        count += 1
        return count

    return inc


"""
装饰器 增强原函数功能
它是一个函数
函数作为它的形参
返回值也是一个函数
可以使用@fun_name方式，简化调用
"""


def copy_properties(src, dst):
    dst.__name__ = src.__name__
    dst.__doc__ = src.__doc__


def logger(fn):
    """
    :param fn:
    :return:
    """

    def wrapper(*args, **kwargs):
        """
        logger  wrapper
        :param args:
        :param kwargs:
        :return:
        """
        print("args={}, kwargs={}".format(args, kwargs))
        start = datetime.datetime.now()
        ret = fn(*args, **kwargs)
        duration = datetime.datetime.now() - start

        print("function {} took {}s.".format(fn.__name__, duration.total_seconds()))
        return ret

    copy_properties(fn, wrapper)
    return wrapper


@logger  # 等价于 add = logger(add)
def add(x, y):
    """
    add  note
    :param x:
    :param y:
    :return:
    """
    print("===call add ===")
    time.sleep(2)
    return x + y


if __name__ == "__main__":
    print(add(4, 6))
    print("name={}, doc={}".format(add.__name__, add.__doc__))
