"""
Python 基础学习：字符串详解
本文件涵盖了字符串的定义、基础操作、索引切片、转义字符、格式化以及常用方法。
"""

def main():
    # --------------------------
    # 1. 字符串定义与基础操作
    # --------------------------
    print("--- 1. 基础操作 ---")
    s1 = "Hello"
    s2 = 'World' # 单引号双引号皆可
    
    # 拼接 (+)
    s3 = s1 + ", " + s2 + "!"
    print(f"拼接: {s3}")
    
    # 重复 (*)
    print(f"重复: {'-' * 20}") # 打印20个横杠
    
    # 成员运算符 (in, not in)
    print(f"'He' in s1: {'He' in s1}")
    print(f"'x' not in s1: {'x' not in s1}")

    # --------------------------
    # 2. 索引与切片 (Indexing & Slicing)
    # --------------------------
    print("\n--- 2. 索引与切片 ---")
    text = "PYTHON"
    #  P   Y   T   H   O   N
    #  0   1   2   3   4   5  (正向索引)
    # -6  -5  -4  -3  -2  -1  (反向索引)
    
    print(f"原字符串: {text}")
    print(f"text[0]: {text[0]}")   # P
    print(f"text[-1]: {text[-1]}") # N (最后一个字符)
    
    # 切片语法: [start:stop:step] (包含start, 不包含stop)
    print(f"text[0:2]: {text[0:2]}")   # PY (从0开始到2结束，不含2)
    print(f"text[:2]: {text[:2]}")     # PY (省略start默认从头开始)
    print(f"text[2:]: {text[2:]}")     # THON (省略stop默认到结尾)
    print(f"text[::2]: {text[::2]}")   # PTO (步长为2)
    print(f"text[::-1]: {text[::-1]}") # NOHTYP (步长为-1，实现字符串反转)

    # --------------------------
    # 3. 转义字符 (Escape Characters)
    # --------------------------
    print("\n--- 3. 转义字符 ---")
    print("Line 1\nLine 2")      # \n 换行
    print("Col 1\tCol 2")        # \t 制表符
    print("I\'m a student.")     # \' 单引号
    print("Path: C:\\Windows")   # \\ 反斜杠本身
    print(r"Raw String: C:\Windows\System32\nNo Newline") # r前缀表示原始字符串，不转义

    # --------------------------
    # 4. 字符串格式化
    # --------------------------
    print("\n--- 4. 字符串格式化 ---")
    name = "Alice"
    score = 98.5
    
    # 方式1: % 操作符 (旧式)
    print("Name: %s, Score: %.1f" % (name, score))
    
    # 方式2: str.format() 方法
    print("Name: {}, Score: {:.1f}".format(name, score))
    print("Name: {n}, Score: {s}".format(n=name, s=score))
    
    # 方式3: f-string (Python 3.6+ 推荐)
    print(f"Name: {name}, Score: {score:.1f}")

    # --------------------------
    # 5. 常用内建方法详解
    # --------------------------
    print("\n--- 5. 常用内建方法详解 ---")
    s = "  python programming 101  "
    print(f"原字符串: '{s}'")

    # 5.1 大小写转换
    print("\n[大小写转换]")
    print(f"upper()      全大写: '{s.upper()}'")
    print(f"lower()      全小写: '{s.lower()}'")
    print(f"title()      标题化 (每个单词首字母大写): '{s.title()}'")
    print(f"capitalize() 首字母大写 (其余小写): '{s.strip().capitalize()}'") # 先去空格看效果
    print(f"swapcase()   大小写互换: '{s.swapcase()}'")

    # 5.2 去除空白/字符
    print("\n[去除空白/字符]")
    print(f"strip()  去除两端空白: '{s.strip()}'")
    print(f"lstrip() 去除左侧空白: '{s.lstrip()}'")
    print(f"rstrip() 去除右侧空白: '{s.rstrip()}'")
    # strip 也可以指定要去除的字符
    # 注意: 参数 ' 10' 表示去除两端所有的 "空格"、"1" 和 "0"
    # 它不是作为一个整体子串去匹配，而是只要头尾字符属于这个集合，就会被移除
    # 原串: "  python programming 101  "
    # 右侧: 移除空格 -> 移除 '1' -> 移除 '0' -> 移除 '1' -> 移除空格 -> 遇到 'g' 停止
    print(f"strip(' 10') 去除两端指定字符: '{s.strip(' 10')}'")

    # 5.3 查找与替换
    print("\n[查找与替换]")
    clean_s = s.strip()
    print(f"replace() 替换: '{clean_s.replace('python', 'Java')}'")
    # replace 可以指定替换次数
    print(f"replace() 只替换1次: '{'aba'.replace('a', 'c', 1)}'")
    
    print(f"count()   统计出现次数: {clean_s.count('o')}")
    print(f"find()    查找子串索引 (从左): {clean_s.find('prog')}")
    print(f"rfind()   查找子串索引 (从右): {clean_s.rfind('o')}")
    # find 找不到返回 -1，index 找不到会报错
    print(f"find()    找不到返回: {clean_s.find('X')}")
    # print(clean_s.index('X')) # ValueError

    # 5.4 拆分与连接
    print("\n[拆分与连接]")
    csv_row = "apple, banana, orange"
    fruits = csv_row.split(",") 
    print(f"split() 按逗号分割: {fruits}")
    
    # split 可以指定分割次数
    print(f"split(maxsplit=1): {csv_row.split(',', 1)}")
    
    joined = " | ".join([f.strip() for f in fruits])
    print(f"join()  连接列表: '{joined}'")

    # 5.5 判断方法 (返回布尔值)
    print("\n[判断方法]")
    print(f"startswith('py'): {clean_s.startswith('py')}")
    print(f"endswith('101'): {clean_s.endswith('101')}")
    
    num_str = "12345"
    alpha_str = "abcDE"
    alnum_str = "user123"
    
    print(f"isdigit()  是否全数字 ('{num_str}'): {num_str.isdigit()}")
    print(f"isalpha()  是否全字母 ('{alpha_str}'): {alpha_str.isalpha()}")
    print(f"isalnum()  是否字母数字 ('{alnum_str}'): {alnum_str.isalnum()}")
    print(f"isspace()  是否全空白: {'   \t\n'.isspace()}")
    print(f"isupper()  是否全大写: {'ABC'.isupper()}")
    print(f"islower()  是否全小写: {'abc'.islower()}")

    # 5.6 对齐与填充
    print("\n[对齐与填充]")
    word = "Hi"
    print(f"center() 居中填充: '{word.center(10, '-')}'")
    print(f"ljust()  左对齐  : '{word.ljust(10, '*')}'")
    print(f"rjust()  右对齐  : '{word.rjust(10, '*')}'")
    print(f"zfill()  零填充  : '{'42'.zfill(5)}'") # 常用于数字格式化

    # --------------------------
    # 6. 编码与解码 (Encoding & Decoding)
    # --------------------------
    print("\n--- 6. 编码与解码 ---")
    # 核心概念：
    # str (字符串) --编码(encode)--> bytes (字节序列)
    # bytes (字节序列) --解码(decode)--> str (字符串)
    
    s_original = "Python 编程"
    print(f"原字符串: {s_original} (类型: {type(s_original)})")
    
    # 6.1 编码 (encode)
    # 将人类可读的文本转换为计算机存储的字节
    # utf-8 是国际通用的编码，gbk 是中文环境常用的编码
    s_utf8 = s_original.encode('utf-8')
    print(f"UTF-8 编码: {s_utf8} (类型: {type(s_utf8)})")
    print(f"  -> 长度: {len(s_utf8)} 字节 (英文字符占1字节，中文字符在UTF-8通常占3字节)")
    
    s_gbk = s_original.encode('gbk')
    print(f"GBK   编码: {s_gbk}")
    print(f"  -> 长度: {len(s_gbk)} 字节 (中文字符在GBK通常占2字节)")
    
    # 6.2 解码 (decode)
    # 将字节序列还原为文本
    # 注意：必须使用对应的编码格式，否则会报错或乱码
    print(f"UTF-8 解码: {s_utf8.decode('utf-8')}")
    print(f"GBK   解码: {s_gbk.decode('gbk')}")
    
    # 错误示例：用 GBK 解码 UTF-8 数据
    try:
        print(s_utf8.decode('gbk'))
    except UnicodeDecodeError as e:
        print(f"解码错误 (尝试用GBK解UTF-8): {e}")
    
    # 忽略错误或替换 (errors参数)
    # 'ignore': 忽略无法解码的字节
    # 'replace': 用  替换无法解码的字节
    print(f"忽略错误解码: {s_utf8.decode('gbk', errors='ignore')}")
    print(f"替换错误解码: {s_utf8.decode('gbk', errors='replace')}")

if __name__ == "__main__":
    main()
