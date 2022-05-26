import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
import mainPage

class LoginPage:
    def __init__(self):
        self.root = tk.Tk()
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        x = 450
        y = 300
        size = '%dx%d+%d+%d' % (x, y, (screenwidth - x) / 2, (screenheight - y) / 2)
        self.root.geometry(size)
        self.root.update()
        self.root.title("Curriculum Vitae Manager System")
        self.creatPage()

    def creatPage(self):
        self.canvas = tk.Canvas(self.root, height=150, width=500)
        self.image_file = tk.PhotoImage(file='welcome.gif')
        self.image = self.canvas.create_image(0, 0, anchor='nw', image=self.image_file)
        self.canvas.pack(side='top')

        self.label_user = ttk.Label(self.root, text='User: ')
        self.label_password = ttk.Label(self.root, text='Password: ')
        self.canvas.pack()

        self.input_userName = ttk.Entry(self.root, width=30)
        self.input_password = ttk.Entry(self.root, show='*', width=30)

        self.login_button = ttk.Button(self.root, command=self.loginCheck, text="Login", width=10)
        self.siginUp_button = ttk.Button(self.root, command=self.siginUp_interface, text="Sign up", width=10)

        self.gui_arrang()

    def gui_arrang(self):
        self.label_user.place(x=60, y=170)
        self.label_password.place(x=60, y=195)
        self.input_userName.place(x=135, y=170)
        self.input_password.place(x=135, y=195)
        self.login_button.place(x=140, y=235)
        self.siginUp_button.place(x=240, y=235)

    def loginCheck(self):
        """Login Function"""
        user = self.input_userName.get()
        password = self.input_password.get()

        conn = sqlite3.connect('DataBase/CVMS.db')
        curs = conn.cursor()
        query = "select userName, password, state from users where userName='%s'" % user
        curs.execute(query)
        sql = curs.fetchall()
        if len(sql) == 0:
            tk.messagebox.showerror('Login Fail', 'Account Can''t find')
        else:
            s_user, s_password, s_state = sql[0]
            if s_state >= 3:
                tk.messagebox.showwarning('Login Fail', 'Account has been blocked')
            elif s_user == user and s_password == password:
                conn.close()
                self.root.destroy()
                mainPage.MainPage(s_user)
            else:
                tk.messagebox.showwarning('Login Fail', 'Wrong password')

    def siginUp_interface(self):
        tk.messagebox.showinfo(title='Curriculum Vitae Manager System', message='Enter the Siginup Page')
