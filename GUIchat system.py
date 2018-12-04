#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 09:36:43 2018

@author: jenniferke
"""

import tkinter
from tkinter import *
import time
import random
import threading


def main():

    
    def sendMsg():
        #sending message
        strMsg = "Me" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n'
        txtMsgList.insert(END, strMsg, 'greencolor')   
        txtMsgList.insert(END, txtMsg.get('0.0', END))
        txtMsg.delete('0.0', END)

    def cancelMsg():
        #cancel message
        txtMsg.delete("0.0", END)
    
    def sendMsgEvent(event):
        #send message
        if event.keysym == "Return":  
            #send message by pressing "return"
            sendMsg()

    #CREATE WINDOW
    t = Tk()
    t.title('Chat Window')
    #forbid the user to adjust the window size
    t.resizable(0,0)
    
  
    
    
    #CREATE FRAME
    #the fisrt colomn
    frmA1 = Frame(width=180, height=460, bg='white')
    frmA2 = Frame(width=180, height=30, bg='green')
    
    #the second colomn
    frmB1 = Frame(width=330, height=320,bg="white")
    frmB2 = Frame(width=330, height=150,bg="white")
    frmB3 = Frame(width=330, height=30,bg="white")
    
    #the third colomn
    frmC1 = Frame(width=180, height=460, bg='white')
    frmC2 = Frame(width=180, height=30, bg='green')
    
    
    
    #CREATE WIDGET
    #1. text widget
    txtMsgList = Text(frmB1)
    # set feature
    txtMsgList.tag_config('greencolor', foreground='#008C00')
                          
    txtMsg = Text(frmB2)
    # bind event
    txtMsg.bind("<KeyPress-Return>", sendMsgEvent)
    
    
    #2. botton widget
    btnSend = Button(frmB3, text='SEND', width = 17,cursor='heart', command=sendMsg)
    btnCancel = Button(frmB3, text='CANCEL', width = 17,cursor='shuttle', command=cancelMsg)
    
   



# Window Setting
    frmA1.grid(row=0, column=0)
    frmA2.grid(row=3, column=0)

    frmB1.grid(row=0, column=1, columnspan=1)
    frmB2.grid(row=1, column=1, columnspan=1)
    frmB3.grid(row=2, column=1, columnspan=1)
  
    frmC1.grid(row=0, column=2)
    frmC2.grid(row=3, column=2)

# Fix the size
    frmA1.grid_propagate(0)
    frmA2.grid_propagate(0)

  
    frmB1.grid_propagate(0)
    frmB2.grid_propagate(0)
    frmB3.grid_propagate(0)
  
    frmC1.grid_propagate(0)
    frmC2.grid_propagate(0)


# Widget Setting
    btnSend.grid(row=0, column=0)
    btnCancel.grid(row=0, column=1)

    txtMsgList.grid()
    txtMsg.grid()

# main loop
    t.mainloop()



if __name__ == '__main__':
    main()
    
    



                          
                          
    
    
