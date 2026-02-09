"""
基础篇：函数的使用 (Functions)

函数 (Function) 是组织好的、可重复使用的代码块。
使用函数可以提高代码的复用性和可读性。
"""

# ==========================================
# 1. 函数的定义与调用 (Definition & Call)
# ==========================================
print("--- 1. 函数的定义与调用 ---")

# 使用 def 关键字定义函数
def say_hello():
    """这是一个简单的函数，打印一句问候语"""
    print("Hello, Python World!")

# 调用函数 (Call the function)
say_hello()
say_hello()  # 可以多次调用


# ==========================================
# 2. 函数参数 (Parameters & Arguments)
# ==========================================
print("\n--- 2. 函数参数 ---")

# 接收参数的函数
def greet(name):
    """
    接收一个 name 参数，并打印个性化问候
    :param name: 用户名 (str)
    """
    print(f"你好, {name}!")

greet("Alice")
greet("Bob")

# 多个参数
def add(a, b):
    print(f"{a} + {b} = {a + b}")

add(3, 5)


# ==========================================
# 3. 返回值 (Return Values)
# ==========================================
print("\n--- 3. 返回值 ---")

# 使用 return 关键字返回结果
def square(number):
    """计算平方并返回"""
    return number * number

result = square(4)
print(f"4 的平方是: {result}")

# 3.1 隐式返回 None
# 如果没有 return，函数默认返回 None
def no_return():
    print("我没有返回值 (执行完毕)")

ret = no_return()
print(f"无返回值函数的返回结果: {ret}")  # None
print(f"ret 的类型是: {type(ret)}")     # <class 'NoneType'>

# 3.2 显式返回 None
def check_value(x):
    if x < 0:
        return None  # 明确表示无效
    return x * 2

val = check_value(-5)
if val is None:
    print("输入值无效")

# 3.3 return 会立即结束函数 (Early Return)
def early_return_example():
    print("第一步: 执行")
    return "结束"
    print("第二步: 这行代码永远不会被执行！")

print(f"函数结果: {early_return_example()}")



# ==========================================
# 4. 默认参数 (Default Arguments)
# ==========================================
print("\n--- 4. 默认参数 ---")

# 给参数指定默认值
def describe_pet(pet_name, animal_type='dog'):
    """
    显示宠物信息
    :param animal_type: 默认为 'dog'
    """
    print(f"我有一只 {animal_type}，它的名字叫 {pet_name}。")

describe_pet("旺财")                  # 使用默认 animal_type
describe_pet("咪咪", "cat")           # 覆盖默认值
describe_pet(animal_type="hamster", pet_name="球球") # 关键字参数，顺序可以打乱


# ==========================================
# 5. 可变参数 (Variable Arguments) *args
# ==========================================
print("\n--- 5. 可变参数 (*args) ---")

# 当你不确定有多少个参数时，使用 *args
def make_pizza(*toppings):
    """
    打印顾客点的所有配料
    *toppings 会把所有参数打包成一个元组 (tuple)
    """
    print(f"正在制作披萨，配料包含: {toppings}")
    for topping in toppings:
        print(f"- 添加 {topping}")

make_pizza("蘑菇")
make_pizza("芝士", "火腿", "青椒")


# ==========================================
# 6. 关键字可变参数 (Keyword Arguments) **kwargs
# ==========================================
print("\n--- 6. 关键字可变参数 (**kwargs) ---")

# **kwargs 会把多余的关键字参数打包成一个字典 (dict)
def build_profile(first, last, **user_info):
    """创建用户信息字典"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    
    # 将其他信息加入字典
    for key, value in user_info.items():
        profile[key] = value
    
    return profile

user_profile = build_profile('Albert', 'Einstein',
                              location='Princeton',
                              field='Physics')
print(user_profile)


# ==========================================
# 7. 变量作用域 (Scope)
# ==========================================
print("\n--- 7. 变量作用域 ---")

global_var = "我是全局变量"

def test_scope():
    local_var = "我是局部变量"
    print(f"在函数内部: {local_var}")
    print(f"在函数内部访问全局: {global_var}")
    
    # 注意：如果在函数内修改全局变量，需要使用 global 关键字
    # global global_var
    # global_var = "被修改了"

test_scope()
# print(local_var) # 报错：NameError，因为局部变量在函数外不可见
