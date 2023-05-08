import numpy as np
import os
from PIL import Image
import plotly.graph_objs as go
# 创建初始帧
fig = go.Figure()
i=1
# 遍历所有bmp图片，创建动画帧
frames = []
# 打开文本文件并读取所有行
folder_path = './data/'
for filename in sorted(os.listdir(folder_path)):
    if not filename.endswith('.txt'):
        continue
    #with open(filename, 'r') as file:
    with open(os.path.join(folder_path, filename), 'r') as file:
        lines = file.readlines()

    # 创建一个空数组来存储转换后的数据
    data = []
    print(i)
    i=i+1
    print(filename)
    # 遍历每一行并将其分割成一系列的值
    for line in lines:
            # 跳过空行
        # if not line.strip():
        #     continue
        values = line.split()
        data.append(values)
    print('data')
    print(len(data))
    data_float = []
    for row in data:
        # 将每一行中的字符串转换为浮点数
        # if not values[0].isdigit():
        #     continue
        row_float = [float(val) for val in row]
        # if len(row_float) < 3:
        #     continue
        # # 删除第一列和第五列
        row_float.pop(0)
        row_float.pop(-1)
        # 将小于0.5的行删除
        if row_float[2] >= 0.1 and row_float[1] >= 0:
            data_float.append(row_float)

    # 将包含浮点数的列表转换为NumPy数组
    data_array = np.array(data_float)
    print(data_array)

    trace = go.Scatter(x=data_array[:,0], y=data_array[:,1], mode='markers', marker=dict(size=5))
    fig.add_trace(trace)
    # frame = go.Frame(data=[trace], name=filename)
    # frames.append(frame)
fig.data[10].visible = True#图形中第十条轮廓线的可见性设置为 True

# Create and add slider
steps = []
for i in range(len(fig.data)):#step["args"][0]是args列表的第一个元素，是一个字典，该字典包含了键"visible"
    step = dict(
        method="update",
        args=[{"visible": [False] * len(fig.data)},  #【0，0，0，0，0，0，0，0，0，0】
              {"title": "Slider switched to time: " + str(16+2*i)+"/s"}],  # layout attribute
    )
    step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"args列表有两个字典，
    #第一个字典的键是"visible"，值是一个长度为fig.data长度的数组，
    steps.append(step)

sliders = [dict(
    active=0,#默认情况下滑块会显示第10条轮廓线。
    currentvalue={"prefix": "time/s: "},
    pad={"t": 50},#标题要从滑块的顶部下移50个像素
    steps=steps
)]

fig.update_layout(
    sliders=sliders
)

fig.show()