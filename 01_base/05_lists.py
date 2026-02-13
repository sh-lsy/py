# -*- coding: utf-8 -*-

def main():
    print("=== Python 列表 (List) 学习 ===")
    
    # --------------------------
    # 1. 列表的定义
    # --------------------------
    print("\n--- 1. 列表的定义 ---")
    # 列表是可变的、有序的序列，可以包含任意类型的元素
    
    empty_list = []                # 空列表
    numbers = [1, 2, 3, 4, 5]      # 数字列表
    fruits = ["apple", "banana"]   # 字符串列表
    mixed = [1, "Hello", 3.14, True] # 混合类型列表
    
    print(f"数字列表: {numbers}")
    print(f"混合列表: {mixed}")
    print(f"列表长度 (len): {len(mixed)}")
    
    # 使用 list() 函数创建
    chars = list("Python") # 将字符串转换为列表
    print(f"list('Python'): {chars}")

    # --------------------------
    # 2. 索引与切片 (Indexing & Slicing)
    # --------------------------
    print("\n--- 2. 索引与切片 ---")
    # 与字符串类似，但列表是可变的 (Mutable)
    
    my_list = ["a", "b", "c", "d", "e"]
    print(f"原列表: {my_list}")
    
    print(f"索引 [0]: {my_list[0]}")
    print(f"索引 [-1]: {my_list[-1]}")
    print(f"切片 [1:4]: {my_list[1:4]}")
    
    # 修改元素 (可变性)
    my_list[0] = "A" 
    print(f"修改 my_list[0] = 'A' 后: {my_list}")
    
    # 切片赋值
    my_list[1:3] = ["B", "C"]
    print(f"切片赋值 my_list[1:3] = ['B', 'C'] 后: {my_list}")

    # --------------------------
    # 3. 列表的操作 (增删改查)
    # --------------------------
    print("\n--- 3. 常用内建方法 (增删改查) ---")
    
    todo = ["Read", "Code"]
    print(f"初始列表: {todo}")
    
    # 3.1 增加元素 (Add)
    print("\n[增加]")
    todo.append("Sleep")          # append: 在末尾添加一个元素
    print(f"append('Sleep'): {todo}")
    
    todo.insert(1, "Eat")         # insert: 在指定索引插入元素
    print(f"insert(1, 'Eat'): {todo}")
    
    others = ["Play", "Music"]
    todo.extend(others)           # extend: 将另一个列表的元素追加到末尾
    print(f"extend({others}): {todo}")
    
    # 3.2 删除元素 (Remove)
    print("\n[删除]")
    item = todo.pop()             # pop: 移除并返回末尾元素 (默认)
    print(f"pop() 移除了: '{item}', 剩余: {todo}")
    
    item_at_1 = todo.pop(1)       # pop(i): 移除指定索引的元素
    print(f"pop(1) 移除了: '{item_at_1}', 剩余: {todo}")
    
    todo.remove("Read")           # remove: 移除第一个匹配的值 (如果不存在会报错)
    print(f"remove('Read'): {todo}")
    
    # del 语句 (按索引删除)
    del todo[0]
    print(f"del todo[0]: {todo}")
    
    todo.clear()                  # clear: 清空列表
    print(f"clear(): {todo}")

    # 3.3 查找与统计 (Search & Count)
    print("\n[查找与统计]")
    nums = [1, 2, 3, 2, 4, 2, 5]
    print(f"列表: {nums}")
    
    count_2 = nums.count(2)       # count: 统计元素出现的次数
    print(f"count(2) 出现的次数: {count_2}")
    
    index_3 = nums.index(3)       # index: 查找元素第一次出现的索引
    print(f"index(3) 的索引: {index_3}")
    # 注意: 如果元素不存在，index() 会抛出 ValueError

    # 3.4 排序与反转 (Sort & Reverse)
    print("\n[排序与反转]")
    unsorted = [3, 1, 4, 1, 5, 9, 2]
    print(f"原列表: {unsorted}")
    
    unsorted.reverse()            # reverse: 原地反转
    print(f"reverse() 反转后: {unsorted}")
    
    unsorted.sort()               # sort: 原地排序 (默认升序)
    print(f"sort() 升序后: {unsorted}")
    
    unsorted.sort(reverse=True)   # sort(reverse=True): 降序
    print(f"sort(reverse=True) 降序后: {unsorted}")

    # --------------------------
    # 4. 列表嵌套 (Nested Lists)
    # --------------------------
    print("\n--- 4. 列表嵌套 ---")
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("二维列表 (矩阵):")
    # matrix 是一个包含 3 个元素的列表，每个元素本身又是一个列表
    # for 循环会依次取出 matrix 中的每个元素 (即每一行)
    # 第1次循环: row = [1, 2, 3]
    # 第2次循环: row = [4, 5, 6]
    # ...
    for row in matrix:
        print(row) # 打印当前的子列表
        
    element = matrix[1][2] # 第2行，第3列 (索引从0开始)
    print(f"访问 matrix[1][2] (即6): {element}")

    # --------------------------
    # 5. 列表常用操作符
    # --------------------------
    print("\n--- 5. 常用操作符 ---")
    list_a = [1, 2]
    list_b = [3, 4]
    
    print(f"拼接 (+): {list_a + list_b}")
    print(f"重复 (*): {list_a * 3}")
    print(f"成员检测 (in): {1 in list_a}")

if __name__ == "__main__":
    main()
