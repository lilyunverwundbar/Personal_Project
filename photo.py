#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 19:42:36 2018

@author: lilywang
"""

import tkinter 
#import tkinter.messagebox
main_window = tkinter.Tk()
main_window.title = 'ChiChat'

# a little more than width and height of image
w = 520
h = 320
x = 80
y = 100
#use width x height + x_offset +y_offset
main_window.geometry("%dx%d+%d+%d" % (w, h, x, y))

gif = tkinter.PhotoImage(file = '/Users/lilywang/Desktop/haoran.gif')
canvas = tkinter.Canvas(bg = 'black')
canvas.pack(side = 'top', fill = 'both', expand = 'no')
canvas.create_image(10,10,image=gif, anchor = 'nw')

main_window.mainloop()

