"""
Python 基础学习：变量的定义与赋值
本文件演示了 Python 中变量的定义、命名规则以及各种赋值技巧。
"""

# --------------------------
# 1. 变量定义 (Variable Definition)
# --------------------------
print("--- 1. 变量定义 ---")
# Python 是动态类型语言，不需要显式声明类型
# 变量在赋值时自动被创建
name = "Alice"  # 字符串
age = 30        # 整数
height = 1.75   # 浮点数
is_student = True # 布尔值

print(f"Name: {name}, Type: {type(name)}")
print(f"Age: {age}, Type: {type(age)}")
print(f"Height: {height}, Type: {type(height)}")
print(f"Is Student: {is_student}, Type: {type(is_student)}")

# --------------------------
# 2. 变量命名规则 (Naming Rules)
# --------------------------
# - 必须以字母或下划线 _ 开头
# - 只能包含字母、数字和下划线
# - 大小写敏感
# - 不能使用 Python 关键字 (如 if, def, class 等)

# 合法的变量名
my_var = 1
_private_var = 2
var2 = 3
myVar = 4 # 虽然合法，但 Python 推荐使用蛇形命名法 (snake_case)

# PEP 8 命名建议：
# - 变量名和函数名：使用小写字母，单词间用下划线分隔 (snake_case)
# - 常量：使用全大写字母 (UPPER_CASE)
MAX_CONNECTIONS = 100

# --------------------------
# 3. 赋值技巧 (Assignment Techniques)
# --------------------------
print("\n--- 3. 赋值技巧 ---")

# 3.1 多变量同时赋值 (Tuple Unpacking)
x, y, z = 10, 20, 30
print(f"x={x}, y={y}, z={z}")

# 3.2 链式赋值 (Chained Assignment)
# 将同一个值赋给多个变量
a = b = c = 0
print(f"a={a}, b={b}, c={c}")

# 3.3 变量交换 (Swapping Variables)
# Python 中交换变量不需要临时变量
a, b = 1, 99
print(f"Before swap: a={a}, b={b}")
a, b = b, a
print(f"After swap:  a={a}, b={b}")

# 3.4 扩展解包赋值 (Extended Iterable Unpacking) - Python 3+
# 使用 * 收集剩余的值
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print(f"List: {numbers}")
print(f"First: {first}")
print(f"Middle: {middle}")
print(f"Last: {last}")

# --------------------------
# 4. 类型提示 (Type Hints)
# --------------------------
print("\n--- 4. 类型提示 (Python 3.5+) ---")
# 虽然 Python 是动态类型，但可以使用类型提示来增加代码可读性
# 注意：解释器不会强制检查类型，这只是给开发者和工具看的
user_name: str = "Bob"
user_age: int = 25

print(f"User: {user_name}, Age: {user_age}")

# --------------------------
# 5. 删除变量 (Deleting Variables)
# --------------------------
temp_var = "I will be deleted"
print(f"\nTemp var exists: {temp_var}")
del temp_var
# print(temp_var) # 取消注释这行会导致 NameError，因为变量已被删除
print("Temp var deleted.")
