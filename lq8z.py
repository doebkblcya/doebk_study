# import random
# from math import sin, cos, pi, log
# from tkinter import *

# CANVAS_WIDTH = 640
# CANVAS_HEIGHT = 480
# CANVAS_CENTER_X = CANVAS_WIDTH / 2
# CANVAS_CENTER_Y = CANVAS_HEIGHT / 2
# IMAGE_ENLARGE = 11
# # 设置颜色
# HEART_COLOR = "#FF99CC"


# def center_window(root, width, height):
#     screenwidth = root.winfo_screenwidth()  # 获取显示屏宽度

#     screenheight = root.winfo_screenheight()  # 获取显示屏高度

#     size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) /

#                             2, (screenheight - height) / 2)  # 设置窗口居中参数

#     root.geometry(size)  # 让窗口居中显示


# def heart_function(t, shrink_ratio: float = IMAGE_ENLARGE):
#     x = 16 * (sin(t) ** 3)

#     y = -(13 * cos(t) - 5 * cos(2 * t) - 2 * cos(3 * t) - cos(4 * t))

#     # 放大

#     x *= shrink_ratio
#     y *= shrink_ratio
#     # 移到画布中央

#     x += CANVAS_CENTER_X

#     y += CANVAS_CENTER_Y

#     return int(x), int(y)


# def scatter_inside(x, y, beta=0.15):
#     ratio_x = - beta * log(random.random())

#     ratio_y = - beta * log(random.random())

#     dx = ratio_x * (x - CANVAS_CENTER_X)

#     dy = ratio_y * (y - CANVAS_CENTER_Y)

#     return x - dx, y - dy


# def shrink(x, y, ratio):
#     force = -1 / (((x - CANVAS_CENTER_X) ** 2 +

#                    (y - CANVAS_CENTER_Y) ** 2) ** 0.6)

#     dx = ratio * force * (x - CANVAS_CENTER_X)

#     dy = ratio * force * (y - CANVAS_CENTER_Y)

#     return x - dx, y - dy


# def curve(p):
#     return 2 * (2 * sin(4 * p)) / (2 * pi)


# class Heart:

#     def __init__(self, generate_frame=20):

#         self._points = set()  # 原始爱心坐标集合

#         self._edge_diffusion_points = set()  # 边缘扩散效果点坐标集合

#         self._center_diffusion_points = set()  # 中心扩散效果点坐标集合

#         self.all_points = {}  # 每帧动态点坐标

#         self.build(2000)

#         self.random_halo = 1000

#         self.generate_frame = generate_frame

#         for frame in range(generate_frame):
#             self.calc(frame)

#     def build(self, number):

#         for _ in range(number):
#             t = random.uniform(0, 2 * pi)

#             x, y = heart_function(t)

#             self._points.add((x, y))

#         # 爱心内扩散

#         for _x, _y in list(self._points):

#             for _ in range(3):
#                 x, y = scatter_inside(_x, _y, 0.05)

#                 self._edge_diffusion_points.add((x, y))

#         # 爱心内再次扩散

#         point_list = list(self._points)

#         for _ in range(4000):
#             x, y = random.choice(point_list)

#             x, y = scatter_inside(x, y, 0.17)

#             self._center_diffusion_points.add((x, y))

#     @staticmethod
#     def calc_position(x, y, ratio):

#         force = 1 / (((x - CANVAS_CENTER_X) ** 2 +

#                       (y - CANVAS_CENTER_Y) ** 2) ** 0.520)

#         dx = ratio * force * (x - CANVAS_CENTER_X) + random.randint(-1, 1)

#         dy = ratio * force * (y - CANVAS_CENTER_Y) + random.randint(-1, 1)

#         return x - dx, y - dy

#     def calc(self, generate_frame):

#         ratio = 10 * curve(generate_frame / 10 * pi)

#         halo_radius = int(4 + 6 * (1 + curve(generate_frame / 10 * pi)))

#         halo_number = int(

#             3000 + 4000 * abs(curve(generate_frame / 10 * pi) ** 2))

#         all_points = []

#         # 光环

#         heart_halo_point = set()

#         for _ in range(halo_number):

#             t = random.uniform(0, 2 * pi)

#             x, y = heart_function(t, shrink_ratio=11.6)

#             x, y = shrink(x, y, halo_radius)

