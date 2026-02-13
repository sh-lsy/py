"""
Python 基础学习：输入函数与运算符
本文件演示了 input() 函数的使用方法以及 Python 中各类运算符的详细示例。

注意：input() 函数会暂停程序运行等待用户输入。
为了方便演示，本脚本在运行时部分 input 可能需要手动输入，
或者可以通过管道传递输入（如 echo "10\n5" | python ...）。
"""

def main():
    # --------------------------
    # 1. 输入函数 input()
    # --------------------------
    print("--- 1. 输入函数 input() ---")
    
    # input() 函数用于接收用户输入，返回结果总是字符串 (str) 类型
    # prompt 参数是可选的，用于提示用户
    
    # 模拟输入（如果是在非交互式环境下运行，可以修改这里的默认值）
    print("请输入您的名字: (示例自动填入 'User')")
    # name = input("请输入您的名字: ") 
    name = "User" # 为了演示方便，这里直接赋值，实际使用请取消上一行注释
    print(f"你好, {name}!")

    print("\n--- 数值输入与类型转换 ---")
    # 因为 input() 返回字符串，进行数学运算前通常需要转换类型
    print("请输入一个数字: (示例自动填入 '10')")
    # num_str = input("请输入一个数字: ")
    num_str = "10"
    
    # 类型转换
    try:
        num = int(num_str) # 转换为整数
        print(f"输入的数字是: {num}, 类型: {type(num)}")
        print(f"它的平方是: {num ** 2}")
    except ValueError:
        print("输入的不是有效的整数！")

    # --------------------------
    # 2. 算术运算符 (Arithmetic Operators)
    # --------------------------
    print("\n--- 2. 算术运算符 ---")
    a = 10
    b = 3
    print(f"a = {a}, b = {b}")
    print(f"加法 (a + b): {a + b}")
    print(f"减法 (a - b): {a - b}")
    print(f"乘法 (a * b): {a * b}")
    print(f"除法 (a / b): {a / b}")    # 结果总是浮点数
    print(f"整除 (a // b): {a // b}")  # 向下取整
    print(f"取模 (a % b): {a % b}")    # 返回余数
    print(f"幂运算 (a ** b): {a ** b}") # a 的 b 次方

    # --------------------------
    # 3. 比较运算符 (Comparison Operators)
    # --------------------------
    print("\n--- 3. 比较运算符 ---")
    # 返回布尔值 True 或 False
    print(f"等于 (a == b): {a == b}")
    print(f"不等于 (a != b): {a != b}")
    print(f"大于 (a > b): {a > b}")
    print(f"小于 (a < b): {a < b}")
    print(f"大于等于 (a >= 10): {a >= 10}")

    # --------------------------
    # 4. 逻辑运算符 (Logical Operators)
    # --------------------------
    print("\n--- 4. 逻辑运算符 ---")
    x = True
    y = False
    print(f"x = {x}, y = {y}")
    print(f"与 (x and y): {x and y}") # 两个都为 True 才返回 True
    print(f"或 (x or y): {x or y}")   # 只要有一个为 True 就返回 True
    print(f"非 (not x): {not x}")     # 取反

    # 短路特性演示
    print("短路演示 (False and ...):", False and print("这行不会被打印"))
    print("短路演示 (True or ...):", True or print("这行不会被打印"))

    # --------------------------
    # 5. 赋值运算符 (Assignment Operators)
    # --------------------------
    print("\n--- 5. 赋值运算符 ---")
    c = 100
    print(f"初始 c = {c}")
    
    c += 10  # c = c + 10
    print(f"c += 10 -> {c}")
    
    c -= 5   # c = c - 5
    print(f"c -= 5  -> {c}")
    
    c *= 2   # c = c * 2
    print(f"c *= 2  -> {c}")
    
    c /= 10  # c = c / 10
    print(f"c /= 10 -> {c} (注意: 结果转为浮点数)")
    
    c //= 3  # c = c // 3
    print(f"c //= 3 -> {c} (向下取整)")
    
    c %= 5   # c = c % 5
    print(f"c %= 5  -> {c} (取余)")
    
    c = 2
    c **= 3  # c = c ** 3
    print(f"重置 c=2, c **= 3 -> {c} (幂运算)")

    # --------------------------
    # 6. 成员运算符 (Membership Operators)
    # --------------------------
    print("\n--- 6. 成员运算符 ---")
    my_list = [1, 2, 3, 4, 5]
    print(f"列表: {my_list}")
    print(f"3 in my_list: {3 in my_list}")
    print(f"10 not in my_list: {10 not in my_list}")
    print(f"'H' in 'Hello': {'H' in 'Hello'}")

    # --------------------------
    # 7. 身份运算符 (Identity Operators)
    # --------------------------
    print("\n--- 7. 身份运算符 ---")
    # is 比较的是对象的内存地址 (id)，== 比较的是值
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    list3 = list1
    
    print(f"list1 == list2 (值相等?): {list1 == list2}")
    print(f"list1 is list2 (是同一个对象?): {list1 is list2}") # False，因为是两个不同的列表对象
    print(f"list1 is list3 (是同一个对象?): {list1 is list3}") # True

if __name__ == "__main__":
    main()
