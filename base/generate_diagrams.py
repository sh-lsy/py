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

if __name__ == "__main__":
    try:
        create_string_index_diagram()
    except ImportError:
        print("matplotlib not installed. Skipping image generation.")
    except Exception as e:
        print(f"Error generating image: {e}")
