import matplotlib.pyplot as plt
import numpy as np
from math import *
from mpl_toolkits import mplot3d
import mpl_toolkits.mplot3d.axes3d as axes3d
import sys
import re
import math_functions as m

line_colors = ['red','blue','orange','grey','black','purple','yellow']
 


def plot3d(f,a,b,n,z,orientation):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d') 

    #processing data
    #have to put inverse function
    packed = m.graph_3d_x(f,a,b,n,z, orientation)
    #print(f,a,b,n,z)

    for func in packed:
        #plotting function
        ax.plot_surface(func[0], func[1], func[2], alpha = 0.2, color=line_colors[func[3]], label = func[4])
        ax.plot_wireframe(func[0], func[1], func[2], rstride=5, cstride=5, label = func[4], color = 'black', linewidth = 0.5, alpha = 0.5)

    if(orientation == 'h'):
        X = np.linspace(a,b,n)
        Y = np.linspace(z,z,n)
        Z = np.linspace(0,0,n)
        ax.plot(X,Y,Z, color = "black")
    else:

        X = np.linspace(0,0,n)
        Y = np.linspace(z,z,n)
        Z = np.linspace(a,b,n)
        ax.plot(X,Y,Z, color = "black")
        
    ax.set_xlabel('x axis')
    ax.set_ylabel('y axis')
    ax.set_zlabel('z axis')
    plt.show()
    plt.close()

def plot2d(f,a,b,n,z, orientation):
    
    
    packed = m.graph_x(f,a,b,n)

    for func in packed:
        plt.plot(func[0],func[1], label = func[2] ,color = line_colors[func[3]])
        

    #fill in in btwn area
    #very specific: either 2 equations around z, or one equation revolved around z

    if orientation == 'h':
        x = np.linspace(a,b,n)
        y = np.linspace(z,z,n)

        
        l1 = packed[0]
        l2 = [x,y]
        
        plt.plot(x,y, label = z, color = line_colors[packed[-1][3]+1])
    

    else:
        x = np.linspace(z,z,n)

        y = np.linspace(eval(f[0].replace("x",str(a))),eval(f[0].replace("x",str(b))),n)

        l1 = packed[0]
        l2 = [x,y]
        
        plt.plot(x,y, label = z, color = line_colors[packed[-1][3]+1])
        

        


        



    plt.grid(alpha=.4,linestyle='--')
    plt.legend()
    plt.show()
    plt.close()


#milestone!!! find area a function rotating about a line z, parallel to the x
#axis

#f = singular function, [a,b], step = n, z = line
def disk_method(f, a, b, n, z, orientation):
    if orientation == 'h':
        #2d -----------------------------------------
        #integral
        area_2d = m.integrate_x_z(f[0],a,b,n,z,8)
        print("2d area is:", round(area_2d,3))

        #plot
        plot2d(f,a,b,n,z, 'h')
        
        #3d -----------------------------------------
        #integral from a to b of r^2 times pi
        #square it
        rx = f[0]
        rx = "(" + rx + ")**2"

        #disk method
        area_3d = m.integrate_x_z(rx, a, b, n, z, 8) * pi
        print("3d area is:", round(area_3d,3), "or", str(round(area_3d / pi,3)) + " pi")

        plot3d(f, a, b, 30, z, 'h')
    
    else:
        #2d ----------------------------------------
        area_2d_inverse = m.integrate_x_z(f[1], a, b, n, z, 8)
        print("2d area is:", round(area_2d_inverse, 3))

        plot2d([f[0]], a, b, n, z, 'v')

        rx = f[1]
        rx = "(" + rx + ")**2"

        area_3d_inverse = m.integrate_x_z(rx, a, b, n, z, 8) * pi
        print("3d area is:", round(area_3d_inverse,3), "or", str(round(area_3d_inverse / pi,3)) + " pi")

        plot3d([f[1]], a, b, 30, z, 'v')


def washer_method_x(f,a,b,n,z,orientation):
    #2d -----------------------------------------
    #integral
    area_2d = m.integrate_x_z(f[0],a,b,n,z,8) - m.integrate_x_z(f[1],a,b,n,z,8)
                
    print("2d area is:", round(area_2d,3))
    #plot
    plot2d(f,a,b,n,z, 'h')
        
    #3d -----------------------------------------
    #integral from a to b of R^2 - r^2 times pi
    #square it
    Rx = f[0]
    rx = f[1]
        
    func = "(" + Rx + ")**2" + "-" + "(" + rx + ")**2"

    #disk method
    area_3d = m.integrate_x_z(func, a, b, n, z, 8) * pi

        
    print("3d area is:", round(area_3d,3), "or", str(round(area_3d / pi,3)) + " pi")

    plot3d(f, a, b, 50, z, 'h')

        
