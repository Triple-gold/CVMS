# text = open(r'./image/temp/data.txt', "r", encoding="utf-8").read()
# r = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)??\d{8})')
# r = re.compile(r'(\d{3}[-\.\s\)]??\d{3}[-\.\s]??\d{4} | \(\d{3}\)\s*\d{3}[-\.\s]??\d{4} | \d{3}[-\.\s]??\d{4})')
# r = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{5}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{5}|\d{3}[-\.\s]??\d{5})')
# r = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{5}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{5}|\d{3}[-\.\s]??\d{5})')
# r = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
# print([re.sub(r'\D', '', number) for number in phone_numbers])

# column1 = column(self, text="Candidate", bg='white', fg='red', font=("Times", 20, "bold"))

# mylistbox = tk.Listbox(self,width=150)
# mylistbox.grid(row=1, column=0, stick=E, pady=10)

# mylistbox.insert(tk.END, 'apple')
# mylistbox.insert(tk.END, 'banana')
# mylistbox.insert(tk.END, 'orange')
# mylistbox.insert(tk.END, 'lemon')
# mylistbox.insert(tk.END, 'tomato')
# mylistbox.pack(side=LEFT)
# Button(self, text='Upload').grid(row=0, column=2, stick=E, pady=10)
#
# dataTreeview = ttk.Treeview(self, show='headings', column=('sid', 'sname', 'sex', 'sage'))
# #dataTreeview = ttk.Treeview(root, show='headings', column=('sid', 'sname', 'sex', 'sage'))
# dataTreeview.column('sid', width=150, anchor="center")
# dataTreeview.column('sname', width=150, anchor="center")
# dataTreeview.column('sex', width=150, anchor="center")
# dataTreeview.column('sage', width=150, anchor="center")
#
# dataTreeview.heading('sid', text='编号')
# dataTreeview.heading('sname', text='名称')
# dataTreeview.heading('sex', text='性别')
# dataTreeview.heading('sage', text='年龄')
# dataTreeview.pack()
# queryPage(mylistbox)
# self.columnconfigure(0, weight=1)
# self.columnconfigure(1, weight=7)
# self.rowconfigure(1, weight=3)
# self.QueryFrame.geometry('620x200')

#         queryPage(tree)
# def queryPage(tree):
#     #mylistbox = tk.Listbox(self)
#     #mylistbox.grid(row=0, column=2, stick=E, pady=10)
#     database = sqlite3.connect('DataBase/CVMS.db')
#     c = database.cursor()
#     candidates = c.execute("SELECT * FROM candidate")
#     for candidate in candidates:
#         tree.insert('', tk.END, values=candidate)

    #c.execute(query)
    # # 关闭游标
    # c.execute("select * from candidate_icon")
    #
    # # 查询存储结果（是二进制数据）
    # print(c.fetchone())
    # c.close()
    #print(c.fetchone())
    # database = sqlite3.connect('DataBase/CVMS.db')
    # # conn = sqlite3.connect('DataBase/CVMS.db')
    # c = database.cursor()
    # # c.execute("SELECT  image FROM candidate_icon")
    # c.execute("INSERT INTO candidate (name , email, phone,resumeFile) VALUES (?, ?, ?,?", (names[0], email, phone))
    # database.commit()

    #tree.insert('ID', tk.END, values="contact")

    # mylistbox.insert(tk.END, 'apple')
    # mylistbox.insert(tk.END, 'banana')
    # mylistbox.insert(tk.END, 'orange')
    # mylistbox.insert(tk.END, 'lemon')
    # mylistbox.insert(tk.END, 'tomato')
    #mylistbox = tk.Listbox(self)


# img_path = r"./image/cv"
# import sys
# import sqlite3
#
# #path = "C:\\Users\\Administrator\\Desktop\\1"
# # 读取图片文件
# fp = open(r"./image/face.jpg", 'rb')
# img = fp.read()
# fp.close()
#
# # 建立一个连接
# database = sqlite3.connect('DataBase/CVMS.db')
#
# # 创建游标
# c = database.cursor()
# # 创建表
#
# # 注意使用Binary()函数来指定存储的是二进制
# #c.execute('''CREATE TABLE candidate (width char, length char, image1 blob)''')
#
# # 存入图片
# c.execute("INSERT INTO candidate_icon (width, length,image, userID) VALUES (?, ?, ?, ?)", ('605', '300', img, '1'))
#
# database.commit()
# # 关闭游标
# c.execute("select * from candidate_icon")
#
# # 查询存储结果（是二进制数据）
# print(c.fetchone())
# c.close()
# # 关闭数据库连接
# database.close()
# #print("============")
# #print("End! ")++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++0

