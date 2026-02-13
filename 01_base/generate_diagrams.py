import matplotlib.pyplot as plt
import os

def create_string_index_diagram():
    # 设置中文字体 (Windows 下常用 Microsoft YaHei, SimHei)
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial']
    plt.rcParams['axes.unicode_minus'] = False # 解决负号显示问题

    text = "PYTHON"
    n = len(text)
    
    fig, ax = plt.subplots(figsize=(8, 3))
    ax.set_xlim(-1.5, n - 0.5) # 调整左边界以容纳中文标签
    ax.set_ylim(0, 3)
    ax.axis('off')
    
    # 绘制方格和文字
    for i, char in enumerate(text):
        # 方格
        rect = plt.Rectangle((i - 0.5, 1), 1, 1, facecolor='lightblue', edgecolor='black')
        ax.add_patch(rect)
        
        # 字符
        ax.text(i, 1.5, char, ha='center', va='center', fontsize=20, weight='bold')
        
        # 正向索引
        ax.text(i, 2.3, str(i), ha='center', va='center', fontsize=14, color='green')
        
        # 反向索引
        ax.text(i, 0.7, str(i - n), ha='center', va='center', fontsize=14, color='red')

    # 添加说明标签 (中文)
    ax.text(-0.6, 2.3, "正向索引:", ha='right', va='center', fontsize=12, color='green')
    ax.text(-0.6, 1.5, "字符串:", ha='right', va='center', fontsize=12, color='black', weight='bold')
    ax.text(-0.6, 0.7, "反向索引:", ha='right', va='center', fontsize=12, color='red')

    plt.title("Python 字符串索引示意图", fontsize=16)
    plt.tight_layout()
    
    # 保存图片
    output_path = os.path.join(os.path.dirname(__file__), 'assets', 'string_indices.png')
    plt.savefig(output_path, dpi=100)
    print(f"Image saved to: {output_path}")

def create_function_diagram():
    """生成函数输入输出示意图"""
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial']
    plt.rcParams['axes.unicode_minus'] = False

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')

    # 绘制函数盒子
    box = plt.Rectangle((3, 2), 4, 2, facecolor='#FFEB3B', edgecolor='black', lw=2)
    ax.add_patch(box)
    ax.text(5, 3, "Function\n(函数体)", ha='center', va='center', fontsize=16, weight='bold')

    # 输入箭头
    ax.arrow(1, 3, 1.8, 0, head_width=0.2, head_length=0.2, fc='blue', ec='blue', lw=2)
    ax.text(1.5, 3.3, "Input\n(参数)", ha='center', va='center', fontsize=12, color='blue')

    # 输出箭头
    ax.arrow(7, 3, 1.8, 0, head_width=0.2, head_length=0.2, fc='green', ec='green', lw=2)
    ax.text(8.5, 3.3, "Output\n(返回值)", ha='center', va='center', fontsize=12, color='green')

    # 黑盒子比喻
    ax.text(5, 1.5, "黑盒子: 你不需要知道内部细节\n只需要知道给什么，得什么", ha='center', va='center', fontsize=10, style='italic')

    plt.title("函数工作原理示意图", fontsize=16)
    plt.tight_layout()

    # 保存图片
    output_path = os.path.join(os.path.dirname(__file__), 'assets', 'function_flow.png')
    plt.savefig(output_path, dpi=100)
    print(f"Image saved to: {output_path}")

