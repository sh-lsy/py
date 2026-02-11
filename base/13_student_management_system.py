"""
基础篇实战：学员管理系统 (Student Management System)

这是一个基于函数开发的简单控制台管理系统。
涉及知识点：
1. 函数的定义与调用
2. 循环 (while/for)
3. 条件判断 (if/elif/else)
4. 数据结构 (列表 + 字典)
5. 输入输出 (input/print)
6. 随机数模块 (random)
"""

import random
import time

# 全局变量：用于存储所有学员信息
# 结构示例: [{'id': '1001', 'name': '张三', 'phone': '13800138000'}, ...]
students = []

def print_menu():
    """打印功能菜单"""
    print("=" * 30)
    print("   🎓 学员管理系统 V1.0")
    print("=" * 30)
    print(" 1. 添加学员信息")
    print(" 2. 删除学员信息")
    print(" 3. 编辑学员信息")
    print(" 4. 查询学员信息")
    print(" 5. 显示所有学员")
    print(" 6. 退出系统")
    print("=" * 30)

def generate_student_id():
    """
    生成唯一的 4 位随机学号
    :return: 唯一的学号字符串 (str)
    """
    while True:
        # 生成 1000 到 9999 之间的随机数
        new_id = str(random.randint(1000, 9999))
        
        # 检查是否重复
        is_exist = False
        for stu in students:
            if stu['id'] == new_id:
                is_exist = True
                break
        
        # 如果不重复，则返回这个 ID
        if not is_exist:
            return new_id

def add_student():
    """添加学员信息"""
    print("\n--- 添加新学员 ---")
    name = input("请输入学员姓名: ").strip()
    phone = input("请输入手机号码: ").strip()
    
    if not name or not phone:
        print("❌ 错误：姓名和手机号不能为空！")
        return

    # 生成唯一学号
    stu_id = generate_student_id()
    
    # 创建学员字典
    new_student = {
        'id': stu_id,
        'name': name,
        'phone': phone
    }
    
    # 添加到全局列表
    students.append(new_student)
    print(f"✅ 添加成功！学号为: {stu_id}")

def delete_student():
    """删除学员信息"""
    print("\n--- 删除学员 ---")
    del_id = input("请输入要删除的学员学号: ").strip()
    
    # 查找并删除
    for i in range(len(students)):
        if students[i]['id'] == del_id:
            # 再次确认
            confirm = input(f"确认删除学员 {students[i]['name']} 吗？(y/n): ").lower()
            if confirm == 'y':
                del students[i]
                print("✅ 删除成功！")
            else:
                print("操作已取消。")
            return # 结束函数
            
    print("❌ 未找到该学号的学员。")

def edit_student():
    """编辑学员信息"""
    print("\n--- 编辑学员 ---")
    edit_id = input("请输入要修改的学员学号: ").strip()
    
    for stu in students:
        if stu['id'] == edit_id:
            print(f"当前信息 -> 姓名: {stu['name']}, 手机: {stu['phone']}")
            
            # 获取新信息（如果用户直接回车，则不修改）
            new_name = input("请输入新姓名 (回车保持不变): ").strip()
            new_phone = input("请输入新手机 (回车保持不变): ").strip()
            
            if new_name:
                stu['name'] = new_name
            if new_phone:
                stu['phone'] = new_phone
                
            print("✅ 修改成功！")
            return
            
    print("❌ 未找到该学号的学员。")

def search_student():
    """查询学员信息"""
    print("\n--- 查询学员 ---")
    search_id = input("请输入要查询的学员学号: ").strip()
    
    for stu in students:
        if stu['id'] == search_id:
            print("-" * 20)
            print(f"学号: {stu['id']}")
            print(f"姓名: {stu['name']}")
            print(f"手机: {stu['phone']}")
            print("-" * 20)
            return
            
    print("❌ 未找到该学号的学员。")

def show_all_students():
    """显示所有学员信息"""
    print("\n--- 所有学员列表 ---")
    if len(students) == 0:
        print("📭 暂无学员信息，请先添加。")
        return

    # 打印表头
    print(f"{'学号':<10}{'姓名':<10}{'手机号':<15}")
    print("-" * 35)
    
    # 遍历打印
    for stu in students:
        print(f"{stu['id']:<10}{stu['name']:<10}{stu['phone']:<15}")
    print(f"共 {len(students)} 名学员")

def main():
    """主程序入口"""
    while True:
        print_menu()
        choice = input("👉 请选择功能序号 (1-6): ").strip()
        
        if choice == '1':
            add_student()
        elif choice == '2':
            delete_student()
        elif choice == '3':
            edit_student()
        elif choice == '4':
            search_student()
        elif choice == '5':
            show_all_students()
        elif choice == '6':
            confirm = input("确定要退出系统吗？(y/n): ").lower()
            if confirm == 'y':
                print("👋 感谢使用，再见！")
                break
        else:
            print("❌ 输入错误，请输入 1-6 之间的数字。")
            
        # 暂停一下，让用户看清结果
        input("\n按回车键继续...")

if __name__ == "__main__":
    # 预存几个测试数据
    students.append({'id': '1001', 'name': '张三', 'phone': '13812345678'})
    students.append({'id': '1002', 'name': '李四', 'phone': '13987654321'})
    
    main()
