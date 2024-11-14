# import numpy as np
# data = np.array([1,2,3,4])
# print(data)

# data=np.array([[1,2,3,4],[4,5,6,7]])
# print(data)

# import numpy as np
# data = np.arange(10,16,2) # 10-16的数据，步长为2
# print(data)

# import numpy as np
# #shape代表维度，比如我这里创建的就是5行三列的2维数组
# data=np.empty(shape=(5,3))
# print(data)

# import numpy as np
# #shape代表形状，比如我这里创建的就是5行三列的2维数组
# data=np.zeros(shape=(5,3))
# print(data)

# import numpy as np
# data1=[1,2,3,4,5]
# data2=[1,2,3,4,5]
# data=np.array([data1,data2])
# print("改之前的数组形状为:")
# print(data.shape)
# print(data)
# data=data.reshape((5,2))
# print("改之后的数组形状为:")
# print(data.shape)
# print(data)

# import matplotlib.pyplot as plt
# squares = [1, 4, 9, 16, 25]
# fig, ax = plt.subplots()
# ax.plot(squares)
# plt.show()

# from pathlib import Path
# path = Path('do_it.txt')
# print(path.read_text())
# path.write_text('ai')
list = []
for num in range(1,101):
    if num % 2 == 0:
        list.append(num)
print(list)
