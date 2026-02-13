"""
10_conditionals.py - 条件语句 (Conditional Statements)

条件语句允许程序根据不同的情况执行不同的代码块。
主要关键字: if, elif, else

核心知识点:
1. 缩进 (Indentation): Python 依靠缩进来划分代码块，必须严格保持一致（推荐 4 个空格）。
2. 布尔上下文 (Boolean Context): 非零数值、非空容器、True 视为真；0、空容器、None、False 视为假。
3. 逻辑运算符: and, or, not 用于组合多个条件。
"""

def print_section(title):
    print(f"\n{'='*20} {title} {'='*20}")

# 1. 基本语法 (Basic Syntax)
print_section("1. 基本语法 (if-elif-else)")

score = 85
print(f"Score: {score}")

if score >= 90:
    print("Grade: A (优秀)")
elif score >= 80:
    print("Grade: B (良好)")
elif score >= 60:
    print("Grade: C (及格)")
else:
    print("Grade: D (不及格)")

# 注意: 一旦某个条件满足，后续的 elif/else 将不再执行


# 2. 嵌套条件 (Nested Conditionals)
print_section("2. 嵌套条件")

age = 20
has_ticket = True

if age >= 18:
    print("年龄符合要求")
    if has_ticket:
        print("凭票入场 -> 允许进入")
    else:
        print("无票 -> 拒绝进入")
else:
    print("未成年 -> 禁止入内")


# 3. 逻辑运算符组合 (Logical Operators)
print_section("3. 逻辑运算符 (and, or, not)")

is_weekend = True
is_sunny = False

# and: 两个条件都必须为真
if is_weekend and is_sunny:
    print("去野餐吧！")
else:
    print("待在家里看书。")

# or: 只要有一个为真
if is_weekend or is_sunny:
    print("心情不错！")

# not: 取反
if not is_sunny:
    print("外面没有太阳。")


# 4. 真值测试 (Truth Value Testing)
print_section("4. 真值测试 (Implicit Booleans)")

# 在 Python 中，以下值在 if 中会被视为 False:
# False, None, 0, 0.0, "" (空字符串), [] (空列表), {} (空字典), set() (空集合)

items = []  # 空列表
if items:
    print(f"列表有 {len(items)} 个元素")
else:
    print("列表是空的 (Implicit False)")

name = "Python"
if name:
    print(f"Name is: {name} (Implicit True)")


# 5. 三元运算符 (Ternary Operator)
print_section("5. 三元运算符 (Conditional Expression)")

# 语法: value_if_true if condition else value_if_false
# 适合简单的赋值操作

x = 10
y = 20

max_val = x if x > y else y
print(f"Max between {x} and {y} is: {max_val}")

status = "Adult" if age >= 18 else "Minor"
print(f"Status: {status}")


# 6. pass 语句
print_section("6. pass 占位符")

# 如果代码块中什么都不做，必须写 pass，否则会报错
if True:
    pass  # TODO: 以后再实现逻辑
    print("pass 语句已执行，用于占位防止报错")
