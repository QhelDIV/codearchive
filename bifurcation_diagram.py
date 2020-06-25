import matplotlib.pyplot as plt
import numpy as np
r_range=np.linspace(3.5,4.0000,500)
pts = []
for r in r_range:
    x0 = np.random.rand(300)
    xn = x0
    for i in range(400):
        xn = r*xn*(1-xn)
    pts.append( np.stack([np.ones_like(xn)*r,xn],axis=-1) )
pts = np.concatenate(pts)
plt.scatter(pts[:,0],pts[:,1],s=.01,marker='o')

