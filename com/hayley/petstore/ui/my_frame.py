import tkinter as tk
from tkinter import messagebox


# 定义Frame基类窗口

class MyFrame(tk.Tk):
    # 用户登录之后，用于保存当前用户信息
    Session = {}

    def __init__(self):
        # self.root_window = tk.Tk()
        # self.root_window.title("petStore")
        # self.root_window.geometry('500x300')

        self.title("petStore")
        self.geometry('500x300')

        # 开始主循环
        # self.root_window.mainloop()
        self.mainloop() # 继承tk.Tk

    def quit(self):
        messagebox.showinfo("See you next time!")
        self.root_window.quit()
