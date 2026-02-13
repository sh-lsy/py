import matplotlib.pyplot as plt
import os

def create_class_object_diagram():
    """生成类与对象的关系图 (图纸 vs 房子)"""
    # 设置中文字体
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial']
    plt.rcParams['axes.unicode_minus'] = False

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # 1. 类 (Class) - 蓝图
    # 画一个像图纸的矩形
    bbox_blueprint = dict(boxstyle="square,pad=0.3", fc="#E3F2FD", ec="blue", lw=2, linestyle='--')
    ax.text(2.5, 6, "Class Cat (类)\n[图纸/模具]", ha='center', va='center', fontsize=16, weight='bold', bbox=bbox_blueprint)
    
    # 图纸内容
    content = "属性 (标签):\n - name\n - color\n\n方法 (行为):\n - speak()\n - eat()"
    ax.text(2.5, 4.5, content, ha='center', va='center', fontsize=12, style='italic', color='blue')

    # 2. 实例化过程 (Instantiation)
    ax.arrow(4.5, 6, 2, 0, head_width=0.2, head_length=0.2, fc='gray', ec='gray', lw=2)
    ax.text(5.5, 6.3, "实例化\n(造猫)", ha='center', va='center', fontsize=12, color='gray')

    # 3. 对象 (Objects) - 具体的实体
    # 对象 1
    bbox_obj1 = dict(boxstyle="round,pad=0.5", fc="#FFF9C4", ec="orange", lw=2)
    ax.text(8, 7, "Object: tom\n(具体的猫)", ha='center', va='center', fontsize=14, weight='bold', bbox=bbox_obj1)
    ax.text(8, 6.2, "name='汤姆'\ncolor='蓝色'", ha='center', va='top', fontsize=10)

    # 对象 2
    bbox_obj2 = dict(boxstyle="round,pad=0.5", fc="#FFF9C4", ec="orange", lw=2)
    ax.text(8, 4, "Object: jerry_cat\n(具体的猫)", ha='center', va='center', fontsize=14, weight='bold', bbox=bbox_obj2)
    ax.text(8, 3.2, "name='朋友'\ncolor='灰色'", ha='center', va='top', fontsize=10)

    # 连线
    ax.annotate("", xy=(6.8, 7), xytext=(4.5, 6), arrowprops=dict(arrowstyle="->", lw=2, color='gray', connectionstyle="arc3,rad=-0.2"))
    ax.annotate("", xy=(6.8, 4), xytext=(4.5, 6), arrowprops=dict(arrowstyle="->", lw=2, color='gray', connectionstyle="arc3,rad=0.2"))

    # 4. self 的解释
    ax.text(5, 1.5, "💡 核心概念: self", ha='center', va='center', fontsize=14, weight='bold', color='red')
    ax.text(5, 0.8, "在 tom 肚子里，self 就是 tom\n在 jerry_cat 肚子里，self 就是 jerry_cat", ha='center', va='center', fontsize=12, bbox=dict(fc='white', ec='red'))

    plt.title("类 (Class) vs 对象 (Object) 关系图", fontsize=18)
    plt.tight_layout()

    # 确保目录存在
    output_dir = os.path.join(os.path.dirname(__file__), 'assets')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_path = os.path.join(output_dir, 'class_vs_object.png')
    plt.savefig(output_path, dpi=100)
    print(f"Image saved to: {output_path}")

def create_encapsulation_diagram():
    """生成封装示意图 (ATM/保险柜)"""
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'Arial']
    plt.rcParams['axes.unicode_minus'] = False

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis('off')

    # 1. 对象边界 (Object Boundary) - 像个银行大楼
    bbox_building = dict(boxstyle="round,pad=1", fc="#F5F5F5", ec="gray", lw=3)
    ax.text(5, 4, " ", ha='center', va='center', bbox=bbox_building, fontsize=200) # 占位
    # 手动画个大框
    rect = plt.Rectangle((1, 1), 8, 6, fill=False, edgecolor='gray', linewidth=3, linestyle='--', zorder=0)
    ax.add_patch(rect)
    ax.text(5, 7.5, "BankAccount Object (银行账户对象)", ha='center', va='center', fontsize=16, weight='bold')

    # 2. 私有区域 (Private) - 保险柜
    bbox_safe = dict(boxstyle="round,pad=0.5", fc="#FFCDD2", ec="red", lw=2)
    ax.text(7, 4, "🔒 私有变量\nself.__balance\n(1000元)", ha='center', va='center', fontsize=14, bbox=bbox_safe)

    # 3. 公有区域 (Public) - 柜台窗口
    bbox_window = dict(boxstyle="round,pad=0.5", fc="#C8E6C9", ec="green", lw=2)
    ax.text(3, 5, "✅ 公开方法\ndeposit()", ha='center', va='center', fontsize=12, bbox=bbox_window)
    ax.text(3, 3, "✅ 公开方法\nwithdraw()", ha='center', va='center', fontsize=12, bbox=bbox_window)

    # 4. 外部访问者 (External User)
    ax.text(0.5, 4, "外部\n用户", ha='center', va='center', fontsize=14)

    # 5. 路径 (Path)
    # 正确路径: 用户 -> 方法 -> 变量
    ax.annotate("", xy=(2.3, 5), xytext=(0.8, 4.2), arrowprops=dict(arrowstyle="->", lw=2, color='green'))
    ax.annotate("", xy=(2.3, 3), xytext=(0.8, 3.8), arrowprops=dict(arrowstyle="->", lw=2, color='green'))
    
    ax.annotate("", xy=(6.2, 4.2), xytext=(3.7, 5), arrowprops=dict(arrowstyle="->", lw=2, color='green', linestyle='dashed'))
    ax.annotate("", xy=(6.2, 3.8), xytext=(3.7, 3), arrowprops=dict(arrowstyle="->", lw=2, color='green', linestyle='dashed'))
    
    ax.text(5, 5, "检查\n通过", ha='center', va='center', fontsize=10, color='green', bbox=dict(fc='white', ec='none'))

    # 错误路径: 用户 -> 变量
    ax.annotate("", xy=(6.2, 4), xytext=(0.8, 4), arrowprops=dict(arrowstyle="->", lw=2, color='red'))
    ax.text(3.5, 4, "❌ 禁止直接访问", ha='center', va='center', fontsize=12, color='red', weight='bold', bbox=dict(fc='white', ec='red'))

    plt.title("封装原理 (Encapsulation) 示意图", fontsize=18)
    plt.tight_layout()

    output_path = os.path.join(os.path.dirname(__file__), 'assets', 'encapsulation.png')
    plt.savefig(output_path, dpi=100)
    print(f"Image saved to: {output_path}")

if __name__ == "__main__":
    try:
        # create_class_object_diagram() # 已生成过，暂时注释
        create_encapsulation_diagram()
    except ImportError:
        print("matplotlib not installed. Skipping image generation.")
    except Exception as e:
        print(f"Error generating image: {e}")
