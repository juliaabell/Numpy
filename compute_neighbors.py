#This script will compute the ordered set of points closer to a point P1

import numpy as np

# this is P1
p1 = [0.2,0.4]

#this is a raw list of coordinates in the following format
#[p2x,p2y,p3x,p3y,p4x,p4y,p5x,p5y,...,pNx,pNy,]
points = [0.4,0.2,1.0,2.0,3.1,1.1,0.1,0.4]

#transform the list of points in a np.array having (2 lines of code)
# - a point of each row
# - the x coordinate of such point in the first column
# - the y coordinate of such point in the second column

array=np.array(points)
array=array.reshape(4,2)

#compute the square differences between p1 and points (1 line of code)

squared_array=(p1-array)**2

#sum the coordinate differences (1 line of code)

sum_array=np.sum(squared_array,axis=1)

#print the indices of points (from the nearest to p1 to the most far away)
#(1 line of code)

indicies_array=sum_array.argsort()