#             if (x, y) not in heart_halo_point:
#                 heart_halo_point.add((x, y))

#                 x += random.randint(-14, 14)

#                 y += random.randint(-14, 14)

#                 size = random.choice((1, 2, 2))

#                 all_points.append((x, y, size))

#         # 轮廓

#         for x, y in self._points:
#             x, y = self.calc_position(x, y, ratio)

#             size = random.randint(1, 3)

#             all_points.append((x, y, size))

#         # 内容

#         for x, y in self._edge_diffusion_points:
#             x, y = self.calc_position(x, y, ratio)

#             size = random.randint(1, 2)

#             all_points.append((x, y, size))

#         self.all_points[generate_frame] = all_points

#         for x, y in self._center_diffusion_points:
#             x, y = self.calc_position(x, y, ratio)

#             size = random.randint(1, 2)

#             all_points.append((x, y, size))

#         self.all_points[generate_frame] = all_points

#     def render(self, render_canvas, render_frame):

#         for x, y, size in self.all_points[render_frame % self.generate_frame]:
#             render_canvas.create_rectangle(

#                 x, y, x + size, y + size, width=0, fill=HEART_COLOR)


# def draw(main: Tk, render_canvas: Canvas, render_heart: Heart, render_frame=0):
#     render_canvas.delete('all')

#     render_heart.render(render_canvas, render_frame)

#     main.after(160, draw, main, render_canvas, render_heart, render_frame + 1)


# if __name__ == '__main__':
#     root = Tk()

#     root.title("爱心")

#     center_window(root, CANVAS_WIDTH, CANVAS_HEIGHT)  # 窗口居中显示

#     canvas = Canvas(root, bg='black', height=CANVAS_HEIGHT, width=CANVAS_WIDTH)

#     canvas.pack()

#     heart = Heart()

#     draw(root, canvas, heart)

#     Label(root, text="", bg="black", fg="#FF99CC", font="Helvetic 20 bold").place(

#         relx=.5, rely=.5, anchor=CENTER)

#     root.mainloop()

# import numpy as np
# import matplotlib.pyplot as plt
 
# # 定义爱心曲线方程
# def heart_curve(t):
#     x = 16 * np.power(np.sin(t), 3)
#     y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
#     return x, y
 
# # 生成曲线上的点
# t = np.linspace(0, 2*np.pi, 1000)
# x, y = heart_curve(t)
 
# # 绘制爱心图形
# plt.plot(x, y, color='red')
# plt.axis('equal')
# plt.title('高级爱心图形')
# plt.show()

# from tkinter import *
# from matplotlib import pyplot as plt
# from PIL import Image
# import random
# import math
# import numpy as np
# import os
# import colorsys
# import cv2
# from scipy.ndimage.filters import gaussian_filter
# from math import sin, cos, pi, log

# canvas_width = 600
# canvas_height = 600
# world_width = 0.05
# world_heigth = 0.05

# # 中间心的参数
# points = None
# fixed_point_size = 20000
# fixed_scale_range = (4, 4.3)
# min_scale = np.array([1.0, 1.0, 1.0]) * 0.9
# max_scale = np.array([1.0, 1.0, 1.0]) * 0.9
# min_heart_scale = -15
# max_heart_scale = 16

# # 外围随机心参数
# random_point_szie = 7000
# random_scale_range = (3.5, 3.9)
# random_point_maxvar = 0.2

# # 心算法参数
# mid_point_ignore = 0.95

# # 相机参数
# camera_close_plane = 0.1
# camera_position = np.array([0.0, -2.0, 0.0])

# # 点的颜色
# hue = 0.92
# color_strength = 255

# # 常用向量缓存
# zero_scale = np.array([0.0, 0.0, 0.0])
# unit_scale = np.array([1.0, 1.0, 1.0])
# color_white = np.array([255, 255, 255])
# axis_y = np.array([0.0, 1.0, 0.0])

# # 渲染缓存
# render_buffer = np.empty((canvas_width, canvas_height, 3), dtype=int)
# strength_buffer = np.empty((canvas_width, canvas_height), dtype=float)

# # 随机点文件缓存
# points_file = "temp.txt"

# # 渲染结果
# total_frames = 30
# output_dir = "./output"

# # 格式
# image_fmt = "jpg"


