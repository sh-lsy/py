"""
08_sets.py - 集合 (Sets)

集合 (Set) 是一个无序、不重复的元素序列。
主要功能包括：成员关系测试、消除重复元素、数学集合运算（交集、并集、差集等）。

核心特性:
1. 无序性 (Unordered): 集合中的元素没有固定的顺序，不支持索引访问。
2. 唯一性 (Unique): 集合中不允许有重复元素。
3. 可变性 (Mutable): 可以添加或删除元素 (但集合中的元素本身必须是不可变类型)。
"""

def print_section(title):
    print(f"\n{'='*20} {title} {'='*20}")

# 1. 集合的创建 (Creation)
print_section("1. 集合的创建")

# 使用花括号 {} 创建
set1 = {1, 2, 3, 4, 5}
print(f"set1: {set1}, type: {type(set1)}")

# 自动去重
set2 = {1, 2, 2, 3, 3, 3}
print(f"set2 (自动去重): {set2}")

# 使用 set() 函数创建
# 可以将列表、元组、字符串等转换为集合
list_data = [1, 2, 3, 2, 1]
set3 = set(list_data)
print(f"List -> Set (去重): {set3}")

str_data = "hello"
set4 = set(str_data)
print(f"String -> Set (无序): {set4}")

# 注意：创建空集合必须使用 set()，因为 {} 代表空字典
empty_set = set()
empty_dict = {}
print(f"empty_set type: {type(empty_set)}")
print(f"empty_dict type: {type(empty_dict)}")


# 2. 集合的增删改 (Add & Remove)
print_section("2. 集合的增删改")

s = {"Python", "Java", "C++"}
print(f"Original: {s}")

# 添加元素 add()
s.add("Go")
print(f"After add('Go'): {s}")

# update() 更新（合并）其他集合
s.update({"Rust", "Swift"}) # 参数可以是列表、元组等可迭代对象
print(f"After update: {s}")

# 删除元素 remove() - 如果元素不存在会报错 KeyError
s.remove("Java")
print(f"After remove('Java'): {s}")
# s.remove("PHP") # KeyError: 'PHP'

# 删除元素 discard() - 如果元素不存在不会报错 (推荐)
s.discard("PHP") 
print(f"After discard('PHP') (no error): {s}")

# 随机删除 pop() - 因为集合无序，所以删除也是随机的
popped = s.pop()
print(f"Popped element: {popped}")
print(f"After pop: {s}")

# 清空 clear()
s.clear()
print(f"After clear: {s}")


# 3. 集合运算 (Set Operations)
print_section("3. 集合运算 (交/并/差)")

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(f"Set a: {a}")
print(f"Set b: {b}")

# 并集 (Union): 包含 a 和 b 的所有元素
# 运算符: |  方法: union()
print(f"并集 (a | b): {a | b}")
print(f"并集 (union): {a.union(b)}")

# 交集 (Intersection): 同时存在于 a 和 b 的元素
# 运算符: &  方法: intersection()
print(f"交集 (a & b): {a & b}")
print(f"交集 (intersection): {a.intersection(b)}")

# 差集 (Difference): 在 a 中但不在 b 中的元素
# 运算符: -  方法: difference()
print(f"差集 (a - b): {a - b}")     # {1, 2}
print(f"差集 (b - a): {b - a}")     # {5, 6}

# 对称差集 (Symmetric Difference): 在 a 或 b 中，但不同时存在的元素
# 运算符: ^  方法: symmetric_difference()
print(f"对称差集 (a ^ b): {a ^ b}") # {1, 2, 5, 6}


# 4. 集合判断与关系 (Relationships)
print_section("4. 集合判断与关系")

s1 = {1, 2}
s2 = {1, 2, 3}

# 子集 (Subset)
print(f"{s1} <= {s2} (s1 is subset of s2?): {s1.issubset(s2)}")
print(f"{s1} <= {s2} (Operator <=): {s1 <= s2}")

# 超集 (Superset)
print(f"{s2} >= {s1} (s2 is superset of s1?): {s2.issuperset(s1)}")

# 不相交 (Disjoint): 是否没有共同元素
s3 = {4, 5}
print(f"{s1} and {s3} are disjoint?: {s1.isdisjoint(s3)}")


# 5. 不可变集合 (frozenset)
print_section("5. 不可变集合 (frozenset)")

# 普通集合是可变的，不能作为字典的 key
# frozenset 是不可变的，可以作为字典的 key
fs = frozenset([1, 2, 3])
print(f"frozenset: {fs}")
# fs.add(4) # AttributeError: 'frozenset' object has no attribute 'add'

# 字典 key 示例
d = {fs: "Values for 1,2,3"}
print(f"Dictionary with frozenset key: {d}")
