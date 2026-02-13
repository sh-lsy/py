"""
计算器模块
用于演示 from . import xxx 的用法
"""

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b
