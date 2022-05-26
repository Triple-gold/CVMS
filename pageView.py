from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.messagebox import *
import sys
import sqlite3
#import queryPage
import upLoadFile
from upLoadFile import *
import matplotlib.image as mping
from PIL import ImageTk, Image
import PIL.Image
import PIL.ImageTk

candidateIcon = None
class InputFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master
        self.itemName = StringVar()
        self.importPrice = StringVar()
        self.sellPrice = StringVar()
        self.deductPrice = StringVar()
        self.createPage()

    def createPage(self):

        Label(self, height = 850,width = 350,bg = '#C1CDCD').grid(row=0, column=0, sticky=NSEW)
        Label(self, text="Please push the button to upload the candidate resume", bg='#C1CDCD', fg='#FFFFFF',
              font=("Times", 20, "bold")).place(relx=0.5, rely=0.5, anchor='center')
        ttk.Button(self, text='Upload',width = 50, command=self.upLoadFile).place(relx=0.5, rely=0.6,anchor='center')


    def upLoadFile(self):
        upLoadFile.runUploadFunction()



class QueryFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master
        self.itemName = StringVar()
        self.createPage()

    def createPage(self):

        def refreshTree():
            items = tree.get_children()
            for item in items :
                tree.delete(item)
            database = sqlite3.connect('DataBase/CVMS.db')
            c = database.cursor()
            candidates = []
            candidates = c.execute("SELECT * FROM candidate")
            candidates = c.fetchall()
            for candidate in candidates:
                tree.insert("", tk.END, values=candidate)
        label1 = Label(self, text="Candidate", bg='white', fg='red', font=("Times", 20, "bold"))
        label1.grid(row=0, column=0, sticky=NSEW, padx=0, pady=0)

        columns = ('ID', 'Name', 'Email', 'Phone', 'Experience Years', 'resume')
        global tree
        tree = ttk.Treeview(self, columns=columns, show='headings')
        tree.column("ID", width=50)
        tree.column("Name", width=100)
        tree.column("Phone", width=65)
        tree.heading('ID', text='ID')
        tree.heading('Name', text='Name')
        tree.heading('Email', text='Email')
        tree.heading('Phone', text='Phone')
        tree.heading('Experience Years', text='Experience Years')
        tree.heading('resume', text='resume')
        tree.grid(row=1, column=0, sticky=NSEW)
        database = sqlite3.connect('DataBase/CVMS.db')
        c = database.cursor()
        candidates = []
        candidates = c.execute("SELECT * FROM candidate")
        candidates = c.fetchall()
        #print(candidates)
        candidate_icons = c.execute("SELECT userID FROM candidate_icon")
        candidate_icons = c.fetchall()
        for candidate in candidates:
            tree.insert("", tk.END, values=candidate)

        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1, column=1, sticky=W+NS)
        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview")
        tree.bind('<Double-1>', self.show_selected)
        ttk.Button(self, text="Show selected", command=self.show_selected).grid(row=2, column=0, stick=E, pady=10)
        ttk.Button(self, text='Show the resume', command=self.getTheResumeFile).grid(row=3, column=0, stick=NS+E, padx=0, pady=0)

        ttk.Button(self, text='Refresh', command=refreshTree).grid(row=0, column=0, stick=NS+E, padx=0, pady=0)


    def getTheResumeFile(self):

        curItem = tree.focus()
        pdfPathEnd = tree.item(curItem, 'values')
        print('this is th end ',(pdfPathEnd[5][1:]))
        pdfPath =os.getcwd()+pdfPathEnd[5][1:]
        print(pdfPath)
        os.system(pdfPath)

    r"./image/Temp/cv.pdf"
    def show_selected(self,event=None):
        top = Toplevel()
        top.title('Details')
        screenwidth = top.winfo_screenwidth()
        screenheight = top.winfo_screenheight()
        x = 800
        y = 600
        size = '%dx%d+%d+%d' % (x, y, (screenwidth - x) / 2, (screenheight - y) / 2)
        top.geometry(size)
        top.resizable(width=0, height=0)
        top.update()

        curItem = tree.focus()
        candidateId = tree.item(curItem, 'values')

        label2 = Label(top, text="ID:", bg='white', fg='red', font=("Times", 20, "bold"))
        label2.grid(row=1, column=3, sticky=NW, pady=10)
        userIDLabel = Label(top, text=candidateId[0], fg='black', font=("Times", 20, "bold"))
        userIDLabel.grid(row=1, column=4, sticky=NW, pady=10)

        label3 = Label(top, text="Name:", bg='white', fg='red', font=("Times", 20, "bold"))
        label3.grid(row=1, column=5, sticky=NW, padx=20, pady=10)
        userNameLabel = Label(top, text=candidateId[1], fg='black', font=("Times", 20, "bold"))
        userNameLabel.grid(row=1, column=6, sticky=NW, pady=10)


        database = sqlite3.connect('DataBase/CVMS.db')
        c = database.cursor()
        c.execute("SELECT image FROM candidate_icon where userID='%s'" % candidateId[0])
        #print(c.fetchone()[0])
        f = open(r"./image/Temp/image.jpg", 'wb')
        f.write(c.fetchone()[0])
        f.close()

        img = Image.open(r"./image/Temp/image.jpg")
        global candidateIcon
        candidateIcon = ImageTk.PhotoImage(img)

        candidateIconLabel = Label(top, image=candidateIcon)
        candidateIconLabel.grid(row=1, column=1, sticky=W, padx=10, pady=10)


        labelsFrame = tk.LabelFrame(top, text=' Languages ')
        labelsFrame.grid(row=2, column=1, columnspan=4,sticky=NW, padx=10, pady=10)

        c.execute("SELECT name FROM languages where candidateID='%s'" % candidateId[0])
        langs = c.fetchall()
        tk.Label(labelsFrame, text=(langs[0], "," , langs[1], ",", langs[2]), font=("Times", 12, "bold")).grid(row=1, column=1,sticky=NW+E, rowspan=2,  pady=5)
        EducationFrame = tk.LabelFrame(top, text=' Education Level ')
        EducationFrame.grid(row=3, column=1, columnspan=4, sticky=NW, padx=10, pady=10)
        c.execute("SELECT educationLevel FROM candidate where id='%s'" % candidateId[0])
        educationLevel = c.fetchone()
        tk.Label(EducationFrame, text=educationLevel[0], font=("Times", 12, "bold")).grid(row=1, column=1, sticky=NW, padx=5, pady=5)

        EducationFrame = tk.LabelFrame(top, text=' Experience Years ')
        EducationFrame.grid(row=4, column=1, columnspan=4, sticky=NW, padx=10, pady=10)
        c.execute("SELECT experience_years FROM candidate where id='%s'" % candidateId[0])
        experience_years = c.fetchone()
        tk.Label(EducationFrame, text=experience_years[0], font=("Times", 12, "bold")).grid(row=1, column=1, sticky=NW,
                                                                                            padx=5, pady=5)

        EducationFrame = tk.LabelFrame(top, text=' Last School ')
        EducationFrame.grid(row=2, column=3, columnspan=4, sticky=NW, padx=10, pady=10)
        # tk.Label(EducationFrame, text="Education Level:",  font=("Times", 12, "bold")).grid(row=1, column=1,sticky=NW)
        c.execute("SELECT last_school FROM candidate where id='%s'" % candidateId[0])
        last_school = c.fetchone()
        tk.Label(EducationFrame, text=last_school[0], font=("Times", 12, "bold")).grid(row=1, column=1, sticky=NW,
                                                                                       padx=5, pady=5)

        c.close()
        database.close()

class CountFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master
        self.createPage()

    def createPage(self):

        Label(self, text="Search Candidate", bg='white', fg='red', font=("Times", 20, "bold")).grid(row=0, column=0, sticky=NSEW, padx=0, pady=0)
        Label(self, text="Please enter the keyword :", font=("Times")).grid(row=1, column=0, sticky=W, padx=20, pady=0)
        global searchKeyword
        searchKeyword = tk.StringVar()
        ttk.Entry(self, text="Search Candidate",width = 60,textvariable=searchKeyword).grid(row=1, column=0, sticky=E, padx=200, pady=0)

        ttk.Button(self, text='Search', width = 20, command=self.searchDataToTree).grid(row=1, column=0, stick=NS + E, padx=0, pady=0)
        columns = ('ID', 'Name', 'Email', 'Phone', 'Experience Years', 'resume')
        global searchTree
        searchTree = ttk.Treeview(self, columns=columns, show='headings')
        searchTree.column("ID", width=50)
        searchTree.column("Name", width=100)
        searchTree.column("Phone", width=65)
        searchTree.heading('ID', text='ID')
        searchTree.heading('Name', text='Name')
        searchTree.heading('Email', text='Email')
        searchTree.heading('Phone', text='Phone')
        searchTree.heading('Experience Years', text='Experience Years')
        searchTree.heading('resume', text='resume')
        searchTree.grid(row=2, column=0, sticky=NSEW)
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=searchTree.yview)
        searchTree.configure(yscroll=scrollbar.set)
        searchTree.bind('<Double-1>',self.show_selected)
        scrollbar.grid(row=2, column=1, sticky=W + NS)
        ttk.Button(self, text='Show the resume', command=self.getTheResumeFile).grid(row=3, column=0, stick=NS+E, padx=0, pady=0)

    def getTheResumeFile(self):
        curItem = searchTree.focus()
        pdfPathEnd = searchTree.item(curItem, 'values')
        print('this is th end ', (pdfPathEnd[5][1:]))
        pdfPath = os.getcwd() + pdfPathEnd[5][1:]
        print(pdfPath)
        os.system(pdfPath)

    def searchDataToTree(self,event=None):
        items = searchTree.get_children()
        for item in items:
            searchTree.delete(item)
        database = sqlite3.connect('DataBase/CVMS.db')
        c = database.cursor()

        sKeyword = '%'+searchKeyword.get()+'%'
        candidateIds = c.execute("SELECT id FROM candidate where resume_text LIKE '%s'" % sKeyword)
        candidateIds = c.fetchall()
        for candidateId in candidateIds:
            candidates = c.execute("SELECT * FROM candidate where id = '%s'" % candidateId[0])
            candidates = c.fetchall()
            for candidate in candidates:
                searchTree.insert("", tk.END, values=candidate)
        c.close()
        database.close()

    def show_selected(self,event=None):
        top = Toplevel()
        top.title('Details')
        screenwidth = top.winfo_screenwidth()
        screenheight = top.winfo_screenheight()
        x = 800
        y = 600
        size = '%dx%d+%d+%d' % (x, y, (screenwidth - x) / 2, (screenheight - y) / 2)
        top.geometry(size)
        top.update()

        curItem = searchTree.focus()

        candidateId = searchTree.item(curItem, 'values')
        print(candidateId)

        label2 = Label(top, text="ID:", bg='white', fg='red', font=("Times", 20, "bold"))
        label2.grid(row=1, column=3, sticky=NW, pady=10)
        userIDLabel = Label(top, text=candidateId[0], fg='black', font=("Times", 20, "bold"))
        userIDLabel.grid(row=1, column=4, sticky=NW, pady=10)

        label3 = Label(top, text="Name:", bg='white', fg='red', font=("Times", 20, "bold"))
        label3.grid(row=1, column=5, sticky=NW, padx=20, pady=10)
        userNameLabel = Label(top, text=candidateId[1], fg='black', font=("Times", 20, "bold"))
        userNameLabel.grid(row=1, column=6, sticky=NW, pady=10)

        database = sqlite3.connect('DataBase/CVMS.db')
        c = database.cursor()
        c.execute("SELECT image FROM candidate_icon where userID='%s'" % candidateId[0])
        f = open(r"./image/Temp/image.jpg", 'wb')
        f.write(c.fetchone()[0])
        f.close()

        img = Image.open(r"./image/Temp/image.jpg")
        global candidateIcon
        candidateIcon = ImageTk.PhotoImage(img)

        candidateIconLabel = Label(top, image=candidateIcon)
        candidateIconLabel.grid(row=1, column=1, sticky=W, padx=10, pady=10)

        labelsFrame = tk.LabelFrame(top, text=' Languages ')
        labelsFrame.grid(row=2, column=1, columnspan=4, sticky=NW, padx=10, pady=10)

        c.execute("SELECT name FROM languages where candidateID='%s'" % candidateId[0])
        langs = c.fetchall()

        tk.Label(labelsFrame, text=(langs[0], ",", langs[1], ",", langs[2]), font=("Times", 12, "bold")).grid(row=1,
                                                                                                              column=1,
                                                                                                              sticky=NW + E,
                                                                                                              rowspan=2,
                                                                                                              pady=5)
        EducationFrame = tk.LabelFrame(top, text=' Education Level ')
        EducationFrame.grid(row=3, column=1, columnspan=4, sticky=NW, padx=10, pady=10)
        c.execute("SELECT educationLevel FROM candidate where id='%s'" % candidateId[0])
        educationLevel = c.fetchone()
        tk.Label(EducationFrame, text=educationLevel[0], font=("Times", 12, "bold")).grid(row=1, column=1,
                                                                                          sticky=NW, padx=5, pady=5)

        EducationFrame = tk.LabelFrame(top, text=' Experience Years ')
        EducationFrame.grid(row=4, column=1, columnspan=4, sticky=NW, padx=10, pady=10)
        c.execute("SELECT experience_years FROM candidate where id='%s'" % candidateId[0])
        experience_years = c.fetchone()
        tk.Label(EducationFrame, text=experience_years[0], font=("Times", 12, "bold")).grid(row=1, column=1,
                                                                                            sticky=NW,
                                                                                            padx=5, pady=5)

        EducationFrame = tk.LabelFrame(top, text=' Last School ')
        EducationFrame.grid(row=2, column=3, columnspan=4, sticky=NW, padx=10, pady=10)
        # tk.Label(EducationFrame, text="Education Level:",  font=("Times", 12, "bold")).grid(row=1, column=1,sticky=NW)
        c.execute("SELECT last_school FROM candidate where id='%s'" % candidateId[0])
        last_school = c.fetchone()
        tk.Label(EducationFrame, text=last_school[0], font=("Times", 12, "bold")).grid(row=1, column=1, sticky=NW,
                                                                                       padx=5, pady=5)

        c.close()
        database.close()

class AboutFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master
        self.createPage()

    def createPage(self):
        Label(self, height = 850,width = 350,bg = '#C1CDCD').grid(row=0, column=0, sticky=NSEW)
        Label(self, text="This function will be added in a future version",bg = '#C1CDCD', fg='#FFFFFF', font=("Times",20, "bold")).place(relx=0.5, rely=0.5,anchor='center')





