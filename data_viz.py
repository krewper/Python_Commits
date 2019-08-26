import pandas as pd 
import matplotlib.pyplot as plt 
  
# create 2D array
data = [['E001', 'M', 34, 123, 'Normal', 234], 
        ['E002', 'F', 40, 114, 'Overweight', 159], 
        ['E003', 'F', 37, 135, 'Obesity', 169], 
        ['E004', 'M', 30, 139, 'Underweight', 189], 
        ['E005', 'F', 44, 117, 'Underweight', 487], 
        ['E006', 'M', 36, 121, 'Normal', 80], 
        ['E007', 'M', 32, 133, 'Obesity', 124], 
        ['E008', 'F', 26, 140, 'Normal', 78], 
        ['E009', 'M', 32, 133, 'Normal', 240], 
        ['E010', 'M', 36, 133, 'Underweight', 700] ] 
  

df = pd.DataFrame(data, columns = ['EMPID', 'Gender',  
                                    'Age', 'Sales', 
                                    'BMI', 'Income'] ) 
  
 
df.hist() 
  
#printing plot of the data 
plt.show() 