"""
基础篇：异常处理 (Exception Handling)

异常 (Exception) 是程序在运行时发生的错误。
如果不处理异常，程序会直接崩溃（停止运行）。
使用 try-except 语句可以捕获并处理这些错误，让程序继续运行。
"""

# ==========================================
# 1. 基本语法 (Basic Syntax)
# ==========================================
print("--- 1. 基本语法 ---")

# 场景：除以零错误
try:
    print("尝试计算 10 / 0 ...")
    result = 10 / 0
    print(f"结果是: {result}") # 这行代码不会执行
except ZeroDivisionError:
    print("❌ 错误：不能除以零！")

print("程序继续执行...") # 程序没有崩溃，继续往下走


# ==========================================
# 2. 捕获多种异常 (Multiple Exceptions)
# ==========================================
print("\n--- 2. 捕获多种异常 ---")

def calculate(a, b):
    try:
        # 尝试将输入转换为整数
        x = int(a)
        y = int(b)
        res = x / y
        print(f"计算结果: {res}")
    except ValueError:
        print("❌ 格式错误：请输入数字！")
    except ZeroDivisionError:
        print("❌ 计算错误：除数不能为零！")
    except Exception as e:
        # 捕获其他所有未知的异常，并打印错误信息
        print(f"❌ 未知错误: {e}")

calculate("10", "2")   # 正常
calculate("10", "0")   # ZeroDivisionError
calculate("abc", "2")  # ValueError


# ==========================================
# 3. else 和 finally
# ==========================================
print("\n--- 3. else 和 finally ---")

# try:     尝试执行的代码
# except:  出错时执行的代码
# else:    没出错时执行的代码
# finally: 无论是否出错，最后都会执行的代码（常用于关闭文件、释放资源）

def read_number(text):
    print(f"正在处理: {text}")
    try:
        num = int(text)
    except ValueError:
        print("-> 发生异常：这不是一个数字")
    else:
        print(f"-> 成功转换：{num}")
    finally:
        print("-> [清理工作]：处理结束")
    print("-" * 20)

read_number("123")
read_number("hello")


# ==========================================
# 4. 主动抛出异常 (raise)
# ==========================================
print("\n--- 4. 主动抛出异常 (raise) ---")

def set_age(age):
    """设置年龄，如果年龄不合法则抛出异常"""
    if age < 0:
        raise ValueError("年龄不能是负数！")
    if age > 150:
        raise ValueError("年龄超出人类范围！")
    print(f"年龄设置为: {age}")

try:
    set_age(18)   # 正常
    set_age(-5)   # 会抛出异常
except ValueError as e:
    print(f"❌ 捕获到错误: {e}")


# ==========================================
# 5. 实战演示：文件读取
# ==========================================
print("\n--- 5. 实战演示：文件读取 ---")

def read_file_safe(filename):
    try:
        # open() 可能会抛出 FileNotFoundError
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            print(f"文件内容: {content}")
    except FileNotFoundError:
        print(f"❌ 文件未找到: {filename}")
    except Exception as e:
        print(f"❌ 读取出错: {e}")

read_file_safe("not_exist_file.txt")
