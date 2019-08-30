import matplotlib.image as img
import numpy as npy

m = img.imread("car1.jpg")
w, h = m.shape[:2]

xNew = int(w * 1 / 4)
yNew = int(h * 1/ 4)
newImage = npy.zeros([xNew, yNew, 4])

print(w)
print(h)

for i in range(1, xNew):
    for j in range(1, yNew):
        newImage[i, j]= m[100 + i, 100 + j]
img.imsave('cropped.jpg', newImage)
