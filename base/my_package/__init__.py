"""
my_package 的初始化文件

1. 标识这个文件夹是一个 Python 包。
2. 可以在这里做一些初始化工作（例如打印日志）。
3. 可以控制 `from my_package import *` 导入哪些模块。
4. 可以方便用户直接导入子模块的功能。
"""

print("📦 my_package 正在初始化...")

# 暴露内部模块的功能，让用户可以直接 from my_package import add
# 方式 1: 相对导入 (推荐) - 使用 . 表示当前目录
# 好处：即使包改名了，这里的代码也不用动。
from .math_tools import add
from .str_tools import reverse_str

# 方式 2: 导入整个子模块 (演示 from . import xxx)
# 这样用户可以用 my_package.calc.multiply 调用
from . import calc

# ❌ 错误写法：直接 import .模块名 是语法错误！
# import .math_tools  # SyntaxError

# ✅ 正确写法：如果你想导入整个模块，必须用 from . import
# from . import math_tools
# 这样用户就可以通过 my_package.math_tools 访问

# 方式 3: 绝对导入 (不推荐但可行)
# from my_package.math_tools import add
# 坏处：如果以后你把 my_package 改名为 tools，这里就报错了。

# 控制 from my_package import * 时导入的内容
__all__ = ['add', 'reverse_str', 'calc']
