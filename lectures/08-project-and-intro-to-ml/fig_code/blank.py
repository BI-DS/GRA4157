from pylab import *
from IPython import embed

data = array([[1,1], [1,0], [0.4,0.8], [2,5], [2,4], [2.2,4.6]])     # input numbers x,y
target = array([0,0,0,1,1,1])                                        # output from x,y
colors = array(['blue', 'red'])                                     

p_pred = array([1.75, 2])                                            # new point to predict. Should output be 0 or 1

#print(norm(data-p_pred,axis=1))                                      # compute distance to data points

def distance(p0, P1):
    M = (p0 - P1)**2                                                 # can in theory implement any distance function
    return sqrt(sum(M, axis=1))

d = distance(p_pred,data)

idx = argsort(d)                                                     # sort points according to distance as indices
s_targ = target[idx]                                                 # corresponding predictions
n = 3                                                                # choose the number of votes
s_targ = s_targ[:n]                                                  # select n nearest neighbors

vote = bincount(s_targ)                                              # see the output among neighbors
pred = argmax(vote)                                                  # choose most common output among neighbors

print("input: ", p_pred, "predicted output: ", pred)

