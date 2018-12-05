#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 12:49:11 2018

@author: lilywang
"""

import tkinter as tk

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title = 'ChitChat'
        self.root.configure(width = 400, height = 500, background = '#ffe6f2')
        
        self.photo = tk.PhotoImage(file = '/Users/lilywang/Desktop/sailormoon.gif')
        
        self.label1 = tk.Label(self.root, text = 'Love is amazing')
        self.label1.pack(side='left')
        self.label = tk.Label(self.root, image = self.photo)
        self.label.pack(side='left')
        
        self.root.mainloop()




mygui = GUI()        