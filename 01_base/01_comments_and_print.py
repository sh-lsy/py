"""
Python 基础学习：注释与输出函数
本文件演示了 Python 中不同类型的注释以及 print() 函数的各种用法和参数。
"""

# --------------------------
# 1. 注释 (Comments)
# --------------------------

# 这是单行注释
# Python 解释器会忽略 # 符号后面的所有内容

"""
这是多行注释（使用三个双引号）
通常用于编写长文本注释或文档字符串
"""

'''
这是多行注释（使用三个单引号）
效果与双引号相同
'''

def example_function():
    """
    这是文档字符串 (Docstring)。
    它通常出现在模块、函数、类或方法定义的开头。
    可以通过 help(example_function) 或 example_function.__doc__ 查看。
    """
    pass

# --------------------------
# 2. 输出函数 print()
# --------------------------

print("--- 基础输出 ---")
print("Hello, Python!")  # 输出字符串
print(123)               # 输出数字
print(3.14)              # 输出浮点数

print("\n--- print() 函数的常用参数 ---")

# 参数 1: objects (可以是一个或多个对象)
print("Item 1", "Item 2", "Item 3")  # 默认使用空格分隔

# 参数 2: sep (分隔符)
# 默认是空格 ' '，可以修改为其他字符
print("Apple", "Banana", "Cherry", sep=", ")
print("2023", "10", "01", sep="-")

# 参数 3: end (结束符)
# 默认是换行符 '\n'，可以修改为其他字符（例如空字符串或空格），实现不换行输出
print("Hello", end=" ")
print("World!", end=" [END]\n")

# 参数 4: file (输出目标)
# 默认是 sys.stdout (标准输出/控制台)，可以重定向到文件
# 注意：这里仅演示语法，实际写入文件通常使用 with open(...)
import sys
print("这条错误信息会被输出到标准错误流", file=sys.stderr)

# 参数 5: flush (强制刷新缓冲区)
# 默认是 False。设置为 True 可以强制立即输出内容，不等待缓冲区满。
# 在制作进度条或实时日志时很有用。
import time
print("Loading: ", end="")
for i in range(3):
    print(".", end="", flush=True)
    time.sleep(0.5)
print(" Done!")

print("\n--- 格式化输出简述 (F-string) ---")
name = "Trae"
age = 1
# 使用 f-string (Python 3.6+) 是目前最推荐的格式化输出方式
print(f"My name is {name} and I am {age} year old.")
