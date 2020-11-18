from binomial import binomial_iter
import matplotlib.pyplot as plt
import numpy as np


def bezier(points, t):
    n = len(points) - 1
    
    r = [0, 0]

    for i, b in enumerate(binomial_iter(n)):
        r[0] += (b * ((1.0 - t) ** (n - i)) * (t ** i)) * points[i][0]
        r[1] += (b * ((1.0 - t) ** (n - i)) * (t ** i)) * points[i][1]

    return r



if __name__ == "__main__":
    #points = [ (110,150), (25,190), (210,250), (210,30) ]
    points = [ (0, 0), (1, 0), 
               (0, 0), (1, 1), 
               (0, 0), (0, 1), 
               (0, 0), (-1, 1), 
               (0, 0), (-1, 0), 
               (0, 0), (-1, -1), 
               (0, 0), (0, -1), 
               (0, 0), (1, -1) ]

    x = []
    y = []
    
    for t in np.linspace(0, 1, 100):
        p = bezier(points, t)
        x.append(p[0])
        y.append(p[1])
    
    plt.plot(x, y)
    plt.show()
