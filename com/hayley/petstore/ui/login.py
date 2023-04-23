import tkinter as tk
import tkinter.messagebox
from com.hayley.petstore.ui.my_frame import MyFrame
from com.hayley.petstore.dao.account_dao import AccountDao
from com.hayley.petstore.dao.product_dao import ProductDao


class Login(tk.Tk):
    def __init__(self):
        super().__init__()  # 调用父类属性和方法

        self.title("petStore")
        self.geometry("500x300")

        # 创建界面控件
        tk.Label(self,text="用户id").grid(row=0, sticky="w")
        tk.Label(self,text="密码").grid(row=1, sticky="w")

        # 需要获取输入框内的值
        # 定义动态变量,accoutid
        accoutid = tk.StringVar()
        self.accoutid = tk.Entry(self, textvariable=accoutid)
        self.accoutid.grid(row=0, column=1)

        # 定义动态变量,password
        password = tk.StringVar()
        self.password = tk.Entry(self, textvariable=password)
        self.password.grid(row=1, column=1)

        self.login_btn = tk.Button(self, text="登录", width=10, command=self.log_btn_onclick)
        self.login_btn.grid(row=3, column=0, columnspan=2, sticky="w")

        self.quit_btn = tk.Button(self, text="退出", width=10, command=self.quit)
        self.quit_btn.grid(row=3, column=1, columnspan=2, sticky="e")

        # 开始主循环
        # self.root_window.mainloop()

    def log_btn_onclick(self):
        dao = AccountDao()

        account = dao.findbyid(self.accoutid.get())
        # print(account,'-----------')

        if account is not None:
            tkinter.messagebox.showinfo("提示", "今天是2022年11月")

            # 登录成功，保存用户session。
            MyFrame.Session = account
        else:
            tkinter.messagebox.showinfo("提示a","failed!")


if __name__ == "__main__":
    app = Login()
    app.mainloop()
