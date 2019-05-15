import matplotlib.pyplot as plt
import numpy as np
from math import *
from mpl_toolkits import mplot3d
import mpl_toolkits.mplot3d.axes3d as axes3d
import sys
import re
 

line_colors = ['red','blue','orange','grey','black','purple','yellow']

#f = function, a and b = bounds, n = steps btwn a and b, r rounding decimals
#integral in retrospect to line its bound: z
def integrate_x_z(f,a,b,n,z,r):
    #divide into equal sections
    step = float((b - a) / n)

    #initialize variable with area 0
    area = 0.0

    #single first term
    
    area += abs(eval(f.replace("x", str(a))) - z )
    #double middle terms
    #[a,b)
    for i in range(1,n):
        area += abs((eval(f.replace("x", str(a + i * step))) - z) * 2.0)


    #single last term
    area += abs(eval(f.replace("x", str(b))) - z)
    
    #1/2 * (b-a)/n
    area *= (b-a)/(2 * n)


    return abs(round(area,r))



def graph_x(f,a,b,n):
    
    count = 0
    output = []
    for function in f:
    
        x = np.linspace(a,b,n)
        fx = []

        for i in x:
            fx.append(eval(function.replace("x", str(i))))
    
        output.append([x, np.array(fx), function, count])

        count += 1

    return output



    


#just disk, rotating along a z value
def graph_3d_x(f, a, b, n, z, orientation):

    output = []

    u = np.linspace(a,b,n)
    v = np.linspace(0,2*pi,n)
    U,V = np.meshgrid(u,v)
        
    count = 0

    for function in f:
        
        fx = []
        for i in U:
            temp = []
            for j in i:
                temp.append(eval(function.replace("x",str(j))) - z)
                    
                        
        fx.append(temp)
            
        X = U
        Y = (np.array(fx))*np.cos(V) + z
        Z = (np.array(fx))*np.sin(V)
            

            
        if orientation == 'h':
            #pack
            output.append([X,Y,Z, count, function])
        elif orientation == 'v':
            output.append([Y,Z,X, count, function])
    
            

        count += 1

    return output



 
def convert(s):
    s = s.replace("^","**")

    s = s.replace("arcsin","asin")
    s = s.replace("arccos","acos")
    s = s.replace("arctan","atan")

    s = s.replace("csc","1/sin")
    s = s.replace("sec","1/cos")
    s = s.replace("cot","1/tan")
    

    return s
 
