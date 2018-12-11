import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
import chat_utils
import copy


class ChatSystemGUI(object):

    def __init__(self, root):
        self.root = root
        self.width = 400
        self.height = 600
        self.max_entry = 500.0    # 最大输入字符长度
        self.new_message = ''    # 输入框信息
        self.new_message_copy = ''
        self.client_message = ''
        self.name = ''    # 登陆用户名
        self.root.title('Chat System')
        self.root.geometry(str(self.width) + 'x' + str(self.height))
        self.root.maxsize(width=self.width, height=self.height)
        self.root.minsize(width=self.width, height=self.height)
        # 只是为了初始化参数而写
        self.image_count = None
        self.image_dict = None
        self.previous_is_image = None
        self.output_place = None
        self.output = None
        self.scroll_bar = None
        self.button = None
        self.select_button = None
        self.send_button = None
        self.input_place = None
        self.input = None
        self.welcome_place = None
        self.welcome = None
        self.server_message = ''
        # 进入登陆界面
        # 空白布局
        self.space_place = tk.Frame(self.root, width=self.width - 20,
                                    height=250, bg='white')
        self.space_place.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        # 登陆栏
        self.name_place = tk.Frame(self.root, width=self.width - 100,
                                   height=20, bg='black')
        self.name_place.grid(row=1, column=0, padx=80, pady=10, sticky='w')
        # 登陆框
        self.name_input = tk.Text(self.name_place, width=30, height=1)
        self.name_input.grid(row=0, column=0, padx=5, pady=5)
        # 确认栏
        self.submit_place = tk.Frame(self.root, width=self.width - 200,
                                     height=15, bg='black')
        self.submit_place.grid(row=2, column=0, padx=0, pady=10)
        # 确认按钮
        self.submit_button = tk.Button(self.submit_place, text='log in',
                                       width=15, height=1, padx=5, pady=5,
                                       command=lambda: self.log_in())
        self.submit_button.grid(row=0, column=0, padx=5, pady=5)

    # 登陆后动作
    def log_in(self):
        self.name = self.name_input.get(1.0, self.max_entry).split('\n')[0]
        self.new_message = self.name
        self.show_welcome()

    def show_welcome(self):
        self.reset()
        self.welcome_place = tk.Frame(self.root, width=self.width,
                                      height=250, bg='black')
        self.welcome_place.grid(row=0, column=0, padx=10, pady=200, sticky='w')
        self.welcome = tk.Label(self.welcome_place, width=24,
                                height=1, bg='white', text='WELCOME!')
        self.welcome.grid(row=0, column=0, padx=80, pady=10, sticky='w')
        self.root.after(1800, self.enter)

    # 清空界面
    def reset(self):
        all_item = self.root.grid_slaves()
        for item in all_item:
            item.destroy()

    # 进入聊天界面
    def enter(self):
        self.reset()
        self.image_count = 1.0
        self.image_dict = dict()
        self.previous_is_image = False
        # 展示栏
        self.output_place = tk.Frame(self.root, width=self.width - 20,
                                     height=self.height / 2, bg='black')
        self.output_place.grid(row=0, column=0, padx=10, pady=10)
        # 展示框
        self.output = tk.Text(self.output_place, width=50, height=19)
        self.output.insert('end', chat_utils.menu)
        self.output.config(state='disabled')
        self.output.grid(row=0, column=0, padx=10, pady=10)
        # 展示框滚动条
        self.scroll_bar = tk.Scrollbar(self.output_place, command=self.output.yview)
        self.scroll_bar.grid(row=0, column=1, sticky='nsew')
        self.output['yscrollcommand'] = self.scroll_bar.set
        # 按钮栏
        self.button = tk.Frame(self.root, width=self.width - 20,
                               height=20, bg='black')
        self.button.grid(row=1, column=0, padx=10, pady=10)
        # 选择图片
        self.select_button = tk.Button(self.button, text='select picture',
                                       width=15, padx=5, pady=5,
                                       command=lambda: self.select_picture())
        self.select_button.grid(row=1, column=0, padx=10, pady=10)
        # 发送按钮
        self.send_button = tk.Button(self.button, text='send',
                                     width=8, padx=5, pady=5,
                                     command=lambda: self.send_message())
        self.send_button.grid(row=1, column=1, padx=10, pady=10)
        # 输入栏
        self.input_place = tk.Frame(self.root, width=self.width - 20,
                                    height=self.height / 3 - 10, bg='black')
        self.input_place.grid(row=2, column=0, padx=10, pady=10)
        # 输入框
        self.input = tk.Text(self.input_place, width=50, height=10)
        self.input.grid(row=0, column=0, padx=10, pady=10)

    def select_picture(self):
        self.new_message = filedialog.askopenfilename(initialdir='')
        # 如果取消选择文件
        if self.new_message == '':
            return
        # 如果打开的不是图片文件
        try:
            self.image_dict[self.image_count] = Image.open(self.new_message)
        except OSError:
            return
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
        if self.previous_is_image:
            self.new_message = '\n' + 'me: ' + self.input.get(1.0, self.max_entry)
            self.new_message_copy = '\n' + 'me: ' + self.input.get(1.0, self.max_entry)
            self.previous_is_image = False
        else:
            self.new_message = 'me: ' + self.input.get(1.0, self.max_entry)
            self.new_message_copy = '\n' + 'me: ' + self.input.get(1.0, self.max_entry)
        self.output.config(state='normal')
        self.output.insert('end', self.new_message_copy)
        self.output.config(state='disabled')
        self.input.delete(1.0, self.max_entry)    # 清空输入框

    def push_message(self):
        try:
            # todo: 图片后紧跟 server_message
            self.output.config(state='normal')
            self.output.insert('end', 'system: ' + self.server_message)
            self.output.config(state='disabled')
            self.server_message = ''
        except AttributeError:
            pass

    # 定时刷新，单位毫秒
    def refresh(self):
        if len(self.server_message) > 0:
            self.output.config(state='normal')
            self.output.insert('end', self.server_message)
            self.output.config(state='disabled')
            self.server_message = ''
            print(1111)
        self.root.after(1000, self.refresh)

    def run(self):
        self.refresh()


if __name__ == '__main__':

    test = ChatSystemGUI(root=tk.Tk())
    test.run()
    test.root.mainloop()

