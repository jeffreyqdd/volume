import matplotlib.pyplot as plt
import numpy as np
from math import *
from mpl_toolkits import mplot3d
import mpl_toolkits.mplot3d.axes3d as axes3d
import sys
import re
import usr_calculation as usr
import math_functions as m

command_arr = {
    "-quit" : 0,
    "-begin" : 1,
    "-history":2,
    "-disk" : 3,
    "-washer" : 4
}



def disk():
    tick = 10000
           
    print("Running disk function ... \n")
    
    orientation = "n"
    while orientation != "v" and orientation != "h":
        orientation = str(input("Axis of rotation: v or h? \n"))

    if orientation == "h":
        while True:
            try:
                f = m.convert(str(input("Enter equation: y= \n")))

                bounds = str(input("Enter bounds: a [space] b \n")).replace("pi", str(3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610454326648213393607260249141273))
                a,b = map(eval, bounds.split(" "))
                usr.disk_method([f], a, b, tick, 0, 'h')

                
                break
            except:
                a = input("An error occurred... do you wish to try again? y/n \n")
                if(a != "y"):
                    break
    if orientation == "v":
        while True:
            try:
                #original function
                f = m.convert(str(input("Enter equation y=\n")))
                #inverse
                g = m.convert(str(input("Enter inverse equation: y= \n")))

                bounds = str(input("Enter bounds: a [space] b\n")).replace("pi", str(3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610454326648213393607260249141273))
                a,b = map(eval, bounds.split(" "))

                usr.disk_method([f,g], a, b, tick, 0, 'v')

                break
        
            except:
                a = input("an error occurred... do you wish to try again? y/n \n")
                if(a != "y"):
                    break
    
    print("Returning to command...")


def washer():
    tick = 10000
    print("Running washer function ... \n")

    orientation = "h"

    print("\nPlease note that due to python capabilities, revolution about a vertical axis is not supported\n")

    while True:
        try:
            f1 = m.convert(str(input("Enter outer equation: y= \n")))
            f2 = m.convert(str(input("Enter inter equation: y= \n")))
            axis = float(str(input("Enter axis of rotation y= \n")).replace("pi", str(3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610454326648213393607260249141273)))

            bounds = str(input("Enter bounds: a [space] b \n")).replace("pi", str(3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610454326648213393607260249141273))
            a,b = map(eval, bounds.split(" "))


                        
            usr.washer_method_x([f1,f2], a, b, tick, axis, 'h')

                                
            break
                
        except:
            a = input("an error occured... do you wish to try again? y/n \n")
            if(a != "y"):
                break


            
    print("returning to command...")




def print_f(path):
    raw_file = open(path,'r')
    with raw_file as text:
        for line in text:
                print(line)

def execute(command):
    for pair in command_arr:
        if command == pair:
            return (command_arr[command])

    print("Command not found. Please try again.")
    return -1

def main():
    #intro
    print_f('texts/intro.txt')

    while True:
        command_id = execute(input())
        if command_id == 0:
            quit()
        if command_id == 1:
            print_f('texts/commands.txt')
        if command_id == 2:
            print_f('texts/readme.md')
        if command_id == 3:
            disk()
        if command_id == 4:
            washer()





if __name__ == '__main__':
    main()