# def color(value):
#     digit = list(map(str, range(10))) + list("ABCDEF")
#     string = '#'
#     for i in value:
#         a1 = i // 16
#         a2 = i % 16
#         string += digit[a1] + digit[a2]
#     return string


# def heart_func(x, y, z, scale):
#     bscale = scale
#     bscale_half = bscale / 2
#     x = x * bscale - bscale_half
#     y = y * bscale - bscale_half
#     z = z * bscale - bscale_half
#     return (x ** 2 + 9 / 4 * (y ** 2) + z ** 2 - 1) ** 3 - (x ** 2) * (z ** 3) - 9 / 200 * (y ** 2) * (z ** 3)

# def lerp_vector(a, b, ratio):
#     result = a.copy()
#     for i in range(3):
#         result[i] = a[i] + (b[i] - a[i]) * ratio
#     return result


# def lerp_int(a, b, ratio):
#     return (int)(a + (b - a) * ratio)


# def lerp_float(a, b, ratio):
#     return (a + (b - a) * ratio)


# def distance(point):
#     return (point[0] ** 2 + point[1] ** 2 + point[2] ** 2) ** 0.5


# def dot(a, b):
#     return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


# def inside_rand(tense):
#     x = random.random()
#     y = -tense * math.log(x)
#     return y


# # 生成中间心
# def genPoints(pointCount, heartScales):
#     result = np.empty((pointCount, 3))
#     index = 0
#     while index < pointCount:
#         # 生成随机点
#         x = random.random()
#         y = random.random()
#         z = random.random()

#         # 扣掉心中间的点
#         mheartValue = heart_func(x, 0.5, z, heartScales[1])
#         mid_ignore = random.random()
#         if mheartValue < 0 and mid_ignore < mid_point_ignore:
#             continue

#         heartValue = heart_func(x, y, z, heartScales[0])
#         z_shrink = 0.01
#         sz = z - z_shrink
#         sheartValue = heart_func(x, y, sz, heartScales[1])

#         # 保留在心边上的点
#         if heartValue < 0 and sheartValue > 0:
#             result[index] = [x - 0.5, y - 0.5, z - 0.5]

#             # 向内扩散
#             len = 0.7
#             result[index] = result[index] * (1 - len * inside_rand(0.2))

#             # 重新赋予深度
#             newY = random.random() - 0.5
#             rheartValue = heart_func(result[index][0] + 0.5, newY + 0.5, result[index][2] + 0.5, heartScales[0])
#             if rheartValue > 0:
#                 continue
#             result[index][1] = newY

#             # 删掉肚脐眼
#             dist = distance(result[index])
#             if dist < 0.12:
#                 continue

#             index = index + 1
#             if index % 100 == 0:
#                 print("{ind} generated {per}%".format(ind=index, per=((index / pointCount) * 100)))

#     return result


# # 生成随机心
# def genRandPoints(pointCount, heartScales, maxVar, ratio):
#     result = np.empty((pointCount, 3))
#     index = 0
#     while index < pointCount:
#         x = random.random()
#         y = random.random()
#         z = random.random()
#         mheartValue = heart_func(x, 0.5, z, heartScales[1])
#         mid_ignore = random.random()
#         if mheartValue < 0 and mid_ignore < mid_point_ignore:
#             continue

#         heartValue = heart_func(x, y, z, heartScales[0])
#         sheartValue = heart_func(x, y, z, heartScales[1])

#         if heartValue < 0 and sheartValue > 0:
#             result[index] = [x - 0.5, y - 0.5, z - 0.5]
#             dist = distance(result[index])
#             if dist < 0.12:
#                 continue

#             len = 0.7
#             result[index] = result[index] * (1 - len * inside_rand(0.2))
#             index = index + 1

#     for i in range(pointCount):
#         var = maxVar * ratio
#         randScale = 1 + random.normalvariate(0, var)
#         result[i] = result[i] * randScale

#     return result


# # 世界坐标到相机本地坐标
# def world_2_cameraLocalSapce(world_point):
#     new_point = world_point.copy()
#     new_point[1] = new_point[1] + camera_position[1]
#     return new_point


# # 相机本地坐标到相机空间坐标
# def cameraLocal_2_cameraSpace(cameraLocalPoint):
#     depth = distance(cameraLocalPoint)
#     cx = cameraLocalPoint[0] * (camera_close_plane / cameraLocalPoint[1])
#     cz = -cameraLocalPoint[2] * (cx / cameraLocalPoint[0])
#     cameraLocalPoint[0] = cx
#     cameraLocalPoint[1] = cz
#     return cameraLocalPoint, depth


