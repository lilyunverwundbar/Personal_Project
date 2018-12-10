import time
import socket
import select
import sys
import json
from chat_utils import *
import client_state_machine as csm

import GUIchat_system as gui



import threading

class Client:
    def __init__(self, args):
        self.peer = ''
        self.console_input = []
        self.state = S_OFFLINE
        self.system_msg = ''
        self.local_msg = ''
        self.peer_msg = ''
        self.args = args
        
        self.name=''
        
        
        
        

    def quit(self):
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()

    def get_name(self):
        return self.name

    def init_chat(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
        svr = SERVER if self.args.d == None else (self.args.d, CHAT_PORT)
        self.socket.connect(svr)
        self.sm = csm.ClientSM(self.socket)
        reading_thread = threading.Thread(target=self.read_input)
        reading_thread.daemon = True
        reading_thread.start()

    def shutdown_chat(self):
        return

    def send(self, msg):
        mysend(self.socket, msg)

    def recv(self):
        return myrecv(self.socket)

    def get_msgs(self):
        read, write, error = select.select([self.socket], [], [], 0)
        my_msg = ''
        peer_msg = []
        #peer_code = M_UNDEF    for json data, peer_code is redundant
        if len(self.console_input) > 0:
            my_msg = self.console_input.pop(0)
        if self.socket in read:
            peer_msg = self.recv()
        return my_msg, peer_msg

    def output(self):
        if self.sm.get_state()!=S_OFFLINE:
            if len(self.system_msg) > 0:
                self.log.chat.txtMsgList.insert(END,self.system_msg)
                self.system_msg = ''
            try:
                self.log.log_w.update()
            except:
                pass
            try:
                self.log.chat.window.update()
            except:
                pass
        
            
    

    def login(self):
        my_msg, peer_msg = self.get_msgs()
        if len(my_msg) > 0:
            self.name = my_msg
            msg = json.dumps({"action":"log", "name":self.name})
            self.send(msg)
            response = json.loads(self.recv())
            if response["status"] == 'ok':
                self.state = S_LOGGEDIN
                self.sm.set_state(S_LOGGEDIN)
                self.sm.set_myname(self.name)
                self.print_instructions()
                return (True)
            elif response["status"] == 'duplicate':
                self.system_msg += 'Duplicate username, try again'
                return False
        else:               # fix: dup is only one of the reasons
           return(False)

    
    '''def log_and_return_name(self):
        if log(self):
            self.name = self.logMsg.get('0.0',END)
            self.window.destroy()'''
            
    def read_input(self):                           #if state = LOGGED_IN and state = CHATTING
        if self.state == S_OFFLINE:
            try:
                while self.log.get_name()=='':
                    continue
                self.name = self.log.get_name()
                text = self.name
                self.console_input.append(text) # no need for lock, append is thread safe
                self.log.log_w.destroy()
            except:
                pass
        elif self.state == S_LOGGEDIN or S_CHATTING:
            try:
                if self.log.chat.message!='':
                    text = self.log.chat.message
                    self.log.chat.message=''
                    self.console_input.append(text)
            except:
                pass
    def print_instructions(self):
        self.system_msg += menu

    def run_chat(self):
        self.init_chat()
        self.log = gui.Login()
        self.system_msg += 'Welcome, ' + self.get_name() + '!'
        self.output()
        while self.sm.get_state() == S_OFFLINE:
            self.output()
        self.login()
        while self.sm.get_state() != S_OFFLINE:
            self.proc()
            self.output()
            time.sleep(CHAT_WAIT)
        self.quit()

#==============================================================================
# main processing loop
#==============================================================================
    def proc(self):
        my_msg, peer_msg = self.get_msgs()
        self.system_msg += self.sm.proc(my_msg, peer_msg)
