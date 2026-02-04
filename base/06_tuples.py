# -*- coding: utf-8 -*-

def main():
    print("=== Python 元组 (Tuple) 学习 ===")
    
    # --------------------------
    # 1. 元组的定义
    # --------------------------
    print("\n--- 1. 元组的定义 ---")
    # 元组与列表类似，但它是不可变的 (Immutable)
    # 通常用于存储不希望被修改的数据
    
    empty_tuple = ()
    point = (10, 20)           # 坐标点
    user_info = ("Alice", 30)  # 记录
    
    print(f"坐标点: {point}, 类型: {type(point)}")
    
    # 注意: 定义只有一个元素的元组，必须加逗号
    single = (100,)
    not_tuple = (100) # 这只是一个整数
    
    print(f"(100,) 的类型: {type(single)}")
    print(f"(100)  的类型: {type(not_tuple)}")
    
    # 可以省略括号 (Tuple Packing)
    packed = 1, 2, 3
    print(f"1, 2, 3 打包为: {packed}")

    # --------------------------
    # 2. 访问元素 (索引与切片)
    # --------------------------
    print("\n--- 2. 访问元素 ---")
    # 操作方式与列表/字符串完全相同
    
    colors = ("red", "green", "blue", "yellow")
    print(f"colors[0]: {colors[0]}")
    print(f"colors[-1]: {colors[-1]}")
    print(f"colors[1:3]: {colors[1:3]}")

    # --------------------------
    # 3. 不可变性 (Immutability)
    # --------------------------
    print("\n--- 3. 不可变性演示 ---")
    # 元组一旦创建，其元素不能被修改、添加或删除
    
    t = (1, 2, 3)
    print(f"原元组: {t}")
    
    try:
        print("尝试修改 t[0] = 99 ...")
        t[0] = 99
    except TypeError as e:
        print(f"修改失败: {e}")
        
    # 注意: 如果元组包含可变对象 (如列表)，该对象的内容是可以修改的
    nested = (1, [2, 3], 4)
    print(f"\n包含列表的元组: {nested}")
    nested[1][0] = 99 
    print(f"修改内部列表后: {nested}")
    # nested[1] = [8, 9] # 这样会报错，因为不能修改元组对列表的引用

    # --------------------------
    # 4. 常用操作
    # --------------------------
    print("\n--- 4. 常用操作 ---")
    
    # 解包 (Unpacking)
    x, y = (10, 20)
    print(f"解包 x={x}, y={y}")
    
    # 交换变量 (本质上就是元组打包和解包)
    a, b = 1, 2
    a, b = b, a
    print(f"交换变量 a={a}, b={b}")
    
    # 统计与查找
    data = (1, 2, 3, 2, 2, 4)
    print(f"count(2): {data.count(2)}")
    print(f"index(3): {data.index(3)}")
    
    # 拼接与重复 (会生成新元组)
    t1 = (1, 2)
    t2 = (3, 4)
    print(f"t1 + t2: {t1 + t2}")
    
    # 列表与元组转换 (Type Conversion)
    # 有时候我们需要修改元组的内容，可以先转为列表，修改后再转回元组
    print(f"tuple([1, 2]): {tuple([1, 2])}") # 列表 -> 元组
    print(f"list((1, 2)): {list((1, 2))}")   # 元组 -> 列表

if __name__ == "__main__":
    main()
