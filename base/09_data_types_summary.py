"""
09_data_types_summary.py - 数据类型总结

本文件总结了 Python 中的基本数据类型和复合数据结构，
以及类型转换和通用操作。

1. 基本数据类型 (Basic Data Types): int, float, bool, str, None
2. 复合数据结构 (Compound Data Structures): list, tuple, dict, set
"""

def print_section(title):
    print(f"\n{'='*20} {title} {'='*20}")

# 1. 基本数据类型
print_section("1. 基本数据类型 (Primitives)")

i = 10              # int
f = 3.14            # float
b = True            # bool
c = 1 + 2j          # complex
s = "Hello"         # str
n = None            # NoneType

print(f"int:     {i:<10} type: {type(i)}")
print(f"float:   {f:<10} type: {type(f)}")
print(f"bool:    {str(b):<10} type: {type(b)}")
print(f"complex: {str(c):<10} type: {type(c)}")
print(f"str:     {s:<10} type: {type(s)}")
print(f"None:    {str(n):<10} type: {type(n)}")


# 2. 复合数据结构
print_section("2. 复合数据结构 (Containers)")

lst = [1, 2, 3]             # list (有序可变)
tup = (1, 2, 3)             # tuple (有序不可变)
dct = {"name": "Alice"}     # dict (键值对)
st = {1, 2, 3}              # set (无序不重复)

print(f"list:    {str(lst):<20} type: {type(lst)}")
print(f"tuple:   {str(tup):<20} type: {type(tup)}")
print(f"dict:    {str(dct):<20} type: {type(dct)}")
print(f"set:     {str(st):<20} type: {type(st)}")


# 3. 类型转换 (Type Conversion)
print_section("3. 类型转换 (Type Conversion)")

# 显式转换
print(f"int(3.14)      -> {int(3.14)}")       # 浮点转整型 (截断)
print(f"float(10)      -> {float(10)}")       # 整型转浮点
print(f"str(123)       -> '{str(123)}'")      # 数字转字符串
print(f"bool(0)        -> {bool(0)}")         # 0 为 False
print(f"bool(1)        -> {bool(1)}")         # 非 0 为 True
print(f"list((1,2))    -> {list((1, 2))}")    # 元组转列表
print(f"tuple([1,2])   -> {tuple([1, 2])}")   # 列表转元组
print(f"set([1,2,2])   -> {set([1, 2, 2])}")  # 列表转集合 (去重)
print(f"dict(...)      -> {dict([('a', 1), ('b', 2)])}") # 列表(元组对)转字典
print(f"eval('1+1')    -> {eval('1+1')}")     # 执行字符串表达式

# 隐式转换 (运算时自动发生)
res = 10 + 3.14
print(f"10 + 3.14      -> {res} (type: {type(res)})")


# 4. 公共操作 (Common Operations)
print_section("4. 公共操作 (Common Operations)")

# len() - 获取长度 (不适用于 int/float/bool/None)
print(f"len('hello'): {len('hello')}")
print(f"len([1,2,3]): {len([1, 2, 3])}")

# type() - 获取类型
print(f"type(10) is int: {type(10) is int}")
print(f"isinstance(10, int): {isinstance(10, int)}") # 推荐用 isinstance

# del - 删除变量或元素
x = [10, 20, 30]
del x[0]
print(f"After del x[0]: {x}")

# id() - 获取内存地址
print(f"id(x): {id(x)}")

# max(), min(), sum() - 适用于数字序列
nums = [1, 5, 2, 8]
print(f"nums: {nums}, max: {max(nums)}, min: {min(nums)}, sum: {sum(nums)}")

# sorted() - 排序 (返回新列表)
print(f"sorted(nums): {sorted(nums)}")
