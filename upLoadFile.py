# run one time
# pip install PyMuPDF


import os
import shutil
import time
from tkinter import filedialog
import cv2
import ddddocr
import pyautogui as pyautogui
from PIL import Image, ImageEnhance
import os
import pytesseract
import cv2 as cv
import fitz
import nltk
from pyocr import builders
from nltk.corpus import stopwords
import aircv

import mainPage
import pageView

stop = stopwords.words('english')
import json
import cv2
import dlib
# nltk.download()
import re
import nltk
import sqlite3
from nltk.corpus import stopwords
import sys
from pdfminer.layout import LAParams, LTTextBox
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator

def UploadFile():
    # print("This is upload file")

    # select_path = r'C:\FYP\CVMS\image'
    #  print("location is " + os.getcwd())
    localTime = time.strftime("%Y%m%d-%H%M%S", time.localtime())

    filename = filedialog.askopenfilename(title='Please select the file')
    # mylistTest = []
    # List_Correct = []
    # print(filename)
    fileExtension = os.path.splitext(filename)[-1]
    # rint(fileExtension)

    imageFolderLoaction = (os.getcwd() + '/pdf/' + localTime + fileExtension)
    # print(" imageFolderLoaction" + imageFolderLoaction)
    shutil.copy(filename, imageFolderLoaction)
    imgName = os.path.basename(filename)
    # pdf_path = r"./pdf/ + localTime + '.pdf' "
    pdf_path = r"./pdf/" + localTime + '.pdf'
    # print("pdf_path" + pdf_path)

    # pdf_path = r"G:\User\Yam\Desktop\TestOpenCV2.pdf"
    img_path = r"./image/cv"
    # pdf_image(pdf_path, img_path, 5, 5, 0)
    return pdf_path, img_path


def pdf_image(pdfPath, imgPath):
    zoom_x = 5
    zoom_y = 5
    rotation_angle = 0

    pdf = fitz.open(pdfPath)

    trans = fitz.Matrix(zoom_x, zoom_y).prerotate(rotation_angle)
    pm = pdf[0].get_pixmap(matrix=trans, alpha=False)

    pm.save(imgPath + ".jpg")
    cvImagePath = imgPath + ".jpg"
        


    pdf.close()
    return cvImagePath

def redImage(cvImagePath):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    img_path = cvImagePath

    img = cv2.imread(img_path)
    edges = cv2.Canny(img, 100, 200)

  
    text = pytesseract.image_to_string(Image.fromarray(edges), lang='eng', config='–-psm 1')

    text_file = open(r'./image/temp/data.txt', "w", encoding="utf-8")

    n = text_file.write(text)

    text_file.close()
    # candidate_info(cvImagePath)


def get_info_formAPIs(file_pth):
    # from pathlib import Path
    print('This is the new', file_pth)
    from affinda import AffindaAPI, TokenCredential

    token = "f27c6ab8230af886a64231c6cc01634ddf592c20"
  
    credential = TokenCredential(token=token)
    client = AffindaAPI(credential=credential)

    with open(file_pth, "rb") as f:
        resume = client.create_resume(file=f)


    text_json_file = open(r'./image/temp/data.json', "w")
    json.dump(resume.as_dict(), text_json_file, indent = 6)
  
    text_json_file.close()
    get_date_from_jason()