# # 相机空间坐标到屏幕坐标
# def camerSpace_2_screenSpace(cameraSpace):
#     x = cameraSpace[0]
#     y = cameraSpace[1]

#     # convert to view space
#     centerx = canvas_width / 2
#     centery = canvas_height / 2
#     ratiox = canvas_width / world_width
#     ratioy = canvas_height / world_heigth

#     viewx = centerx + x * ratiox
#     viewy = canvas_height - (centery + y * ratioy)

#     cameraSpace[0] = viewx
#     cameraSpace[1] = viewy
#     return cameraSpace.astype(int)


# # 绘制世界坐标下的点
# def draw_point(worldPoint):
#     cameraLocal = world_2_cameraLocalSapce(worldPoint)
#     cameraSpsace, depth = cameraLocal_2_cameraSpace(cameraLocal)
#     screeSpace = camerSpace_2_screenSpace(cameraSpsace)

#     draw_size = int(random.random() * 3 + 1)
#     draw_on_buffer(screeSpace, depth, draw_size)


# # 绘制到缓存上
# def draw_on_buffer(screenPos, depth, draw_size):
#     if draw_size == 0:
#         return
#     elif draw_size == 1:
#         draw_point_on_buffer(screenPos[0], screenPos[1], color_strength, depth)
#     elif draw_size == 2:
#         draw_point_on_buffer(screenPos[0], screenPos[1], color_strength, depth)
#         draw_point_on_buffer(screenPos[0] + 1, screenPos[1] + 1, color_strength, depth)
#     elif draw_size == 3:
#         draw_point_on_buffer(screenPos[0], screenPos[1], color_strength, depth)
#         draw_point_on_buffer(screenPos[0] + 1, screenPos[1] + 1, color_strength, depth)
#         draw_point_on_buffer(screenPos[0] + 1, screenPos[1], color_strength, depth)
#     elif draw_size == 4:
#         draw_point_on_buffer(screenPos[0], screenPos[1], color_strength, depth)
#         draw_point_on_buffer(screenPos[0] + 1, screenPos[1], color_strength, depth)
#         draw_point_on_buffer(screenPos[0], screenPos[1] + 1, color_strength, depth)
#         draw_point_on_buffer(screenPos[0] + 1, screenPos[1] + 1, color_strength, depth)


# # 根据色调和颜色强度获取颜色
# def get_color(strength):
#     result = None
#     if strength >= 1:
#         result = colorsys.hsv_to_rgb(hue, 2 - strength, 1)
#     else:
#         result = colorsys.hsv_to_rgb(hue, 1, strength)
#     r = min(result[0] * 256, 255)
#     g = min(result[1] * 256, 255)
#     b = min(result[2] * 256, 255)
#     return np.array((r, g, b), dtype=int)


# # 可以根据深度做一些好玩的
# def draw_point_on_buffer(x, y, color, depth):
#     if x < 0 or x >= canvas_width or y < 0 or y >= canvas_height:
#         return

#     # 混合
#     strength = float(color) / 255
#     strength_buffer[x, y] = strength_buffer[x, y] + strength


# # 绘制缓存
# def draw_buffer_on_canvas(output=None):
#     render_buffer.fill(0)
#     for i in range(render_buffer.shape[0]):
#         for j in range(render_buffer.shape[1]):
#             render_buffer[i, j] = get_color(strength_buffer[i, j])
#     im = Image.fromarray(np.uint8(render_buffer))
#     im = im.rotate(-90)
#     if output is None:
#         plt.imshow(im)
#         plt.show()
#     else:
#         im.save(output)


# def paint_heart(ratio, randratio, outputFile=None):
#     global strength_buffer
#     global render_buffer
#     global points

#     # 清空缓存
#     strength_buffer.fill(0)

#     for i in range(fixed_point_size):
#         # 缩放
#         point = points[i] * lerp_vector(min_scale, max_scale, ratio)

#         # 球型场
#         dist = distance(point)
#         radius = 0.4
#         sphere_scale = radius / dist
#         point = point * lerp_float(0.9, sphere_scale, ratio * 0.3)

#         # 绘制
#         draw_point(point)

