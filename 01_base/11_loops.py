"""
11_loops.py - 循环语句 (Loops)

循环语句用于重复执行某段代码。
Python 主要有两种循环：
1. for 循环: 遍历序列 (如列表、字符串) 或数字范围。
2. while 循环: 当条件为真时持续运行。

核心关键字: for, in, while, break, continue, else
"""

def print_section(title):
    print(f"\n{'='*20} {title} {'='*20}")

# 1. for 循环基础 (Basic for Loop)
print_section("1. for 循环 (遍历序列)")

# 遍历列表
fruits = ["Apple", "Banana", "Cherry"]
print("遍历列表:")
for fruit in fruits:
    print(f"  I like {fruit}")

# 遍历字符串
word = "Python"
print("\n遍历字符串:")
for char in word:
    print(f"  {char}", end="-") # end="-" 让输出不换行，用 - 连接
print("Done")


# 2. range() 函数 (Generating Numbers)
print_section("2. range() 函数")

# range(stop): 0 到 stop-1
print("range(5):", list(range(5)))

# range(start, stop): start 到 stop-1
print("range(2, 6):", list(range(2, 6)))

# range(start, stop, step): 步长
print("range(0, 10, 2):", list(range(0, 10, 2)))

print("\n使用 range 循环:")
for i in range(1, 4):
    print(f"  Count: {i}")


# 3. while 循环 (While Loop)
print_section("3. while 循环")

count = 3
while count > 0:
    print(f"  倒计时: {count}")
    count -= 1  # 重要：必须手动更新条件，否则会变成死循环
print("  发射!")


# 4. 循环控制 (Loop Control)
print_section("4. 循环控制 (break/continue)")

# break: 立即终止整个循环
print("测试 break (遇到 5 停止):")
for i in range(1, 10):
    if i == 5:
        print("  -> Found 5, breaking!")
        break
    print(f"  {i}", end=" ")
print()

# continue: 跳过本次循环，进入下一次
print("\n测试 continue (跳过偶数):")
for i in range(1, 6):
    if i % 2 == 0:
        continue # 跳过下面的 print，直接开始下一次循环
    print(f"  {i} 是奇数")


# 5. 循环中的 else (else in Loops)
print_section("5. 循环中的 else 子句")

# 特性: 当循环【正常结束】时执行 else 块。
# 如果循环是被 break 【强制中断】的，则【不执行】 else 块。

print("场景 1: 正常结束")
for i in range(3):
    print(f"  Checking {i}...")
else:
    print("  -> 循环全部完成，没有被中断。")

print("\n场景 2: 被 break 中断")
for i in range(3):
    print(f"  Checking {i}...")
    if i == 1:
        print("  -> 遇到问题，中断!")
        break
else:
    print("  -> 这句话不会打印，因为循环被 break 了。")


# 6. 嵌套循环 (Nested Loops)
print_section("6. 嵌套循环 (九九乘法表)")

for i in range(1, 4):      # 外层循环 (行)
    for j in range(1, i+1): # 内层循环 (列)
        print(f"{j}x{i}={i*j}", end="\t") # \t 是制表符，对齐用
    print() # 换行
