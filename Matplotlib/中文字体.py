import matplotlib.pyplot as plt
import matplotlib
print(matplotlib.matplotlib_fname())
plt.plot([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], '-og')
plt.text(1, 5, '1: 查询 matplotlibrc 文件路径')
plt.text(2, 4, '2: 通过\nmatplotlib.matplotlib_fname()\n查询路径')
plt.text(3, 3, '3: 查找\n#font.family:和\n#font.sans-serif:\n开头的这两行')
plt.text(4, 2, '4: 去掉这两行的 # 号，\n在font.sans-serif:后添加\nSimSun(宋),SimHei(黑)')
plt.text(5, 1, '5: 找axes.unicode_minus:True。\n去掉注释符号（#）,并将True改为False。')
plt.title('显示中文的方法！')
plt.xlabel('中文')
plt.ylabel('字体')
plt.show()
