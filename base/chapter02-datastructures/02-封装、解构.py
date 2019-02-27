"""
lst = list(range(10)) # 这样一个列表，取出第二个、第四个、倒数第二个
"""
lst = list(range(10))
lst[1]
lst[3]
lst[-2]

"""
p 从lst = [1,(2,3,4),5]中，提取4出来 
p 环境变量JAVA_HOME=/usr/bin，返回环境变量名和路径 
p 对列表[1, 9, 8, 5, 6, 7, 4, 3, 2]使用冒泡法排序，要求使用封装和解构来交互数据
"""

lst = [1, (2, 3, 4), 5]
lst[1][2]
_, (*_, val), *_ = lst
val

key, _, val = "JAVA_HOME=/usr/bin".partition("=")

print(key)
print(val)

"""
列表解析
生成一个列表，元素0~9，对每一个元素自增1后求平方返回新列表 
"""

l1 = list(range(10))
l2 = [(i + 1) ** 2 for i in l1]

"""
列表解析
语法
[返回值 for 元素 in 可迭代对象 if 条件] 

获取10以内的偶数，比较执行效率 
"""
even = [x for x in range(10) if x % 2 == 0]


"""
生成器表达式
语法
(返回值 for 元素 in 可迭代对象 if 条件) 

生成器VS列表解析
延迟计算            立即计算
返回迭代器           返回可迭代对象
从前往后只能走一遍       可反复遍历
可使用next取值


集合解析表达式
语法
{返回值 for 元素 in 可迭代对象 if 条件} 

字典解析表达式
{(key,val) for 元素 in 可迭代对象 if 条件} 
"""
