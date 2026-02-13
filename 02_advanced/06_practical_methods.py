# 06_practical_methods.py - 实战场景：用户注册系统
# 这是一个非常经典的“实战”用法。

import json

class User:
    def __init__(self, username, email):
        print(f"  [__init__] 正在初始化对象... name={username}, email={email}")
        self.username = username
        self.email = email
        print(f"✅ 用户 {self.username} 创建成功！")

    def send_email(self, message):
        """
        实例方法：必须有具体的对象才能发邮件。
        """
        print(f"📧 发送邮件给 {self.email}: {message}")

    # ========================================================
    # 实战场景 1：类方法用作“第二种构造函数” (Factory Pattern)
    # ========================================================
    # 场景：前端传给你的是 JSON 字符串，而不是现成的参数。
    # 你不想在外面解析完再传进来，而是想让 User 类自己有能力处理 JSON。
    @classmethod
    def from_json(cls, json_str):
        """
        接收 JSON 字符串，解析后返回一个 User 对象
        """
        print(f"  [from_json] 1. 现在的 cls 就是: {cls}")
        data = json.loads(json_str)
        print(f"  [from_json] 2. 解析数据: {data}")
        print(f"  [from_json] 3. 准备调用构造函数: cls('{data['name']}', '{data['email']}')")
        
        # cls(...) 等同于 User(...)
        # 这一步会跳转到 __init__ 方法
        new_object = cls(data['name'], data['email'])
        
        print(f"  [from_json] 4. 对象创建完毕，准备返回: {new_object}")
        return new_object

    # ========================================================
    # 实战场景 2：静态方法用作“工具函数” (Utility)
    # ========================================================
    # 场景：在创建用户之前，我们需要检查邮箱格式是否正确。
    # 这个逻辑跟具体的某个用户无关，它是一个通用的规则。
    @staticmethod
    def is_valid_email(email):
        """
        检查邮箱是否包含 @ 符号 (简单的验证)
        """
        return "@" in email

# --- 模拟实战流程 ---

if __name__ == "__main__":
    # 1. 模拟从前端接收到的数据 (JSON 格式)
    api_response = '{"name": "Alice", "email": "alice@example.com"}'
    
    # 2. 模拟用户输入的非法邮箱
    bad_email = "invalid_email_address"

    print("--- 场景 A: 数据校验 (Static Method) ---")
    # 我们不需要创建一个 User 对象就能检查邮箱
    if User.is_valid_email(bad_email):
        print("邮箱有效")
    else:
        print(f"❌ 错误: '{bad_email}' 不是一个有效的邮箱！")

    print("\n--- 场景 B: 处理 JSON 数据 (Class Method) ---")
    # 直接把 JSON 丢给 User 类，让它自己搞定对象的创建
    # 这比在外面写解析代码要整洁得多
    user = User.from_json(api_response)
    
    print("\n--- 场景 C: 正常业务逻辑 (Instance Method) ---")
    user.send_email("欢迎注册！")
