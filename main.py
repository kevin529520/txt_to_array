# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # 读取.txt文件
    with open('crosssection.txt', 'r') as f:
        data = f.readlines()
    # 去除每行末尾的换行符
    data = [line.strip() for line in data]

    # 将数据解析为矩阵
    matrix = []
    for line in data:
        row = line.split(',')  # 假设数据中每行用逗号分隔
        row = ''.join([c for c in row if c != 'E'])  # 去除非数字、小数点和负号
        row = ''.join([c for c in row if c != '+'])  # 去除非数字、小数点和负号
        row = ''.join([c for c in row if c != '-'])  # 去除非数字、小数点和负号
        row = [float(i) for i in row]  # 将字符串转换为浮点数
        matrix.append(row)

    # 将矩阵转换为NumPy数组
    matrix = np.array(matrix)


    # 输出结果
    print(matrix)
    #print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
