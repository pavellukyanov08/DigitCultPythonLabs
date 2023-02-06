import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline

plt.plot([1, 2, 3, 4], [1, 4, 2, 3])

# Создать рисунок
plt.figure()

# Задаем точки рисования
plt.scatter([0, 0.25, 1], [0, 1, 0.5])
# Вывод на экран
plt.show()


plt.scatter([0, 1, 2, 3, 4 , 5], [0, 1, 2, 3, 4 , 5])
plt.scatter([1, 2, 3, 1, 2 , 1], [2, 3, 4, 3, 4 , 4])
plt.scatter([2, 3, 4, 3, 4 , 4], [1, 2, 3, 1, 2 , 1])
plt.show()

plt.figure()
plt.plot([0, 0.25, 1, 0], [0, 1, 0.5, 0])
plt.show()