#     # 生成一组随机点
#     randPoints = genRandPoints(random_point_szie, random_scale_range, random_point_maxvar, randratio)
#     for i in range(random_point_szie):
#         # 绘制
#         draw_point(randPoints[i])

#     # 高斯模糊
#     for i in range(1):
#         strength_buffer = gaussian_filter(strength_buffer, sigma=0.8)

#     # 绘制缓存
#     draw_buffer_on_canvas(outputFile)


# def show_images():
#     img = None
#     for i in range(total_frames):
#         save_name = "{name}.{fmt}".format(name=i, fmt=image_fmt)
#         save_path = os.path.join(output_dir, save_name)
#         img = cv2.imread(save_path, cv2.IMREAD_ANYCOLOR)
#         cv2.imshow("Img", img)
#         cv2.waitKey(25)


# def gen_images():
#     global points

#     if not os.path.isdir(output_dir):
#         os.mkdir(output_dir)

#     # 尝试加载或生成中间心
#     if not os.path.exists(points_file):
#         print("未发现缓存点，重新生成中")
#         points = genPoints(fixed_point_size, fixed_scale_range)
#         np.savetxt(points_file, points)
#     else:
#         print("发现缓存文件，跳过生成")
#         points = np.loadtxt(points_file)

#     for i in range(total_frames):
#         print("正在处理图片... ", i)
#         frame_ratio = float(i) / (total_frames - 1)
#         frame_ratio = frame_ratio ** 2
#         ratio = math.sin(frame_ratio * math.pi) * 0.743144
#         randratio = math.sin(frame_ratio * math.pi * 2 + total_frames / 2)
#         save_name = "{name}.{fmt}".format(name=i, fmt=image_fmt)
#         save_path = os.path.join(output_dir, save_name)
#         paint_heart(ratio, randratio, save_path)
#         print("图片已保存至", save_path)


# if __name__ == "__main__":
#     gen_images()
#     while True:
#         show_images()

# height = 5
# stars = 1
# for i in range(height):
#     print((' ' * (height - i)) + ('*' * stars))
#     stars += 2
# print((' ' * height) + '|')

# import turtle as t  # as就是取个别名，后续调用的t都是turtle
# from turtle import *
# import random as r
# import time
 
# n = 100.0
# t.pensize(10)  # 修改画笔大小
# speed("fastest")  # 定义速度
# screensize(bg='black')  # 定义背景颜色，可以自己换颜色
# left(90)
# forward(3 * n)
# color("orange", "yellow")  # 定义最上端星星的颜色，外圈是orange，内部是yellow
# begin_fill()
# left(126)
 
# for i in range(5):  # 画五角星
#     forward(n / 5)
#     right(144)  # 五角星的角度
#     forward(n / 5)
#     left(72)  # 继续换角度
# end_fill()
# right(126)
 
 
# def drawlight():  # 定义画彩灯的方法
#     if r.randint(0, 30) == 0:  # 如果觉得彩灯太多，可以把取值范围加大一些，对应的灯就会少一些
#         color('tomato')  # 定义第一种颜色
#         circle(6)  # 定义彩灯大小
#     elif r.randint(0, 30) == 1:
#         color('orange')  # 定义第二种颜色
#         circle(3)  # 定义彩灯大小
#     else:
#         linewidth = 5
#         color('dark green')  # 其余的随机数情况下画空的树枝
 
 
# color("dark green")  # 定义树枝的颜色
# backward(n * 4.8)
 
 
# def tree(d, s):  # 开始画树
#     if d <= 0: return
#     forward(s)
#     tree(d - 1, s * .8)
#     right(120)
#     tree(d - 3, s * .5)
#     drawlight()  # 同时调用小彩灯的方法
#     right(120)
#     tree(d - 3, s * .5)
#     right(120)
#     backward(s)
 
 
# tree(15, n)
# backward(n / 2)
 
# for i in range(200):  # 循环画最底端的小装饰
#     a = 200 - 400 * r.random()
#     b = 10 - 20 * r.random()
#     up()
#     forward(b)
#     left(90)
#     forward(a)
#     down()
#     if r.randint(0, 1) == 0:
#         color('tomato')
#     else:
#         color('wheat')
#     circle(2)
#     up()
#     backward(a)
#     right(90)
#     backward(b)
 
