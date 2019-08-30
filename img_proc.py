
# using matplotlib and numpy 
  
import matplotlib.image as img 
import numpy as npy 
  
# provide the location of image for reading  
m = img.imread("car1.jpg"); 
  
# determining the length of original image 
w, h = m.shape[:2]; 
  
# xNew and yNew are new width and 
# height of image required  
#after scaling 
xNew = int(w * 1 / 2); 
yNew = int(h * 1 / 2); 
  
# calculating the scaling factor  
# work for more than 2 pixel  
xScale = xNew/(w-1); 
yScale = yNew/(h-1); 
  
# using numpy taking a matrix of xNew 
# width and yNew height with  
# 4 attribute [alpha, B, G, B] values 
newImage = npy.zeros([xNew, yNew, 4]); 
  
for i in range(xNew-1): 
   for j in range(yNew-1): 
       newImage[i + 1, j + 1]= m[1 + int(i / xScale), 1 + int(j / yScale)] 
  
# Save the image after scaling  
img.imsave('scaled.jpg', newImage); 
