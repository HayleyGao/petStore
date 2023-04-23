import tkinter as tk
import tkinter.messagebox
from com.hayley.petstore.ui.my_frame import MyFrame
from com.hayley.petstore.dao.account_dao import AccountDao
from com.hayley.petstore.dao.product_dao import ProductDao


class ProductsList(tk.Tk):
    def __init__(self):
        super().__init__()  # 调用父类属性和方法

        self.title("petStore")
        self.geometry("600x350")

        # 创建界面控件

        self.login_btn = tk.Button(self, text="查看所有商品", command=self.prodslist_btn_onclick)
        self.login_btn.grid(row=0, column=0, columnspan=2, sticky="w")

        self.quit_btn = tk.Button(self, text="退出", width=10, command=self.quit)
        self.quit_btn.grid(row=0, column=4, columnspan=2, sticky="e")

        self.list_ = tk.StringVar()
        self.list_.set(['a', 'apple', 'fish', 'stars', 'movie', 'cookie', '定风波·苏轼'])

        self.listbox1 = tk.Listbox(self, listvariable=self.list_, width=20)
        self.listbox1.grid(row=5, column=0, padx='5px', pady='5px', ipadx='5px', ipady='5px')  # 别忘记布局，不然不会显示在窗口上。
        # 给设置默认值
        # for i in range(8):
        #     self.listbox1.insert(i,i)

        # prod = tk.StringVar()
        # tk.Label(self, width=20, textvariable=prod)
        self.listbox1.bind('<<ListboxSelect>>', self.itemSelected)  # 绑定事件

        # 用于展示展示选中的列表项
        self.disp = tk.StringVar()
        self.disp.set('haha')
        self.display_ = tk.Label(self, width=20, text='展示选中的列表项', textvariable=self.disp, background='yellow')
        self.display_.grid(row=3, columnspan=2, column=1, sticky="w")

    def itemSelected(self, event):
        index = self.listbox1.curselection()  # 获取选中的索引
        self.disp.set(self.listbox1.get(index))

    def prodslist_btn_onclick(self):
        dao = ProductDao()

        products = dao.findall()
        print(products, '-----------')

        if products is not None:
            tkinter.messagebox.showinfo("提示", "显示所有的商品喽！")
            name_tmp = []
            for product in products:
                name_tmp.append(product['ename'])
            self.list_.set(name_tmp)

        else:
            tkinter.messagebox.showinfo("提示a", "failed!")


if __name__ == "__main__":
    app = ProductsList()
    app.mainloop()
