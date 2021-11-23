import matplotlib.pyplot as plt
import numpy as np

# 一些全局变量
FontSize = 10  # 字体大小
dpi = 240  # 画质
lw = 0.5  # 线宽
ms = 1  # 标记（点）的大小


def init_fig(fig_size=(6, 3)):
    """
    初始化：设置图片大小(有默认大小)，并设置画质
    """
    plt.close()
    plt.figure(figsize=fig_size, dpi=dpi)


def add_fig(xl, yl):
    """
    设置图片网格
    设置xy轴标签，字体大小
    设置xy轴上刻度字体大小，以及y轴旋转
    """
    plt.grid(ls="--", linewidth=lw)
    plt.xlabel(xl, fontsize=FontSize)
    plt.ylabel(yl, fontsize=FontSize)
    plt.xticks(fontsize=FontSize)
    plt.yticks(fontsize=FontSize, rotation=90)


def set_legend():
    """
    设置图例样式：字体，边框，列数
    """
    plt.legend(fontsize=FontSize, frameon=False, ncol=2)


def save_fig(filename):
    """
    保存图片，并去除白边，已经清晰度
    :param filename:
    :return:
    """
    plt.savefig("../Picture/" + filename + ".png", bbox_inches='tight', dpi=dpi)


if __name__ == "__main__":
    """
    效果测试
    """
    init_fig()
    x = np.arange(-6, 6, 0.2)
    plt.plot(x, np.sin(x), linewidth=lw, label="sin x")
    plt.plot(x, np.cos(x), linewidth=lw, label="cos x")
    add_fig("X轴", "Y轴")
    set_legend()

    plt.show()
