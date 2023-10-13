from pylab import *


data = array([[1,1], [1,0], [0.4,0.8], [2,5], [2,4], [2.2, 4.6]])

target = array([0,0,0,1,1,1])
colors = ['blue', 'red']



point_to_predict = array([1.75,2])

def distance(p0,p1):
    d = p1 - p0
    d_2 = sum(d**2, axis=1)
    return sqrt(d_2)

distances = distance(data, point_to_predict)

for i in range(len(data)):
    p = data[i]
    t = target[i]
    c = colors[t]
    plot(p[0], p[1], 'o', color=c)



def KNearest(data, target, point_to_predict, n_neighbors=3):
    distances = distance(data, point_to_predict)
    sorted_args = argsort(distances)
    closest_labels = target[sorted_args]
    valid_labels = closest_labels[:n_neighbors]
    
    vote = bincount(valid_labels)
    plot(point_to_predict[0], point_to_predict[1], 'o', color=colors[vote.argmax()], alpha=0.5)
    
    center = point_to_predict
    radius = (distances[sorted_args])[n_neighbors-1]
    t = linspace(0,2*pi, 501)
    plot(radius*cos(t) + center[0], radius*sin(t) + center[1], '--', color=colors[vote.argmax()])
    return colors[vote.argmax()]
    

print(KNearest(data, target, point_to_predict))

show()

