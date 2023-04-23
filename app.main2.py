import tkinter as tk
from tkinter import messagebox


class App:
    def onInit(self):
        root_window = tk.Tk()
        root_window.title("petStore")
        root_window.geometry('500x300')

        tk.Label(root_window, text="用户id").grid(row=0, sticky="w")
        tk.Label(root_window, text="密码").grid(row=1, sticky="w")

        tk.Entry(root_window).grid(row=0, column=1)
        tk.Entry(root_window).grid(row=1, column=1)

        tk.Button(root_window, text="登录", width=10, command=login).grid(row=3, column=0, columnspan=2, sticky="w")
        tk.Button(root_window, text="退出", width=10, command=root_window.quit).grid(row=3, column=1, columnspan=2,
                                                                                   sticky="e")
        root_window.configure(bg="white")
        # 开始主循环
        root_window.mainloop()


def login():
    messagebox.showinfo("welcome to petStore!")


if __name__ == "__main__":
    app = App()
    app.onInit()
