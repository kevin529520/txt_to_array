import numpy as np

# 读取文本文件并将其转换为数组
data = np.loadtxt("crosssection2.txt")
# 找到第三列中所有数字出现的次数
unique_vals, val_counts = np.unique(data[:, 2], return_counts=True)

# 将第三列中所有数字按大小进行排序
sorted_vals = np.argsort(data[:, 2])

# 记录已经处理过的数字
processed_vals = {}

# 将第三列中所有数字设置为对应的排名
for i in range(len(sorted_vals)):
    if data[sorted_vals[i], 2] not in processed_vals:
        rank = len(processed_vals) + 1
        processed_vals[data[sorted_vals[i], 2]] = rank
    data[sorted_vals[i], 2] = processed_vals[data[sorted_vals[i], 2]]


# 将第四列不为0的数设置成1
data[:, 3][data[:, 3] != 0] = 1

# 将数据保留两位有效数字
data = np.round(data, decimals=2)

# 将数组的前四列转换为一个矩阵
matrix = np.array(data[:, :4])

# 打印处理后的数据
print("Processed data:\n", data)
