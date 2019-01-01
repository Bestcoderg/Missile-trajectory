# -*- coding: utf-8 -*-

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation
from matplotlib.font_manager import FontProperties
import math

#创建一个fig对象，自定义fig的尺寸
fig=plt.figure(figsize=(30,35))
#划分fig并且选择一个子图给ax变量
ax=fig.add_subplot(1,1,1)
#用Basemap（）创建一个地图实例m,
m = Basemap(projection='mill',llcrnrlat=0,urcrnrlat=50,llcrnrlon=100,urcrnrlon=160)
# m = Basemap(projection = 'ortho', lat_0 = 0, lon_0 = 125)
#绘制海岸线
m.drawcoastlines()
# 绘制国家，linewidth表示国界线的粗细值
m.drawcountries(linewidth=2)
#绘制河流
m.drawrivers()
zstux,zstuy = 30.32 , 120.16
ax,ay = 13.27 , 144.47

#绘制经线和纬线
m.drawparallels(np.arange(10,90,20),labels=[1,1,0,1])
m.drawmeridians(np.arange(-180,180,30),labels=[1,1,0,1])
#绘制两个城市的连接线
m.drawgreatcircle(zstuy,zstux,ay,ax,linewidth=4,color='r')
#将地图加上去
m.etopo()
plt.title(u'Missile launch trajectory (2D)')



# --------------------------------
fig2=plt.figure(figsize=(30,35))
ax2=fig2.add_subplot(1,1,1)
# m = Basemap(projection='mill',llcrnrlat=0,urcrnrlat=50,llcrnrlon=100,urcrnrlon=160)
m2 = Basemap(projection = 'ortho', lat_0 = 0, lon_0 = 125)
m2.drawcoastlines()
m2.drawcountries(linewidth=2)
m2.drawrivers()

#绘制经线和纬线
m2.drawparallels(np.arange(10,90,20),labels=[1,1,0,1])
m2.drawmeridians(np.arange(-180,180,30),labels=[1,1,0,1])
#绘制两个城市的连接线
m2.drawgreatcircle(zstuy,zstux,ay,ax,linewidth=4,color='r')
#将地图加上去
m2.etopo()
plt.title(u'Missile launch trajectory (3D)')

# --------------------------------
EARTH_REDIUS = 6378.137
pi = 3.1415926
# 算弧度
def rad(d):
    return d * pi / 180.0
# 算两个地点之间的距离
def getDistance(lat1, lng1, lat2, lng2):
    radLat1 = rad(lat1)
    radLat2 = rad(lat2)
    a = radLat1 - radLat2
    b = rad(lng1) - rad(lng2)
    s = 2 * math.sin(math.sqrt(math.pow(math.sin(a/2), 2) + math.cos(radLat1) * math.cos(radLat2) * math.pow(math.sin(b/2), 2)))
    s = s * EARTH_REDIUS
    return s

dis = getDistance(zstux,zstuy,ax,ay)
print dis
# --------------------------------


g = 9.8
fig = plt.figure()
ax= fig.add_subplot(111)
ax.set_aspect('equal')
# 用来画轨迹的list
lx = []
ly = []

# 点的位置
def get_intervals(u, theta):
    intervals = []
    start = 0
    interval = 0.07
    while start < t_flight:
        intervals.append(start)
        start = start + interval
    print(interval)
    return intervals

# 生成器
def update(t):
    x = u*math.cos(theta_radians)*t
    y = u*math.sin(theta_radians)*t - 0.5*g*t*t
    circle.center = x, y
    lx.append(x)
    ly.append(y)

    plt.plot(lx, ly)  # 画出正常点的线
    return circle


def generate():
    for t in intervals:
        yield t


#角度
theta = 60
theta_radians = math.radians(theta)
#初速度
u = math.sqrt((dis*g)/(2*math.sin(theta_radians)*math.cos(theta_radians)))
print u

t_flight = 2*u*math.sin(theta_radians)/g
intervals = get_intervals(u, theta_radians)

xmin = 0

xmax = u*math.cos(theta_radians)*intervals[-1]
ymin = 0
t_max = u*math.sin(theta_radians)/g

ymax = u*math.sin(theta)*t_max - 0.5*g*t_max**2
ymax =xmax

ax = plt.axes(xlim=(xmin, xmax), ylim=(ymin, ymax))

circle = plt.Circle((xmin, ymin), 2)

ax.add_patch(circle)

anim = animation.FuncAnimation(fig, update,frames = generate , interval=100)
anim.save(u'/home/g/桌面/sin_dot.gif', writer='imagemagick', fps=30)

plt.title(u'Missile launch trajectory')
plt.xlabel(u'Horizontal distance')
plt.ylabel(u'Missile operational altitude(km)')


plt.show()