def create_system_flow_diagram():
    """生成学员管理系统流程图"""
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial']
    plt.rcParams['axes.unicode_minus'] = False

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # 定义盒子样式
    bbox_props = dict(boxstyle="round,pad=0.5", fc="white", ec="black", lw=2)
    bbox_start = dict(boxstyle="round,pad=0.5", fc="#90EE90", ec="black", lw=2)
    bbox_decision = dict(boxstyle="round4,pad=0.5", fc="#FFEB3B", ec="black", lw=2)

    # 1. 开始
    ax.text(5, 7, "Start\n(开始)", ha='center', va='center', fontsize=12, bbox=bbox_start)
    ax.arrow(5, 6.5, 0, -0.8, head_width=0.1, head_length=0.1, fc='black', ec='black')

    # 2. 显示菜单
    ax.text(5, 5.2, "Show Menu\n(显示菜单)", ha='center', va='center', fontsize=12, bbox=bbox_props)
    ax.arrow(5, 4.7, 0, -0.8, head_width=0.1, head_length=0.1, fc='black', ec='black')

    # 3. 用户输入
    ax.text(5, 3.4, "User Input\n(用户选择)", ha='center', va='center', fontsize=12, bbox=bbox_decision)

    # 4. 分支箭头
    # 左侧分支 (功能)
    ax.arrow(3.5, 3.4, -2, 0, head_width=0.1, head_length=0.1, fc='black', ec='black')
    ax.text(1.5, 3.8, "1-5", ha='center', va='center', fontsize=10)
    ax.text(0.5, 3.4, "执行对应\n功能函数", ha='center', va='center', fontsize=12, bbox=bbox_props)
    
    # 回环箭头 (功能 -> 菜单)
    ax.arrow(0.5, 3.9, 0, 1.8, head_width=0, head_length=0, fc='black', ec='black')
    ax.arrow(0.5, 5.7, 3.5, 0, head_width=0.1, head_length=0.1, fc='black', ec='black')

    # 右侧分支 (退出)
    ax.arrow(6.5, 3.4, 2, 0, head_width=0.1, head_length=0.1, fc='black', ec='black')
    ax.text(7.5, 3.8, "6 (Exit)", ha='center', va='center', fontsize=10)
    ax.text(9.5, 3.4, "End\n(结束)", ha='center', va='center', fontsize=12, bbox=bbox_start)

    plt.title("学员管理系统运行流程", fontsize=16)
    plt.tight_layout()

    # 保存图片
    output_path = os.path.join(os.path.dirname(__file__), 'assets', 'system_flow.png')
    plt.savefig(output_path, dpi=100)
    print(f"Image saved to: {output_path}")

def create_exception_diagram():
    """生成异常处理流程图"""
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial']
    plt.rcParams['axes.unicode_minus'] = False

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')

    bbox_rect = dict(boxstyle="round,pad=0.5", fc="white", ec="black", lw=2)
    bbox_diamond = dict(boxstyle="round4,pad=0.5", fc="#FFEB3B", ec="black", lw=2)
    bbox_green = dict(boxstyle="round,pad=0.5", fc="#90EE90", ec="black", lw=2)
    bbox_red = dict(boxstyle="round,pad=0.5", fc="#FFCCCB", ec="black", lw=2)

    # 1. try 块
    ax.text(5, 7, "try:\n运行代码", ha='center', va='center', fontsize=12, bbox=bbox_rect)
    ax.arrow(5, 6.5, 0, -0.8, head_width=0.1, head_length=0.1, fc='black', ec='black')

    # 2. 判断是否有异常
    ax.text(5, 5.2, "Has Error?\n(是否出错)", ha='center', va='center', fontsize=12, bbox=bbox_diamond)

    # 3. 分支
    # Yes (出错) -> except
    ax.arrow(6.5, 5.2, 1.5, 0, head_width=0.1, head_length=0.1, fc='red', ec='red')
    ax.text(7, 5.4, "Yes", color='red')
    ax.text(8.5, 4, "except:\n捕获异常", ha='center', va='center', fontsize=12, bbox=bbox_red)

    # No (没出错) -> else
    ax.arrow(3.5, 5.2, -1.5, 0, head_width=0.1, head_length=0.1, fc='green', ec='green')
    ax.text(3, 5.4, "No", color='green')
    ax.text(1.5, 4, "else:\n顺利执行", ha='center', va='center', fontsize=12, bbox=bbox_green)

    # 4. finally
    ax.arrow(1.5, 3.5, 2.5, -1.3, head_width=0.1, head_length=0.1, fc='black', ec='black') # else -> finally
    ax.arrow(8.5, 3.5, -2.5, -1.3, head_width=0.1, head_length=0.1, fc='black', ec='black') # except -> finally
    
    ax.text(5, 1.5, "finally:\n清理工作\n(总是执行)", ha='center', va='center', fontsize=12, bbox=bbox_rect)

    plt.title("异常处理 (try-except) 流程", fontsize=16)
    plt.tight_layout()

    output_path = os.path.join(os.path.dirname(__file__), 'assets', 'exception_flow.png')
    plt.savefig(output_path, dpi=100)
    print(f"Image saved to: {output_path}")