# t.color("dark red", "red")  # 定义字体颜色
# t.write("Merry Christmas", align="center", font=("Comic Sans MS", 40, "bold"))  # 定义文字、位置、字体、大小
 
 
# def drawsnow():  # 定义画雪花的方法
#     t.ht()  # 隐藏笔头，ht=hideturtle
#     t.pensize(2)  # 定义笔头大小
#     for i in range(200):  # 画多少雪花
#         t.pencolor("white")  # 定义画笔颜色为白色，其实就是雪花为白色
#         t.pu()  # 提笔，pu=penup
#         t.setx(r.randint(-350, 350))  # 定义x坐标，随机从-350到350之间选择
#         t.sety(r.randint(-100, 350))  # 定义y坐标，注意雪花一般在地上不会落下，所以不会从太小的纵座轴开始
#         t.pd()  # 落笔，pd=pendown
#         dens = 6  # 雪花瓣数设为6
#         snowsize = r.randint(1, 10)  # 定义雪花大小
#         for j in range(dens):  # 就是6，那就是画5次，也就是一个雪花五角星
#             # t.forward(int(snowsize))  #int（）取整数
#             t.fd(int(snowsize))
#             t.backward(int(snowsize))
#             # t.bd(int(snowsize))  #注意没有bd=backward，但有fd=forward，小bug
#             t.right(int(360 / dens))  # 转动角度
 
 
# drawsnow()  # 调用画雪花的方法
# t.done()  # 完成,否则会直接关闭

# from turtle import *
# import time

# setup(500, 500, startx=None, starty=None)
# speed(0)
# pencolor("pink")
# pensize(10)
# penup()
# hideturtle()
# goto(0, 150)
# showturtle()
# pendown()
# shape(name="classic")
# # 1
# seth(-120)
# for i in range(10):
#     fd(12)
#     right(2)
# penup()
# goto(0, 150)
# seth(-60)
# pendown()
# for i in range(10):
#     fd(12)
#     left(2)
# seth(-150)
# penup()
# fd(10)
# pendown()
# for i in range(5):
#     fd(10)
#     right(15)
# seth(-150)
# penup()
# fd(8)
# pendown()
# for i in range(5):
#     fd(10)
#     right(15)
# seth(-155)
# penup()
# fd(5)
# pendown()
# for i in range(5):
#     fd(7)
#     right(15)
# # 2
# penup()
# goto(-55, 34)
# pendown()
# seth(-120)
# for i in range(10):
#     fd(8)
#     right(5)

# penup()
# goto(50, 35)
# seth(-60)
# pendown()
# for i in range(10):
#     fd(8)
#     left(5)
# seth(-120)
# penup()
# fd(10)
# seth(-145)
# pendown()
# for i in range(5):
#     fd(10)
#     right(15)
# penup()
# fd(10)
# seth(-145)
# pendown()
# for i in range(5):
#     fd(12)
#     right(15)
# penup()
# fd(8)
# seth(-145)
# pendown()
# for i in range(5):
#     fd(10)
#     right(15)
# penup()
# seth(-155)
# fd(8)
# pendown()
# for i in range(5):
#     fd(11)
#     right(15)
# # 3
# penup()
# goto(-100, -40)
# seth(-120)
# pendown()
# for i in range(10):
#     fd(6)
#     right(3)
# penup()
# goto(80, -39)
# seth(-50)
# pendown()
# for i in range(10):
#     fd(6)
#     left(3)
# seth(-155)
# penup()
# fd(10)
# pendown()
# for i in range(5):
#     fd(8)
#     right(10)
# penup()
# fd(8)
# seth(-145)
# pendown()
# for i in range(7):
#     fd(8)
#     right(10)
# penup()
# fd(8)
# seth(-145)
# pendown()
# for i in range(7):
#     fd(7)
#     right(10)
# penup()
# fd(8)
# seth(-145)
# pendown()
# for i in range(7):
#     fd(7)
#     right(10)
# penup()
# fd(8)
# seth(-140)
# pendown()
# for i in range(7):
#     fd(6)
#     right(10)

