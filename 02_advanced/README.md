---

## 5. 类方法与静态方法 (Class & Static Methods)

### 5.1 方法三剑客：Instance vs Class vs Static

在 Python 类中，有三种定义函数（方法）的方式。它们的主要区别在于**第一个参数是谁**。

| 类型         | 装饰器          | 默认第一个参数    | 用途                                                     | 访问权限              |
| :----------- | :-------------- | :---------------- | :------------------------------------------------------- | :-------------------- |
| **实例方法** | (无)            | `self` (对象本身) | **操作个体**。比如 `dog.speak()`，需要用到狗的名字。     | 访问实例属性 + 类属性 |
| **类方法**   | `@classmethod`  | `cls` (类本身)    | **操作群体/工厂**。比如“现在一共造了多少个机器人”。      | 仅访问类属性          |
| **静态方法** | `@staticmethod` | (无)              | **纯工具**。比如“判断这个名字是否合法”。与具体对象无关。 | 无法访问属性          |

### 5.2 核心代码模式

#### 1. 实例方法 (Instance Method)

最常用的方法。

```python
class Robot:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        # 必须用 self 才能访问到 name
        print(f"我是 {self.name}")
```

#### 2. 类方法 (Class Method)

通常用于**工厂模式**（创建对象的另一种方式）或**管理类状态**。

```python
class Robot:
    population = 0 # 类变量

    def __init__(self, name):
        Robot.population += 1

    @classmethod
    def get_population(cls):
        # cls 就相当于 Robot 类
        return cls.population

    @classmethod
    def create_from_string(cls, info):
        # 工厂模式：把 "R2D2" 这样的字符串变成对象
        return cls(info)
```

#### 3. 静态方法 (Static Method)

既不需要 `self` 也不需要 `cls`，只是正好放在类里面的**普通函数**。

```python
class Robot:
    @staticmethod
    def is_valid_name(name):
        return len(name) > 0
```

### 5.3 实战指南：什么时候用哪个？

> 💡 **实战代码**: [06_practical_methods.py](06_practical_methods.py) (用户注册系统示例)

1.  **实例方法 (Instance Method)**:
    - **口诀**: **"我的事"**。
    - **场景**: `user.send_email()`。发邮件必须得知道具体的收件人是谁，所以是实例方法。

2.  **类方法 (Class Method)**:
    - **口诀**: **"大家的事"** 或 **"怎么生孩子"**。
    - **场景**: `User.from_json()`。
    - 前端传过来一串 JSON 字符，你想把它变成一个 User 对象。这时候对象还没生出来呢，所以不能用实例方法，得用类方法（工厂模式）。

3.  **静态方法 (Static Method)**:
    - **口诀**: **"工具人的事"**。
    - **场景**: `User.is_valid_email()`。
    - 在注册前，你想检查邮箱格式对不对。这跟具体是谁没关系，它只是一个通用的检查逻辑。

### 5.4 知识点小结

1.  **`@classmethod`**: 第一个参数是 `cls`，常用于“工厂”或统计。
2.  **`@staticmethod`**: 没有默认参数，就是个寄生在类里的普通函数。
