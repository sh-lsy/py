# -*- coding: utf-8 -*-

def main():
    print("=== Python 字典 (Dictionary) 学习 ===")
    
    # --------------------------
    # 1. 字典的定义
    # --------------------------
    print("\n--- 1. 字典的定义 ---")
    # 字典是无序的(Python 3.7+ 保持插入顺序)、可变的键值对集合
    # 格式: {key1: value1, key2: value2}
    
    empty_dict = {}
    person = {
        "name": "Alice",
        "age": 30,
        "city": "New York",
        "is_student": False
    }
    
    print(f"个人信息: {person}")
    print(f"类型: {type(person)}")
    print(f"长度 (键值对数量): {len(person)}")
    
    # 使用 dict() 构造函数
    # 注意：关键字参数的键不需要加引号
    book = dict(title="Python Guide", author="Guido", price=59.9)
    print(f"书籍信息: {book}")

    # --------------------------
    # 2. 访问元素
    # --------------------------
    print("\n--- 2. 访问元素 ---")
    
    # 方法 A: 使用方括号 [key]
    print(f"姓名: {person['name']}")
    
    # 如果键不存在，[key] 会报错 KeyError
    # print(person['gender']) # 报错
    
    # 方法 B: 使用 get(key, default) (推荐)
    print(f"年龄: {person.get('age')}")
    print(f"性别 (不存在返回默认值): {person.get('gender', 'Unknown')}")
    print(f"性别 (不存在返回None): {person.get('gender')}")

    # --------------------------
    # 3. 增删改操作
    # --------------------------
    print("\n--- 3. 增删改操作 ---")
    
    # [增加/修改]
    person["email"] = "alice@example.com" # 新增
    person["age"] = 31                    # 修改
    print(f"更新后: {person}")
    
    # update() 方法: 批量更新
    person.update({"age": 32, "city": "London", "phone": "123-456"})
    print(f"批量更新后: {person}")
    
    # [删除]
    removed_val = person.pop("is_student") # pop: 删除指定键并返回对应的值
    print(f"pop('is_student') 移除了: {removed_val}")
    
    # del 语句
    del person["phone"]
    print(f"del person['phone'] 后: {person}")
    
    # popitem(): 删除并返回最后一个插入的键值对 (Python 3.7+)
    last_item = person.popitem()
    print(f"popitem() 移除了: {last_item}")
    
    # clear(): 清空
    temp = {"a": 1, "b": 2}
    temp.clear()
    print(f"clear() 后: {temp}")

    # --------------------------
    # 4. 常用方法与遍历
    # --------------------------
    print("\n--- 4. 常用方法与遍历 ---")
    
    d = {"name": "Bob", "job": "Developer", "level": "Senior"}
    
    # 获取所有键、值、键值对
    print(f"keys(): {list(d.keys())}")
    print(f"values(): {list(d.values())}")
    print(f"items(): {list(d.items())}")
    
    # 遍历字典
    print("\n[遍历键值对]:")
    for key, value in d.items():
        print(f"  {key}: {value}")
        
    print("\n[检查键是否存在]:")
    if "name" in d:
        print("  'name' 在字典中")

    # --------------------------
    # 5. 字典嵌套
    # --------------------------
    print("\n--- 5. 字典嵌套 ---")
    
    users = {
        "user1": {"name": "Tom", "age": 20},
        "user2": {"name": "Jerry", "age": 18}
    }
    
    print(f"User1 Name: {users['user1']['name']}")

if __name__ == "__main__":
    main()
