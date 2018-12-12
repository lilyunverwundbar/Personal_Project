import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import chat_utils


class ChatSystemGUI(object):

    def __init__(self, root):
        self.root = root
        self.width = 400
        self.height = 600
        self.max_entry = 500.0    # Index Length Constraint
        self.new_message = ''    # Input Box Info
        self.new_message_copy = ''
        self.client_message = ''
        self.name = ''    # Login Username
        self.root.title('Chat System')
        self.root.geometry(str(self.width) + 'x' + str(self.height))
        self.root.maxsize(width=self.width, height=self.height)
        self.root.minsize(width=self.width, height=self.height)
        # Parameters
        self.image_count = None
        self.image_dict = None
        self.previous_is_image = None
        self.server_message = ''
        # ENTER LOGIN PAGE
        # Blank Setting
        self.space_place = tk.Frame(self.root, width=self.width - 20,
                                    height=250, bg='white')
        self.space_place.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        # Register Bar
        self.name_place = tk.Frame(self.root, width=self.width - 100,
                                   height=20, bg='black')
        self.name_place.grid(row=1, column=0, padx=80, pady=10, sticky='w')
        # Register Input Box
        self.name_input = tk.Text(self.name_place, width=30, height=1)
        self.name_input.grid(row=0, column=0, padx=5, pady=5)
        # Confirm Bar
        self.submit_place = tk.Frame(self.root, width=self.width - 200,
                                     height=15, bg='black')
        self.submit_place.grid(row=2, column=0, padx=0, pady=10)
        # Confirm Button
        self.submit_button = tk.Button(self.submit_place, text='log in',
                                       width=15, height=1, padx=5, pady=5,
                                       command=lambda: self.log_in())
        self.submit_button.grid(row=0, column=0, padx=5, pady=5)

    # AFTER LOGIN
    def log_in(self):
        self.name = self.name_input.get(1.0, self.max_entry).split('\n')[0]
        self.new_message = self.name
        self.show_welcome()
        
    # Welcome Msg
    def show_welcome(self):
        self.reset()
        self.welcome_place = tk.Frame(self.root, width=self.width,
                                      height=250, bg='black')
        self.welcome_place.grid(row=0, column=0, padx=10, pady=200, sticky='w')
        self.welcome = tk.Label(self.welcome_place, width=24,
                                height=1, bg='white', text='WELCOME!')
        self.welcome.grid(row=0, column=0, padx=80, pady=10, sticky='w')
        self.root.after(1800, self.enter)

    # Clear Out the Page
    def reset(self):
        all_item = self.root.grid_slaves()
        for item in all_item:
            item.destroy()

    # Enter the Chat Interface
    def enter(self):
        self.reset()
        self.image_count = 1.0
        self.image_dict = dict()
        self.previous_is_image = False
        # Demonstration Bar
        self.output_place = tk.Frame(self.root, width=self.width - 20,
                                     height=self.height / 2, bg='black')
        self.output_place.grid(row=0, column=0, padx=10, pady=10)
        # Demonstration Box
        self.output = tk.Text(self.output_place, width=50, height=19)
        self.output.insert('end', chat_utils.menu)
        self.output.config(state='disabled')
        self.output.grid(row=0, column=0, padx=10, pady=10)
        # Rolling Bar for Demonstration Box
        self.scroll_bar = tk.Scrollbar(self.output_place, command=self.output.yview)
        self.scroll_bar.grid(row=0, column=1, sticky='nsew')
        self.output['yscrollcommand'] = self.scroll_bar.set
        # Button Bar
        self.button = tk.Frame(self.root, width=self.width - 20,
                               height=20, bg='black')
        self.button.grid(row=1, column=0, padx=10, pady=10)
        # Button -- 'select picture'
        self.select_button = tk.Button(self.button, text='select picture',
                                       width=15, padx=5, pady=5,
                                       command=lambda: self.select_picture())
        self.select_button.grid(row=1, column=0, padx=10, pady=10)
        # Button -- 'send'
        self.send_button = tk.Button(self.button, text='send',
                                     width=8, padx=5, pady=5,
                                     command=lambda: self.send_message())
        self.send_button.grid(row=1, column=1, padx=10, pady=10)
        # Input Bar
        self.input_place = tk.Frame(self.root, width=self.width - 20,
                                    height=self.height / 3 - 10, bg='black')
        self.input_place.grid(row=2, column=0, padx=10, pady=10)
        # Input Box
        self.input = tk.Text(self.input_place, width=50, height=10)
        self.input.grid(row=0, column=0, padx=10, pady=10)

    def select_picture(self):
        self.new_message_copy = filedialog.askopenfilename(initialdir='')
        self.new_message = self.new_message_copy
        # If cancel selecting file
        if self.new_message_copy == '':
            return
        # If the file opened is not a picture file
        if self.new_message_copy.split('.')[-1] not in ['png', 'gif', 'jpg']:
            return
        self.image_dict[self.image_count] = Image.open(self.new_message_copy)
        self.image_dict[self.image_count] = self.image_dict[self.image_count].resize((100, 100), Image.ANTIALIAS)
        self.image_dict[self.image_count] = ImageTk.PhotoImage(self.image_dict[self.image_count])
        self.output.config(state='normal')
        if self.previous_is_image:
            self.output.insert('end', '\nme: \n')
        else:
            self.output.insert('end', 'me: \n')
        self.output.image_create('end', image=self.image_dict[self.image_count])
        self.image_count += 1
        self.output.config(state='disabled')
        self.previous_is_image = True

    def send_message(self):
        print(1)
        self.new_message = self.input.get(1.0, self.max_entry)
        self.new_message_copy = self.input.get(1.0, self.max_entry)
        if self.previous_is_image:
            self.output.config(state='normal')
            self.output.insert('end', '\n' + 'me: ' + self.new_message_copy)
            self.output.config(state='disabled')
            self.previous_is_image = False
        else:
            self.output.config(state='normal')
            self.output.insert('end', 'me: ' + self.new_message_copy)
            self.output.config(state='disabled')
        self.input.delete(1.0, self.max_entry)    # Empty Input Box

    def push_message(self):
        try:
            if self.server_message.split('.')[-1] in ['png', 'gif', 'jpg']:
                name, self.server_message = self.server_message.split(']')
                name = name + ']'
                self.output.config(state='normal')
                if self.previous_is_image:
                    self.output.insert('end', '\n' + name + '\n')
                else:
                    self.output.insert('end', name + '\n')
                self.image_dict[self.image_count] = Image.open(self.server_message)
                self.image_dict[self.image_count] = self.image_dict[self.image_count].resize((100, 100),
                                                                                             Image.ANTIALIAS)
                self.image_dict[self.image_count] = ImageTk.PhotoImage(self.image_dict[self.image_count])
                self.output.image_create('end', image=self.image_dict[self.image_count])
                self.image_count += 1
                self.output.config(state='disabled')
                self.previous_is_image = True
                self.server_message = ''
            else:
                if self.previous_is_image:
                    self.output.config(state='normal')
                    self.output.insert('end', '\n' + self.server_message + '\n')
                    self.output.config(state='disabled')
                else:
                    self.output.config(state='normal')
                    self.output.insert('end', self.server_message + '\n')
                    self.output.config(state='disabled')
                self.previous_is_image = False
                self.server_message = ''
        except AttributeError:
            pass




