import sqlite3
import tkinter as tk
from pageView import *


class MainPage(object):
    def __init__(self, object):
        self.root = tk.Tk()
        self.root.title('Curriculum Vitae Manager System')
        x = 850
        y = 350
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        size = '%dx%d+%d+%d' % (x, y, (screenwidth - x) / 2, (screenheight - y) / 2)
        self.root.geometry(size)
        self.root.update()
        self.createPage()

    def createPage(self):
        self.inputPage = InputFrame(self.root)
        self.queryPage = QueryFrame(self.root)
        self.countPage = CountFrame(self.root)
        self.aboutPage = AboutFrame(self.root)
        self.inputPage.pack(side=LEFT, fill='y')
        menubar = Menu(self.root)
        menubar.add_command(label='Upload Resume', command=self.inputData)
        menubar.add_command(label='Query', command=self.queryData)
        menubar.add_command(label='Search Candidate', command=self.countData)
        menubar.add_command(label='Auto recommend', command=self.aboutDisp)
        self.root['menu'] = menubar

    def inputData(self):
        self.inputPage.pack(side=LEFT, fill='y')
        self.queryPage.pack_forget()
        self.countPage.pack_forget()
        self.aboutPage.pack_forget()

    def queryData(self):
        self.inputPage.pack_forget()
        self.queryPage.update()
        self.queryPage.pack(side=LEFT, fill='y')
        self.countPage.pack_forget()
        self.aboutPage.pack_forget()
        menubar = Menu(self.root)
        menubar.add_command(label='Upload Resume', command=self.inputData)
        menubar.add_command(label='Query', command=self.queryData)
        menubar.add_command(label='Search Candidate', command=self.countData)
        menubar.add_command(label='Auto recommend', command=self.aboutDisp)

    def countData(self):
        self.inputPage.pack_forget()
        self.queryPage.pack_forget()
        self.countPage.pack(side=LEFT, fill='y')
        self.aboutPage.pack_forget()
        menubar = Menu(self.root)
        menubar.add_command(label='Upload Resume', command=self.inputData)
        menubar.add_command(label='Query', command=self.queryData)
        menubar.add_command(label='Search Candidate', command=self.countData)
        menubar.add_command(label='Auto recommend', command=self.aboutDisp)

    def aboutDisp(self):
        self.inputPage.pack_forget()
        self.queryPage.pack_forget()
        self.countPage.pack_forget()
        self.aboutPage.pack()
