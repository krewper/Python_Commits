import numpy as numpy
import cv2
import matplotlib.pyplot as pyplot

# img = cv2.cvtColor(img_raw, cv2.COLOR_BGR2RGB)
# plt.imshow(img_rgb)
def car_class:
    img = cv2.imread('car1.jpg')
    while True:
        cv2.imshow('mandrill',img)

    if cv2.waitKey(1) & 0xFF == 27:
         break

cv2.destroyAllWindows()    

if __name__ == "__main__":
    