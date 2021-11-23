import matplotlib.pyplot as plt
import numpy as np
import matplotlib

if __name__ == "__main__":
    # 1-通过 matplotlib.matplotlib_fname() 查询 matplotlibrc 的 位置
    print(matplotlib.matplotlib_fname())

    # 2-修改字体，找到：#font.family与#font.sans-serif开头两行，去掉前面的#注释
    # 在第二个添加中文字体SimSun(宋),SimHei(黑)

    # 3-修改负号，找到axes.unicode_minus:True，去掉注释，改成False

    # 测试图中的中文显示
    plt.plot(np.arange(-4, 4, 0.1), np.sin(np.arange(-4, 4, 0.1)))
    plt.title('测试图中的中文')
    plt.xlabel('X轴')
    plt.ylabel('Y轴')
    plt.show()
