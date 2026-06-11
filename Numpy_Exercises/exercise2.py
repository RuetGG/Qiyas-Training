import numpy as np

sales = np.array([
    [120, 150, 180],
    [200, 220, 210],
    [170, 160, 190]
])
print("1:", sales[1,1])
print("2:", sales[:,0])
print("3:", sales[:,2])
print("4: ", sales[0,:])
print("5:", sales[1:,:])
print("6:", sales[:,1:])
