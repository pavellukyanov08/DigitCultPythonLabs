import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
# %matplotlib inline

# plt.plot([1, 2, 3, 4], [1, 4, 2, 3])
#
# # Создать рисунок
# plt.figure()
#
# # Задаем точки рисования
# plt.scatter([0, 0.25, 1], [0, 1, 0.5])
# # Вывод на экран
# plt.show()
#
#
# множества точек на одном графике
# plt.scatter([0, 1, 2, 3, 4 , 5], [0, 1, 2, 3, 4 , 5])
# plt.scatter([1, 2, 3, 1, 2 , 1], [2, 3, 4, 3, 4 , 4])
# plt.scatter([2, 3, 4, 3, 4 , 4], [1, 2, 3, 1, 2 , 1])
# plt.show()
#
#
# замкнутый многоугольник
# plt.figure()
# plt.plot([0, 0.25, 1, 0], [0, 1, 0.5, 0])
# plt.show()


# np.linspace(0, 1)
# np.linspace(0, 1, num=5)
# np.linspace(0, 1, num=5, endpoint=False)
# np.linspace(0, 1, num=5, endpoint=False, retstep=True)


# ломаная с использованием linspace с множеством точек
# x = np.linspace(0, 4*np.pi, 100)
# plt.figure()
# plt.plot(x, np.sin(x))
# plt.show()


# параметрическая линия x=x(t), y=y(t)
# t = np.linspace(0, 2*np.pi, 100)
# plt.figure(figsize=(4, 4))
# plt.plot(np.cos(t), np.sin(t))
# plt.show()


# фигура Лиссажу. 2 и 3
# t = np.linspace(0, 2*np.pi, 100)
# plt.figure(figsize=(4, 4))
# plt.plot(np.sin(2*t), np.cos(3*t))
# plt.show()


# фигура Лиссажу. 2 и 3
# t = np.linspace(0, 2*np.pi, 100)
# plt.figure(figsize=(4, 4))
# plt.plot(np.sin(8*t), np.cos(9*t))
# plt.show()


# # несколько кривых на одном графике. Линии
# x = np.linspace(0, 4*np.pi, 100)
# plt.figure()
# plt.plot(x, np.sin(x), 'r-')
# plt.plot(x, np.cos(x), 'b--')
# plt.show()


# несколько кривых на одном графике. Кружки и квадратики
# x = np.linspace(0, 1, 11)
# plt.figure()
# plt.plot(x, x**2, 'ro')
# plt.plot(x, 1 - x, 'gs')
# plt.show()


# x = np.linspace(0, 2*np.pi, 100)
# plt.figure(figsize=(10, 5))
# plt.plot(x, np.sin(x), linewidth=2, color='g', dashes=[8, 4], label=r'$\sin x$')
# plt.plot(x, np.cos(x), linewidth=2, color='r', dashes=[8, 4, 2,
# 4], label=r'$\cos x$')
# plt.axis([0, 2*np.pi, -1, 1])
# plt.xticks(np.linspace(0, 2*np.pi, 9), ('0',r'$\frac{1}{4}\pi$', r'$\frac{1}{2}\pi$', r'$\frac{3}{4}\pi$', r'$\pi$',
#     r'$\frac{5}{4}\pi$',
#     r'$\frac{3}{2}\pi$',
#     r'$\frac{7}{4}\pi$',
#     r'$2\pi$'),
# fontsize=20)
# plt.yticks(fontsize=12)
# plt.xlabel(r'$x$', fontsize=20)
# plt.ylabel(r'$y$', fontsize=20)
# plt.title(r'$\sin x$, $\cos x$', fontsize=20)
# plt.legend(fontsize=20, loc=0)
# plt.show()


# x = np.linspace(-2, 2, 100)
# plt.figure(figsize=(8, 8))
# plt.plot(x, x**3, linestyle='--', lw=2, label='$y=x^3$')
# plt.xlabel('x'), plt.ylabel('y')
# plt.legend()
# plt.title('График кубической функции')
# plt.grid(ls=':')
# plt.show()


