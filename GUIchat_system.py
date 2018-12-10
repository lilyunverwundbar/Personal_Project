from tkinter import *
import time

class Login:
    def __init__(self):
        self.login_w = Tk()
        self.login_w.title('Login')
        #self.login_w.geometry('400x100')
        self.loginLabel = Label(self.login_w,text = 'Enter your name:')
        self.loginTxt = Text(self.login_w)
        self.login_btn = Button(self.login_w,height=20,width=60,text = 'confirm',command = self.login_and_get_name)
        self.loginLabel.grid(row=0,column=0)
        self.loginTxt.grid(row=0,column=1)
        self.login_btn.grid(row=1,column=1)
        #self.login_w.mainloop()
        self.name=''
    def login_and_get_name(self):
        self.name = self.loginTxt.get('1.0',END)
        #self.login_w.destroy()
        self.chat = Chat()
    
    def get_name(self):
        try:
            return self.name
        except:
            return ''

class Chat:
    def __init__(self):
        self.window = Tk()
        self.window.title('Chit Chat')
        
        self.txtMsgList = Text(self.window)
        self.txtMsg = Text(self.window)
        self.txtMsg.bind('<KeyPress-Return>',self.sendMsgEvent)
        
        self.txtMsgList.grid(row=0,column=0)
        self.txtMsg.grid(row=1,column=0)
        
        
        
        self.send_btn = Button(self.window,width = 17,text='send',cursor = 'heart',command = self.send)
        self.cancel_btn = Button(self.window,width = 17, text='cancel',command = self.cancel)
        
        self.send_btn.grid(row=2,column=0)
        self.cancel_btn.grid(row=2,column=1)
        
        #self.window.mainloop()
        
    
    def cancel(self):
        self.txtMsg.delete('0.0',END)
    
    
    def send(self):
        self.strMsg = "Me" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n'
        self.message=self.txtMsg.get('0.0',END)
        self.txtMsgList.insert(END,self.strMsg,'greencolor')
        self.txtMsgList.insert(END,self.txtMsg.get('1.0',END))
        self.txtMsg.delete('1.0',END)
        #self.window.update()
    
    def sendMsgEvent(self,event):
        if event.keysym == 'Return':
            self.send()
    
    
        

    
        