# 二、导出图片

import sys
import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute("SELECT  image1 FROM testb")
f = open('image.png', 'wb')
f.write(c.fetchone()[0])
f.close()
c.close()
conn.close()


import sys
# import sqlite3
# conn = sqlite3.connect('DataBase/CVMS.db')
# c = conn.cursor()
# c.execute("SELECT  image FROM candidate_icon")
# f = open(r"./image/Temp/image.png", 'wb')
# f.write(c.fetchone()[0])
# f.close()
# c.close()
# conn.close()
# cv2.imshow("face", cropped)


# text = open(r'./image/temp/data.txt', "r", encoding="utf-8").read()
# r = re.compile(r'(\d{3}[-\.\s]??\d{5}[-\.\s]??\d{5}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{5}|\d{3}[-\.\s]??\d{5})')
# # r = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{5}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{5}|\d{3}[-\.\s]??\d{5})')
# # r = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
# phone_numbers = r.findall(text)
# print("This is number")
# print([re.sub(r'\D', '', number) for number in phone_numbers])
#
# r = re.compile(r'[\w\.-]+@[\w\.-]+')

# print(r.findall(text))

# sentences = nltk.sent_tokenize(text)
# pos_tag_results = nltk.pos_tag(sentences)  # tagged sentences with pos_tag
# trigram_tagger = nltk.TrigramTagger(sentences)  # build trigram tagger based on your tagged_corpora
# trigram_tag_results = trigram_tagger(sentences)  # tagged sentences with trigram tagger
# for i in range(0, len(pos_tag_results)):
#     if pos_tag_results[i][1] == 'NN':
#         pos_tag_results[i][1] = trigram_tag_results[i][1]  # for 'NN' take trigram_tagger instead
# print(trigram_tag_results)


#candidate_icon = c.execute("SELECT image FROM candidate_icon where userID ='%s'", (candidate,))
            #print("this is test")
            #print(candidate[0])
            #print(candidate[0])
            c.execute("SELECT userID FROM candidate_icon ")
            userIconIDs = c.fetchall()

            #print(record)
            for userIconID in userIconIDs:
                print("this is test")
                print(userIconID)
                c.execute("SELECT id FROM candidate_icon where userID='%s'" % userIconID)
                userIconIDnb = c.fetchall()

                #print(userIconIDnb)
                break
            # if c.execute("SELECT image FROM candidate_icon where userID='%s'" % candidate[0]) is not None:
            #     f = open('image.png', 'wb')
            #     f.write(c.fetchone()[0])
            #     f.close()
            #     c.close()
            #conn.close()

            # c.execute(query)
            # userIcon = c.fetchone()

            #c.execute("SELECT  image1 FROM testb")



            #print(userIcon)
            #candidateID = candidate[0]
            #c.execute("SELECT image FROM candidate_icon")
            #c.execute("SELECT userID FROM candidate_icon where userID='%s'" % candidateID)
            #userIcon = c.fetchone()
            #print(userIcon)
            # userIcon = c.execute("SELECT image FROM candidate_icon where userID='%s'" % candidateID)
            #f = open('image.png','wb')
            #f.write(c.fetchone()[0])
            # print(userIcon)
            # if userIcon is not None:
            #     f = open('image.png', 'wb')
            #     #print(c.fetchone()[0])
            #     f.write(c.fetchone()[0])
            #     f.close()
            #     c.close()
            #conn.close()
            #tree.insert('', tk.END, values=userIcon)

        #print(theSum)
        #return theSum

           #print(candidate)
            # for candidate_icon in candidate_icons:
            #     if candidate_icon != candidate:
            #         print("break")
            #         break
            #     else:
            #         tree.insert('', tk.END, values=candidate_icon)
            #         print("looping2")