import matplotlib.pyplot as plt
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
    frame = go.Frame(data=[trace], name=filename)
    frames.append(frame)


# 将所有帧加入到动画中
fig = go.Figure(frames=frames)
#animation = go.Animation(frames=frames)
fig.add_trace(frames[0].data[0])#frame里的data[0]
print(frames[0])
print(frames[0].data[0])
fig.layout.updatemenus = [dict(
    type='buttons',
    showactive=False,
    
    buttons=[dict(
        label='Play',
        method='animate',
        args=[None, {'frame': {'duration': 50000, 'redraw': True}, 'transition': {'duration': 10}, 
        'fromcurrent': True, 'frame': {'duration': 1000}}])]
        # args=[None,
        #       dict(frame=dict(duration=50),
        #            fromcurrent=True,
        #            transition=dict(duration=500),
        #            redraw=True)])]
                   )]
    # buttons = dict(label='Play', method='update', args=[None, {'frame': {'duration': 50, 'redraw': True}, 
    #                                                      'transition': {'duration': 500}, 
    #                                                      'fromcurrent': True, 'frame': {'duration': 50}}])
    #                                                      )]

# 设置坐标轴范围
#img = Image.open(os.path.join(folder_path, sorted(os.listdir(folder_path))[0]))
#fig.layout.xaxis.range = [0, img.width]
#fig.layout.yaxis.range = [0, img.height]

# 输出HTML文件
fig.update_layout(title='动图示例')
fig.show()
