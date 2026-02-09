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

if __name__ == "__main__":
    try:
        create_string_index_diagram()
        create_function_diagram()
    except ImportError:
        print("matplotlib not installed. Skipping image generation.")
    except Exception as e:
        print(f"Error generating image: {e}")
