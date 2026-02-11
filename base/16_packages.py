"""
基础篇：包 (Packages)

包 (Package) 本质上就是一个包含 `__init__.py` 文件的**文件夹**。
它用于组织多个模块，形成一个层级结构（目录树）。
"""

# ==========================================
# 1. 导入包中的模块 (Import Submodule)
# ==========================================
print("--- 1. 导入子模块 ---")

# 语法: import 包名.模块名
import my_package.math_tools
import my_package.str_tools

print(f"10 + 5 = {my_package.math_tools.add(10, 5)}")
print(f"反转 'Python': {my_package.str_tools.reverse_str('Python')}")

# 【回答疑问 2】能否使用子模块其他方法？
# 答案：可以！只要你导入了具体的子模块 (math_tools)，该模块里定义的所有函数都可以用。
# __init__.py 只是提供了一个“快捷方式”，并不限制子模块本身的功能。
print(f"10 - 5 = {my_package.math_tools.sub(10, 5)} (直接通过子模块调用)")


# ==========================================
# 2. 使用 from ... import 简化
# ==========================================
print("\n--- 2. 使用 from ... import ---")

# 【回答疑问 1】为啥 __init__.py 没写 sub 也能导入？
# 答案：因为这里我们是直接找的 `math_tools.py` 这个文件 (from my_package.math_tools)，
# 而不是找的 `my_package` 这个包 (from my_package)。
# 只要文件存在，就可以直接导入里面的任何函数。

# 语法: from 包名.模块名 import 函数名
from my_package.math_tools import sub
from my_package.str_tools import to_upper

print(f"10 - 5 = {sub(10, 5)}")
print(f"大写: {to_upper('hello')}")


# ==========================================
# 3. 利用 __init__.py 的便捷导入
# ==========================================
print("\n--- 3. 利用 __init__.py 简化导入 ---")

# 我们在 __init__.py 中已经提前导入了 add 和 reverse_str
# 所以用户可以直接从包名导入，不需要写模块名
# 语法: from 包名 import 函数名

from my_package import add, reverse_str

print(f"直接导入 add: {add(100, 200)}")
print(f"直接导入 reverse_str: {reverse_str('abc')}")

# 演示 from . import calc 的效果
# 我们在 __init__.py 中写了 from . import calc
# 所以现在可以通过 my_package.calc 来使用
import my_package # 必须先导入包，或者上面已经导入过
print(f"通过包导入的子模块计算乘法: {my_package.calc.multiply(3, 4)}")


# ==========================================
# 4. 什么是 __init__.py?
# ==========================================
# 它是包的入口文件。
# 当你第一次导入包（或包内的模块）时，__init__.py 会自动运行。
# 它的作用：
# 1. 标识文件夹为包。
# 2. 初始化代码（如打印日志）。
# 3. 暴露常用功能（如上面的第 3 点）。