# # 4
# penup()
# goto(-120, -95)
# seth(-130)
# pendown()
# for i in range(7):
#     fd(10)
#     right(5)
# penup()
# goto(100, -95)
# seth(-50)
# pendown()
# for i in range(7):
#     fd(10)
#     left(5)
# penup()
# seth(-120)
# fd(10)
# seth(-155)
# pendown()
# for i in range(6):
#     fd(8)
#     right(10)
# penup()
# seth(-160)
# fd(10)
# seth(-155)
# pendown()
# for i in range(6):
#     fd(8)
#     right(10)
# penup()
# seth(-160)
# fd(10)
# seth(-155)
# pendown()
# for i in range(6):
#     fd(8)
#     right(10)
# penup()
# seth(-160)
# fd(10)
# seth(-160)
# pendown()
# for i in range(6):
#     fd(8)
#     right(10)
# penup()
# seth(-160)
# fd(10)
# seth(-160)
# pendown()
# for i in range(6):
#     fd(8)
#     right(10)
# penup()
# seth(-160)
# fd(10)
# seth(-165)
# pendown()
# for i in range(5):
#     fd(10)
#     right(11)
# # 5
# penup()
# goto(-70, -165)
# seth(-85)
# pendown()
# for i in range(3):
#     fd(5)
#     left(3)
# penup()
# goto(70, -165)
# seth(-95)
# pendown()
# for i in range(3):
#     fd(5)
#     right(3)
# seth(-170)
# penup()
# fd(10)
# pendown()
# pendown()
# for i in range(10):
#     fd(12)
#     right(2)
# # 6
# penup()
# goto(70, -165)
# pendown()
# seth(-90)
# pensize(8)
# pencolor("#de8891")
# circle(-20, 90)

# penup()
# goto(30, -185)
# pendown()
# seth(-180)
# pensize(8)
# pencolor("#de8891")
# fd(40)

# penup()
# goto(-5, -170)
# pendown()
# seth(-180)
# pensize(8)
# pencolor("#de8891")
# fd(35)


# def guest(x, y, z):
#     penup()
#     goto(x, y)
#     seth(-z)
#     pendown()
#     for angel in range(5):
#         fd(10)
#         right(10)


# def guet(x, y, z):
#     penup()
#     goto(x, y)
#     seth(-z)
#     pendown()
#     for angel in range(5):
#         fd(10)
#         left(10)


# def qu(x, y, z):
#     penup()
#     goto(x, y)
#     seth(-z)
#     pendown()
#     for angel in range(5):
#         fd(6)
#         right(10)
#     seth(-150)
#     fd(20)


# # 树枝
# guest(-70, -150, 160)
# guest(100, -150, 160)
# guet(110, -110, 50)
# guest(160, -140, 150)
# qu(80, -120, 180)
# guest(70, -85, 165)
# guest(-40, -85, 165)
# guet(90, -50, 50)
# guest(130, -80, 150)
# pencolor("pink")
# qu(-40, -60, 180)
# pencolor('#de8891')
# qu(80, -30, 180)
# pencolor("pink")
# qu(40, 10, 180)
# pencolor("#de8891")
# guest(-60, 30, 120)
# guest(-20, -20, 150)
# guet(45, 40, 60)
# guest(-30, 40, 170)
# guest(-30, 110, 115)
# guet(40, 90, 60)
# guest(80, 50, 160)
# pencolor("#de8891")


# def hdj(x, y):
#     penup()
#     goto(x, y)
#     seth(80)
#     pendown()
#     pensize(2)
#     circle(5)
#     seth(10)
#     fd(15)
#     seth(120)
#     fd(20)
#     seth(240)
#     fd(20)
#     seth(180)
#     fd(20)
#     seth(-60)
#     fd(20)
#     seth(50)
#     fd(20)
#     seth(-40)
#     fd(30)
#     seth(-130)
#     fd(5)
#     seth(135)
#     fd(30)
#     seth(-60)
#     fd(30)
#     seth(-150)
#     fd(6)
#     seth(110)
#     fd(30)


# def uit(x, y):
#     penup()
#     goto(x, y)
#     pendown()
#     pensize(2)
#     circle(5)
#     seth(-10)
#     fd(15)
#     seth(90)
#     fd(15)
#     seth(200)
#     fd(15)
#     seth(160)
#     fd(15)
#     seth(-90)
#     fd(15)
#     seth(10)
#     fd(15)
#     seth(-60)
#     fd(20)
#     seth(-180)
#     fd(5)
#     seth(110)
#     fd(20)
#     seth(-90)
#     fd(20)
#     seth(-180)
#     fd(6)
#     seth(70)
#     fd(15)
#     hideturtle()