def create_module_diagram():
    """生成模块导入关系图"""
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial']
    plt.rcParams['axes.unicode_minus'] = False

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')

    bbox_main = dict(boxstyle="round,pad=0.5", fc="#ADD8E6", ec="black", lw=2)
    bbox_module = dict(boxstyle="round,pad=0.5", fc="#FFD700", ec="black", lw=2)
    bbox_lib = dict(boxstyle="round,pad=0.5", fc="#90EE90", ec="black", lw=2)

    # Main Script
    ax.text(5, 4.5, "main.py\n(主程序)", ha='center', va='center', fontsize=14, bbox=bbox_main)

    # Standard Lib
    ax.text(2, 1.5, "math / random\n(Python 标准库)", ha='center', va='center', fontsize=12, bbox=bbox_lib)
    
    # Custom Module
    ax.text(8, 1.5, "my_utils.py\n(自定义模块)", ha='center', va='center', fontsize=12, bbox=bbox_module)

    # Arrows
    ax.annotate("", xy=(5, 4), xytext=(2, 2.2), arrowprops=dict(arrowstyle="<-", lw=2, color='gray'))
    ax.text(2.8, 3.2, "import math", rotation=35, color='gray', fontsize=10)

    ax.annotate("", xy=(5, 4), xytext=(8, 2.2), arrowprops=dict(arrowstyle="<-", lw=2, color='gray'))
    ax.text(6.5, 3.2, "import my_utils", rotation=-35, color='gray', fontsize=10)

    # Explanation
    ax.text(5, 0.5, "模块就像工具箱，主程序按需导入使用", ha='center', va='center', fontsize=12, style='italic')

    plt.title("模块导入关系示意图", fontsize=16)
    plt.tight_layout()

    output_path = os.path.join(os.path.dirname(__file__), 'assets', 'module_flow.png')
    plt.savefig(output_path, dpi=100)
    print(f"Image saved to: {output_path}")

def create_package_diagram():
    """生成包结构示意图"""
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial']
    plt.rcParams['axes.unicode_minus'] = False

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # 文件夹图标 (简单矩形代替)
    bbox_folder = dict(boxstyle="square,pad=0.3", fc="#FFD700", ec="black", lw=2)
    bbox_file = dict(boxstyle="square,pad=0.3", fc="#E0E0E0", ec="black", lw=1)

    # 根目录
    ax.text(5, 7, "my_package/ (文件夹)", ha='center', va='center', fontsize=14, bbox=bbox_folder)
    
    # 连接线
    ax.plot([5, 5], [6.5, 6], color='black', lw=2)  # 竖线
    ax.plot([2, 8], [6, 6], color='black', lw=2)    # 横线
    
    # 子文件连线
    ax.plot([2, 2], [6, 5.5], color='black', lw=2)
    ax.plot([5, 5], [6, 5.5], color='black', lw=2)
    ax.plot([8, 8], [6, 5.5], color='black', lw=2)

    # 文件
    ax.text(2, 5, "__init__.py", ha='center', va='center', fontsize=12, bbox=bbox_file)
    ax.text(5, 5, "math_tools.py", ha='center', va='center', fontsize=12, bbox=bbox_file)
    ax.text(8, 5, "calc.py", ha='center', va='center', fontsize=12, bbox=bbox_file)

    # 说明
    ax.text(2, 4, "from . import calc", ha='center', va='top', fontsize=10, color='red')
    ax.text(5, 4, "def add(x, y)", ha='center', va='top', fontsize=10, style='italic')
    ax.text(8, 4, "def multiply(a, b)", ha='center', va='top', fontsize=10, style='italic')

    # 导入示意
    ax.text(5, 2, "Import Actions (导入行为)", ha='center', va='center', fontsize=14, weight='bold')
    
    ax.text(1, 1, "from my_package import calc", ha='left', va='center', fontsize=11, color='blue')
    ax.text(5.5, 1, "--> 导入整个模块对象", ha='left', va='center', fontsize=11, color='gray')

    ax.text(1, 0.5, "my_package.calc.multiply(2,3)", ha='left', va='center', fontsize=11, color='blue')
    ax.text(5.5, 0.5, "--> 调用模块内函数", ha='left', va='center', fontsize=11, color='gray')

    plt.title("Python 包 (Package) 结构示意图", fontsize=16)
    plt.tight_layout()

    output_path = os.path.join(os.path.dirname(__file__), 'assets', 'package_structure.png')
    plt.savefig(output_path, dpi=100)
    print(f"Image saved to: {output_path}")

if __name__ == "__main__":
    try:
        # 暂时注释掉，避免重复生成图片
        # create_string_index_diagram()  # 生成字符串索引示意图 (配合字符串/列表章节)
        # create_function_diagram()      # 生成函数工作原理图 (配合 12_functions.py)
        # create_system_flow_diagram()   # 生成学员管理系统流程图 (配合 13_student_management_system.py)
        # create_exception_diagram()     # 生成异常处理流程图 (配合 14_exceptions.py)
        # create_module_diagram()        # 生成模块导入关系图 (配合 15_modules.py)
        create_package_diagram()       # 生成包结构示意图 (配合 16_packages.py)
        # print("Skipping diagram generation (commented out).")
    except ImportError:
        print("matplotlib not installed. Skipping image generation.")
    except Exception as e:
        print(f"Error generating image: {e}")