# x = np.linspace(0, 1, 11)
# plt.figure(figsize=(4, 4))
# plt.plot(x, x, linestyle='', marker='<', markersize=20, markerfacecolor='#FF0000')
# plt.plot(x, x**2, linestyle='', marker='^', markersize=10, markerfacecolor='#00FF00')
# plt.plot(x, x**(1/2), linestyle='', marker='v', markersize=10, markerfacecolor='#0000FF')
# plt.plot(x, 1 - x, linestyle='', marker='+', markersize=10, markerfacecolor='#0F0F00')
# plt.plot(x, 1 - x**2, linestyle='', marker='x', markersize=10, markerfacecolor='#0F000F')
# plt.axis([-0.05, 1.05, -0.05, 1.05])
# plt.show()


# x = np.linspace(-5, 5, 100)
# plt.figure()
# plt.plot(x, np.exp(x) + np.exp(-x))
# plt.yscale('log')
# plt.yticks(fontsize=15)
# plt.show()


# x = np.logspace(-2, 2, 100)
# plt.figure()
# plt.plot(x, x + x**3)
# plt.xscale('log'), plt.xticks(fontsize=15)
# plt.yscale('log'), plt.yticks(fontsize=15)
# plt.show()


# спираль
# t = np.linspace(0, 4*np.pi, 100)
# plt.figure()
# plt.polar(t, t)
# plt.show()


# phi = np.linspace(0, 2*np.pi, 100)
# plt.figure()
# plt.polar(phi, np.sin(phi)**2)
# plt.show()


# x = np.linspace(-1, 1, 50)
# y = x
# z = np.outer(x, y)
# plt.figure(figsize=(5,5))
# plt.contour(x, y, z)
# plt.show()


# x = np.linspace(-1, 1, 50)
# y = x
# z = np.outer(x, y)
# plt.figure(figsize=(5,5))
# curves = plt.contour(x, y, z, np.linspace(-1, 1, 11))
# plt.clabel(curves)
# plt.title(r'$z=xy$', fontsize=20)
# plt.show()


# x = np.linspace(-1, 1, 50)
# y = x
# z = np.outer(x, y)
# plt.figure(figsize=(5, 5))
# plt.contourf(x, y, z, np.linspace(-1, 1, 11))
# plt.show()


# x = np.linspace(-1, 1, 50)
# y = x
# z = np.outer(x, y)
# plt.figure(figsize=(5, 5))
# plt.contourf(x, y, z, np.linspace(-1, 1, 11))
# plt.colorbar()
# plt.show()


# n = 256
# u = np.linspace(0, 1, n)
# x, y = np.meshgrid(u, u)
# z = np.zeros((n, n, 3))
# z[:, :, 0] = x
# z[:, :, 2] = y
# plt.figure()
# plt.imshow(z)
# plt.show()


# n = 28
# u = np.linspace(0, 1, n)
# x, y = np.meshgrid(u, u)
# plt.plot(x, y, marker='.', color='r', linestyle='none')
# plt.show()


# n = 256
# u = np.linspace(0, 1, n)
# x, y = np.meshgrid(u, u)
# plt.plot(x, y, marker='.', color='g', linestyle='none')
# plt.show()


# x, y = np.mgrid[-5*np.pi:5*np.pi:1000j, -5*np.pi:5*np.pi:1000j]
# z = np.sin(x) + np.cos(y)
# fig, ax = plt.subplots()
# ax.imshow(z)
# fig.set_figwidth(8) # ширина и
# fig.set_figheight(8) # высота "Figure"
# plt.show()


# t = np.linspace(0, 4*np.pi, 100)
# x = np.cos(t)
# y = np.sin(t)
# z = t/(4*np.pi)
# fig = plt.figure()
# ax = Axes3D(fig)
# ax.elev, ax.azim = 45, 30
# ax.plot(x, y, z)
# plt.show()


# t = np.linspace(0, 4*np.pi, 100)
# x = np.cos(t)
# y = np.sin(t)
# z = t/(4*np.pi)
# fig = plt.figure()
# ax = Axes3D(fig)
# ax.elev, ax.azim = 45, 30
# ax.plot(x, y, z)
# plt.show()


X = 10
N = 50
u = np.linspace(-X, X, N)
x, y = np.meshgrid(u, u)
r = np.sqrt(x**2 + y**2)
z = np.sin(r)/r
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(x, y, z, rstride=10, cstride=10)
plt.show()