# def yut(x, y, z):
#     penup()
#     goto(x, y)
#     pendown()
#     seth(z)
#     for po in range(5):
#         fd(4)
#         left(36)


# def ytu(x, y, z):
#     penup()
#     goto(x, y)
#     pendown()
#     seth(z)
#     for kk in range(5):
#         fd(4)
#         left(36)


# # 小蝴蝶结
# seth(0)
# uit(40, -160)
# hdj(-80, -120)
# yut(-67, -115, 120)
# yut(-86, -123, 150)
# hdj(40, -50)
# yut(52, -45, 130)
# yut(34, -55, 160)
# seth(0)
# uit(-20, -60)
# ytu(-4, -60, 100)
# ytu(-20, -60, 120)
# hdj(-30, 20)
# yut(-15, 25, 130)
# yut(-40, 20, 180)
# uit(30, 70)
# ytu(45, 70, 100)
# ytu(30, 70, 120)

# # 大蝴蝶结
# pencolor("#f799e6")
# pensize(5)
# penup()
# seth(0)
# goto(0, 150)
# pendown()
# circle(10)
# seth(-15)
# fd(40)
# seth(90)
# fd(40)
# seth(200)
# fd(40)
# seth(160)
# fd(40)
# seth(-90)
# fd(40)
# seth(15)
# fd(40)
# seth(-70)
# pencolor("#f799e6")
# pensize(4)
# fd(40)
# seth(-180)
# fd(10)
# seth(100)
# fd(40)
# seth(-100)
# fd(40)
# seth(-180)
# fd(10)
# seth(70)
# fd(40)
# penup()
# seth(0)
# goto(0, 130)
# pencolor("pink")
# pendown()


# def iou(x, y, z):
#     penup()
#     goto(x, y)
#     pencolor("#f799e6")
#     pendown()
#     seth(z)
#     for po in range(10):
#         fd(4)
#         left(18)


# seth(0)
# iou(35, 145, 100)
# iou(-7, 145, 110)
# pencolor("red")
# pensize(7)
# penup()
# goto(-35, 135)
# pendown()

# # 圣诞帽
# seth(-20)
# pensize(2)
# penup()
# goto(-30, -120)
# pencolor("black")
# pendown()
# fillcolor("red")
# fd(30)
# circle(4, 180)
# fd(30)
# circle(4, 180)
# penup()
# goto(-25, -115)
# seth(75)
# pendown()
# begin_fill()
# for i in range(5):
#     fd(6)
#     right(20)
# seth(-10)
# for i in range(5):
#     fd(8)
#     right(15)
# seth(145)
# for i in range(5):
#     fd(5)
#     left(2)
# seth(90)
# for i in range(5):
#     fd(1)
#     left(2)
# seth(-90)
# for i in range(4):
#     fd(4)
#     right(6)
# seth(161)
# fd(30)
# end_fill()
# pensize(1)
# pencolor("black")


# def koc(x, y, size):
#     pensize(2)
#     pencolor("black")
#     penup()
#     goto(x, y)
#     pendown()
#     begin_fill()
#     fillcolor("yellow")
#     for i in range(5):
#         left(72)
#         fd(size)
#         right(144)
#         fd(size)
#     end_fill()


# # 星星
# seth(-15)
# koc(-120, -70, 10)
# seth(10)
# koc(100, -20, 10)
# seth(-10)
# koc(10, 40, 10)
# seth(30)
# koc(-80, 60, 10)
# koc(100, -150, 10)
# koc(-140, -150, 10)
# koc(20, 120, 10)

# # 袜子
# seth(-20)
# pensize(2)
# penup()
# goto(-20, 80)
# pencolor("black")
# pendown()
# fillcolor("red")
# fd(25)
# circle(4, 180)
# fd(25)
# circle(4, 180)
# penup()
# goto(-15, 80)
# pendown()
# begin_fill()
# fillcolor("red")
# seth(-120)
# fd(20)
# seth(150)
# fd(5)
# circle(7, 180)
# fd(15)
# circle(5, 90)
# fd(30)
# seth(160)
# fd(18)
# end_fill()
# penup()
# seth(0)
# goto(100, -230)
# pendown()
# write("wocaonima", align="right", font=("Comic Sans MS", 24, "bold"))
# done()
