#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 09:36:43 2018

@author: jenniferke
"""
import chat_client_class as cc
from tkinter import *
import time
import random
import threading


class GUI:
    def __init__(self):
        self.name = '' #name for the client logged in
        #CREATE WINDOW
        self.t = Tk()
        self.t.title('Chat Window')
        #forbid the user to adjust the window size
        self.t.resizable(0,0)
    
  
    
    
        #CREATE FRAME
        #the fisrt colomn
        '''self.frmA1 = Frame(width=180, height=460, bg='white')
        self.frmA2 = Frame(width=180, height=30, bg='green')'''
    
        #the second colomn
        self.frmB1 = Frame(width=330, height=320,bg="white")
        self.frmB2 = Frame(width=330, height=150,bg="white")
        self.frmB3 = Frame(width=330, height=30,bg="white")
    
        #the third colomn
        '''self.frmC1 = Frame(width=180, height=460, bg='white')
        self.frmC2 = Frame(width=180, height=30, bg='green')'''
    
    
    
        #CREATE WIDGET
        #1. text widget
        self.txtMsgList = Text(self.frmB1)
        # set feature
        self.txtMsgList.tag_config('greencolor', foreground='#008C00')
    
        self.sent_photo = PhotoImage(file='/Users/lilywang/Desktop/sailormoon.gif') 
       
    
   
        self.txtMsg = Text(self.frmB2)
    

        # bind event
    
        self.txtMsg.bind("<KeyPress-Return>", self.sendMsgEvent)
    
    
        #2. botton widget
        self.btnSend = Button(self.frmB3, text='SEND', width = 17,cursor='heart', command=self.sendMsg)
        self.emo_btn = Button(self.frmB3,justify = LEFT,command=self.sendImg)
        self.emo_pic = PhotoImage(file='/Users/lilywang/Desktop/Personal_Project/emoji_button.gif')
        self.emo_btn.config(image = self.emo_pic)
        self.btnCancel = Button(self.frmB3, text='CANCEL', width = 17,cursor='shuttle', command=self.cancelMsg)
    
   



# Window Setting
        '''self.frmA1.grid(row=0, column=0)
        self.frmA2.grid(row=3, column=0)'''

        self.frmB1.grid(row=0, column=1, columnspan=1)
        self.frmB2.grid(row=1, column=1, columnspan=1)
        self.frmB3.grid(row=2, column=1, columnspan=1)
  
        '''self.frmC1.grid(row=0, column=2)
        self.frmC2.grid(row=3, column=2)
'''
# Fix the size
        '''self.frmA1.grid_propagate(0)
        self.frmA2.grid_propagate(0)'''

  
        self.frmB1.grid_propagate(0)
        self.frmB2.grid_propagate(0)
        self.frmB3.grid_propagate(0)
  
        '''self.frmC1.grid_propagate(0)
        self.frmC2.grid_propagate(0)'''


# Widget Setting
        self.btnSend.grid(row=0, column=0)
        self.emo_btn.grid(row=0,column=1)
        self.btnCancel.grid(row=0, column=2)
        

        self.txtMsgList.grid()
        self.txtMsg.grid()

# main loop
        self.t.mainloop()

    def set_name(self,name):
        self.name.set(name)
        
    def sendMsg(self):
        #sending message
        self.strMsg = self.name + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n'
        self.txtMsgList.insert(END, self.strMsg, 'greencolor')
        self.txtMsgList.insert(END, self.txtMsg.get('0.0', END))
        self.txtMsg.delete('0.0', END)
    
    def sendImg(self):
        self.strMsg = self.name + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n'
        self.txtMsgList.insert(END, self.strMsg, 'greencolor')
        self.txtMsgList.image_create(END, image = self.sent_photo)
        
    def cancelMsg(self):
        #cancel message
        self.txtMsg.delete("0.0", END)
    
    def sendMsgEvent(self,event):
        #send message
        if event.keysym == "Return":  
            #send message by pressing "return"
            self.sendMsg()


'''class Login:
    def __init__(self):
        self.window = Tk()
        self.window.title('Login')
        self.window.configure(width=100,height=20)
        
        self.label = Label(self.window, text = 'Enter your name')
        self.label.grid(row = 0,column = 0)
        
        self.name_entry = Entry(self.window,width=18)
        self.name_entry.grid(row = 0, column = 1)
        
        self.conf_btn = Button(self.window, text = 'Confirm',command = self.chat_and_close_login)
        self.conf_btn.grid(row=1,column=1)
        
        
        self.name = StringVar()
        self.window.mainloop()
    def chat_and_close_login(self):
        self.name.set(self.name_entry.get())
        self.window.destroy
        self.mygui = GUI()
        self.mygui.set_name(self.name)'''
        
if __name__ == '__main__':
    #login = Login()
    mygui = GUI()
    
    



                          
                          
    
    
