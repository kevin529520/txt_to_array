import matplotlib.pyplot as plt
import numpy as np
# 打开文本文件并读取所有行
with open('t=32_x=0.1_r=0.001_zdrop=0.001+0.061_zk+0.06_pure_data.txt', 'r') as file:
    lines = file.readlines()

# 创建一个空数组来存储转换后的数据
data = []

# 遍历每一行并将其分割成一系列的值
for line in lines:
    values = line.split()
    data.append(values)

data_float = []
for row in data:
    # 将每一行中的字符串转换为浮点数
    row_float = [float(val) for val in row]
    # 删除第一列和第五列
    row_float.pop(0)
    row_float.pop(-1)
    # 将小于0.5的行删除
    if row_float[2] >= 0.1 and row_float[1] >= 0:
        data_float.append(row_float)

# 将包含浮点数的列表转换为NumPy数组
data_array = np.array(data_float)


# 绘制散点图
plt.scatter(data_array[:, 0], data_array[:, 1],s=5)
# 设置x轴和y轴的标签和标题
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter plot of x and y')
# 显示图形
plt.show()
# 打印出NumPy数组的形状和数据类型
print("Data array shape:", data_array.shape)
print("Data array dtype:", data_array.dtype)
# 输出转换后的数据
print(data)