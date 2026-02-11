"""
基础篇：模块与包 (Modules & Packages)

模块 (Module) 就是一个 Python 文件 (.py)，里面包含了函数、变量和类。
使用模块可以让我们组织代码，把不同功能的代码分开存放，方便复用。
"""

# ==========================================
# 1. 导入标准库 (Standard Library)
# ==========================================
print("--- 1. 导入标准库 ---")

# 方式 1: 直接导入 (import ...)
import math
print(f"圆周率 (math.pi): {math.pi}")
print(f"根号16 (math.sqrt): {math.sqrt(16)}")

# 方式 2: 导入特定功能 (from ... import ...)
from random import randint, choice
print(f"随机整数 (1-10): {randint(1, 10)}")
print(f"随机选择: {choice(['苹果', '香蕉', '橙子'])}")

# 方式 3: 导入并起别名 (import ... as ...)
import datetime as dt
now = dt.datetime.now()
print(f"当前时间: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# 方式 4: 导入所有功能 (from ... import *) - 不推荐
# from math import *
# 缺点: 容易造成变量名冲突，不知道某个函数是从哪里来的。
# 比如 math 和 my_utils 都有 add 函数，后导入的会覆盖先导入的。


# ==========================================
# 2. 模块分类 (Module Classification)
# ==========================================
print("\n--- 2. 模块分类 ---")
# 1. 内置模块 (Built-in): Python 自带的，如 math, random, time, os
# 2. 第三方模块 (Third-party): 需要用 pip 安装的，如 requests, pandas, numpy
# 3. 自定义模块 (Custom): 我们自己写的 .py 文件

# ==========================================
# 3. 导入自定义模块 (Custom Module)
# ==========================================
print("\n--- 3. 导入自定义模块 ---")

# 假设我们在同级目录下有一个 my_utils.py
# 注意观察控制台输出，体会 "模块被加载" 的时机

import my_utils

# 使用模块中的函数
result = my_utils.add(100, 200)
print(f"调用自定义函数: 100 + 200 = {result}")

# 使用模块中的变量
print(f"读取模块变量 PI: {my_utils.PI}")


# ==========================================
# 4. 常见避坑点 (Pitfalls)
# ==========================================
print("\n--- 4. 常见避坑点 ---")
print("1. 模块命名冲突: 千万不要给自己写的 py 文件起名为 math.py, random.py 等。")
print("   否则 import math 时会导入你自己的文件，导致标准库失效！")
print("2. 循环导入: A 导入 B，B 又导入 A，会导致错误。")


# ==========================================
# 5. 关于 if __name__ == "__main__":
# ==========================================
print("\n--- 5. 模块的测试代码 ---")
print("请打开 my_utils.py 查看底部的 if __name__ == '__main__':")
print("当你 import my_utils 时，那段测试代码没有运行，这正是我们想要的！")
print("只有直接运行 python my_utils.py 时，那段代码才会运行。")

# ==========================================
# 6. 什么是包 (Package)?
# ==========================================
# 包就是一个包含 __init__.py 文件的文件夹
# 我们可以把很多相关的模块放在一个包里
# 导入方式: from package_name import module_name
