import numpy as np

# 读取文本文件并将其转换为数组
data = np.loadtxt("crosssection2.txt")



# 将第四列不为0的数设置成1
data[:, 3][data[:, 3] != 0] = 1

# 将数据保留两位有效数字
data = np.round(data, decimals=2)

# 将数组的前四列转换为一个矩阵
matrix = np.array(data[:, :4])





# 打印矩阵的形状和内容
print("Matrix shape:", matrix.shape)
print("Matrix content:", matrix)





