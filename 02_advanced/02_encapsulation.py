"""
进阶篇 02: 封装 (Encapsulation) - 保护你的隐私

【核心概念】
1. 封装 (Encapsulation): 把数据藏起来，只提供特定的“窗口”让别人操作。
2. 私有变量 (Private Variable): 名字前加 `__` (双下划线)。就像锁在保险柜里的钱，外部不能直接拿。
3. Getter/Setter: 专门用来“读”和“写”私有变量的方法。就像银行柜台，你不能直接去金库拿钱，必须通过柜员。
4. @property: Python 特有的语法糖，让用 Getter/Setter 像用普通变量一样简单。

  【生活类比】
- 你的**银行账户余额**是私有的 (Private)。
- 你不能直接拿笔在银行后台改数字 (直接访问属性)。
- 你必须通过**ATM机**或**柜台** (Public Methods) 来存钱、取钱。
- 银行会检查你的密码、余额够不够 (逻辑控制)，才让你操作。
"""

# ==========================================
# 1. 不安全的做法 (没有封装)
# ==========================================
print("--- 1. 不安全的做法 ---")

class Wallet:
    def __init__(self, money):
        self.money = money  # 公有属性，谁都能改

my_wallet = Wallet(100)
print(f"钱包原有: {my_wallet.money}")

# 坏人直接把你的钱改成了 0
my_wallet.money = 0
print(f"被篡改后: {my_wallet.money} (太不安全了！)")


# ==========================================
# 2. 安全的做法 (使用私有变量 + 方法)
# ==========================================
print("\n--- 2. 安全的做法 (封装) ---")

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        # 变量名前加两个下划线 __，变成私有变量
        # Python 会自动给它改名，防止外部直接访问
        self.__balance = balance

    # 提供一个公开的方法来“看”余额 (Getter)
    def get_balance(self):
        # 可以在这里加权限验证：比如检查密码
        return self.__balance

    # 提供一个公开的方法来“存”钱 (Setter)
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"✅ 存入 {amount} 元成功")
        else:
            print("❌ 存入金额必须大于 0")

    # 提供一个公开的方法来“取”钱
    def withdraw(self, amount):
        # 封装的好处：可以在修改数据前做检查 (逻辑控制)
        if amount > self.__balance:
            print("❌ 余额不足！")
        elif amount <= 0:
            print("❌ 取款金额必须大于 0")
        else:
            self.__balance -= amount
            print(f"✅ 取出 {amount} 元成功")

account = BankAccount("小明", 1000)

# 尝试直接访问私有变量 (会报错)
# print(account.__balance) # AttributeError: 'BankAccount' object has no attribute '__balance'

# 必须通过方法访问
print(f"当前余额: {account.get_balance()}")

account.deposit(500)   # 存款
account.withdraw(2000) # 取款 (余额不足，被拦截)
account.withdraw(200)  # 取款 (成功)
print(f"最终余额: {account.get_balance()}")


# ==========================================
# 3. Pythonic 的做法 (@property)
# ==========================================
print("\n--- 3. 高级用法 (@property) ---")

class User:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    # @property 把一个方法变成“属性”的样子
    # 调用时不用加括号 ()
    @property
    def age(self):
        return self.__age

    # @age.setter 允许像属性一样赋值，但实际会走这个方法
    @age.setter
    def age(self, value):
        if 0 < value < 120:
            self.__age = value
            print(f"✅ 年龄已修改为: {value}")
        else:
            print("❌ 年龄不合法 (必须在 0-120 之间)")

p = User("Alice", 25)

# 读属性 (实际上调用了 @property 修饰的 age 方法)
print(f"初始年龄: {p.age}") 

# 写属性 (实际上调用了 @age.setter 修饰的方法)
print("\n--- 关键区别演示 ---")
print("1. 尝试设置不合法的年龄 (-5岁):")
p.age = -5   # 表面是赋值，背后触发了 @age.setter 方法进行检查 -> 拦截！

print("2. 尝试设置合法的年龄 (30岁):")
p.age = 30   # 检查通过 -> 修改成功
print(f"最终年龄: {p.age}")

print("\n【总结】")
print("普通变量 (my_wallet.money = 0): 没有任何检查，想改啥改啥。")
print("@property (p.age = 30): 看着像赋值，其实是在运行代码，可以在里面设卡检查。")