def get_date_from_jason():
    with open(r'./image/temp/data.json') as f:
        data = json.load(f)
    database = sqlite3.connect('DataBase/CVMS.db')
    c = database.cursor()
    c.execute("select id from candidate ORDER by id DESC limit 1")
    candidateID = c.fetchone()
    langs = data['data']['languages']
    for lang in langs:
        c.execute("INSERT INTO languages (name , candidateID) VALUES (?, ?)", (lang, candidateID[0]))

    input_str = data['data']['education'][0]["accreditation"]["input_str"]
    education = data['data']['education'][0]["accreditation"]["education_level"]
    experience_years = data['data']['total_years_experience']
    last_school = data['data']['education'][0]["organization"]
    print(last_school)
    if "Higher Diploma" in input_str:
        education = "Higher Diploma"

    c.execute('''UPDATE candidate SET educationLevel = ? WHERE id = ?''', (education, candidateID[0]))
    c.execute('''UPDATE candidate SET experience_years = ? WHERE id = ?''', (experience_years, candidateID[0]))
    c.execute('''UPDATE candidate SET last_school = ? WHERE id = ?''', (last_school, candidateID[0]))



    database.commit()
    c.execute("select * from languages")
    c.close()
    database.close()



def scanFace(path):
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(
        r"./trainModel/shape_predictor_68_face_landmarks.dat"
    )
    color = (0, 255, 0)

    dets = detector(gray, 1)
    for face in dets:
        shape = predictor(img, face)
        length = []
        width = []
        for pt in shape.parts():
            pt_pos = (pt.x, pt.y)
            length.append(pt.x)
            width.append(pt.y)
        length_max = max(length)
        length_mix = min(length)
        width_max = max(width)
        width_min = min(width)
        cv2.rectangle(img, (length_mix, width_min), (length_max, width_max), color, 1)
        cropped = img[width_min + 1:width_max, length_mix + 1:length_max]

        cv2.imwrite(r"./image/face.jpg", cropped)

        database = sqlite3.connect('DataBase/CVMS.db')
        c = database.cursor()
        c.execute("select id from candidate ORDER by id DESC limit 1")
        userID = c.fetchone()

        fp = open(r"./image/face.jpg", 'rb')
        img = fp.read()
        fp.close()

        c.execute("INSERT INTO candidate_icon (width, length, image, userID) VALUES (?, ?, ?, ?)", ('250', '200', img, userID[0]))
        database.commit()
        c.execute("select * from candidate_icon")
        c.close()
        database.close()


def ie_preprocess(document):
    document = ' '.join([i for i in document.split() if i not in stop])
    sentences = nltk.sent_tokenize(document)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]

    return sentences


def candidate_info(cvImagePath,pdf_path):
    names = []
    text = open(r'./image/temp/data.txt', "r", encoding="utf-8").read()
    sentences = ie_preprocess(text)
    for tagged_sentence in sentences:
        for chunk in nltk.ne_chunk(tagged_sentence):
            if type(chunk) == nltk.tree.Tree:
                if chunk.label() == 'PERSON':
                    names.append(' '.join([c[0] for c in chunk]))


    r = re.compile(r'(5\d{8}|6\d{7}|8\d{7}|9\d{7})')

    phone_numbers = r.findall(text)

    phones = ([re.sub(r'\D', '', number) for number in phone_numbers])
    r = re.compile(r'[\w\.-]+@[\w\.-]+')
    emails = (r.findall(text))


    database = sqlite3.connect('DataBase/CVMS.db')
    c = database.cursor()


    c.execute("INSERT INTO candidate (name , email, phone,resumeFile,resume_text) VALUES (?, ?, ?,?,?)", (names[0], emails[0], phones[0],pdf_path,text))
    database.commit()

    return names, emails, phones


def pdfCompress(cvImagePath):
    image_1 = Image.open(cvImagePath)
    im_1 = image_1.convert('RGB')
    pdfed_src_path = r'./image/Temp/cv.pdf'
    im_1.save(pdfed_src_path)
    return pdfed_src_path

def runUploadFunction():
    pdf_path, img_path = UploadFile()
    cvImagePath = pdf_image(pdf_path, img_path)
    redImage(cvImagePath)
    candidate_info(cvImagePath,pdf_path)
    scanFace(cvImagePath)
    pdfed_src = pdfCompress(cvImagePath)
    print('this is the final output', pdf_path)
    get_info_formAPIs(pdfed_src)

if __name__ == '__main__':
    runUploadFunction()
