import numpy as np
#these are used for visualization purposes, do not focus on this now
import matplotlib.pyplot as plt
import seaborn; seaborn.set() # Plot styling

N = 100
np.random.seed(5) #put a seed to the random function for reproducing results
X = np.random.random((N,2)) #create N random points
array=np.array(X).reshape(N,2)

#for each point in X compute the three points which are closer to it
#reuse the code developed in compute_neighbors.py


#store the final result in an array [N,3] (call it FINAL)
#- each row "i" contains the three indices of the points closer to point "i"

my_array=np.array([])
for points in array:
    squared_array=(points-X)**2
    sum_array=np.sum(squared_array,axis=1)
    indicies_array=sum_array.argsort()
    test=indicies_array[1:4]
    my_array=np.append(my_array,test)

final= my_array.reshape(100,3)  
FINAL=final.astype(int)

#---- Once the FINAL array is ready uncomment the following code and
# save the resulting image (uploading it on GitHub)

colors = ['black','red','green']
plt.scatter(X[:, 0], X[:, 1], s=100);
for i in range(FINAL.shape[0]):
  count=0
    for j in FINAL[i]:
        plt.plot(*zip(X[i], X[j]), color=colors[count])
        count = count+1
plt.show()

