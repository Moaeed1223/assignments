

#Name: Abdul Moaeed
#Email: abdul.moaeed66@myhunter.cuny.edu
#Date : March 11, 2023

import numpy as np

import matplotlib.pyplot as plt



imgName = input('Enter image name:')

value = float(input('Enter a number between 0 and 1:'))


ca = plt.imread(imgName)

count = 0


for row in range(ca.shape[0]):

    for col in range(ca.shape[1]):


        if (ca[row,col,0] < value) and (ca[row,col,1] < value) and (ca[row,col,2] < value):


            count = count + 1


percent = (count/(ca.shape[0]*ca.shape[1]))*100


print("Pixels with RGB values smaller than", value,  ":", count)

print("Percentage of pixels with RGB values below", value, ":", round(percent, 2), '%')


new = np.zeros(ca.shape)


for row in range(new.shape[0]):

    for col in range(new.shape[1]):


        new[row,col,0] = 1 - ca[row,col,0]

        new[row,col,1] = 1 - ca[row,col,1]

        new[row,col,2] = 1 - ca[row,col,2]


newName = imgName.split('.')[0] + '_complement.png'


plt.imsave(newName, new)
