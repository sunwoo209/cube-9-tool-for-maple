#Made By 로슈
#내부 패키지
import atexit
import os
import cv2
import re
import time
from tkinter import *
import ctypes

#conda + pip
import pyautogui as pag
import mss
import numpy as np
import pytesseract
from  PIL import Image
import keyboard
cube_button_pos = [661, 508]

#테서렉트 주소 " 앞에 r 붙이기
directory = r"C:\Program Files\Tesseract-OCR\tesseract.exe"



def click():
        pag.moveTo(cube_button_pos)
        time.sleep(0.2)
        pag.mouseDown(button='left')
        pag.mouseUp(button='left')
        pag.press('enter')
        pag.press('enter')
        pag.press('enter')

def exitf():

                print("종료합니다")
                os.remove('gray1.jpg')
                os.remove('gray2.jpg')
                os.remove('gray3.jpg')
                os.remove('first_screen.jpg')
                os.remove('second_screen.jpg')
                os.remove('third_screen.jpg')



def cleanText(readData):
        text = re.sub('[-=,#/\?^$.@*\"※~&:ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', readData)
        return text

if ctypes.windll.shell32.IsUserAnAdmin():
    print('관리자권한으로 실행된 프로세스입니다.')
else:
    print('일반권한으로 실행된 프로세스입니다.')
    print('관리자권한으로 실행해 주세요.')
    print('종료합니다.')
    time.sleep(3.0)
    sys.exit()


def STRsetting():
    while True:
     try:
        if keyboard.is_pressed('Esc'):
                        print("STOP")
                        break
        click()
        time.sleep(1.0)
        pytesseract.pytesseract.tesseract_cmd = directory

        first_option_pos = {'left': 600, 'top': 427, 'width': 130, 'height': 16}
        second_option_pos = {'left': 600, 'top': 441, 'width': 130, 'height': 16}
        third_option_pos = {'left': 600, 'top': 454, 'width': 130, 'height': 16}



        with mss.mss() as sct:
            first_img = np.array(sct.grab(first_option_pos))[:,:,:3]
            second_img = np.array(sct.grab(second_option_pos))[:,:,:3]
            third_img = np.array(sct.grab(third_option_pos))[:,:,:3]


        cv2.imwrite('first_screen.jpg',first_img)
        Number1='first_screen.jpg'
        img1=cv2.imread(Number1,cv2.IMREAD_COLOR)
        img2=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
        img2=cv2.bitwise_not(img2)
        cv2.imwrite('gray1.jpg',img2)
        first_grayimg='gray1.jpg'

        cv2.imwrite('second_screen.jpg',second_img)
        Number2='second_screen.jpg'
        img3=cv2.imread(Number2,cv2.IMREAD_COLOR)
        img4=cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
        img4=cv2.bitwise_not(img4)
        cv2.imwrite('gray2.jpg',img4)
        second_grayimg='gray2.jpg'

        cv2.imwrite('third_screen.jpg',third_img)
        Number3='third_screen.jpg'
        img5=cv2.imread(Number3,cv2.IMREAD_COLOR)
        img6=cv2.cvtColor(img5,cv2.COLOR_BGR2GRAY)
        img6=cv2.bitwise_not(img6)
        cv2.imwrite('gray3.jpg',img6)
        third_grayimg='gray3.jpg'

        first_option=pytesseract.image_to_string(first_grayimg, lang='eng')
        second_option=pytesseract.image_to_string(second_grayimg, lang='eng')
        third_option=pytesseract.image_to_string(third_grayimg, lang='eng')
        p_first=cleanText(first_option)
        p_second=cleanText(second_option)
        p_third=cleanText(third_option)

        a=(p_first.split())
        b=(p_second.split())
        c=(p_third.split())
        print(a)
        print(b)
        print(c)
        print("-----")


        if a[0] == 'STR' and a[1] == '+6%':
            if b[0] == 'STR' and b[1] == '+3%':
                    break
            if c[0] == 'STR' and c[1] == '+3%':
                    break
            if b[0] == 'STR' and b[1] == '+6%':
                    break
            if c[0] == 'STR' and c[1] == '+6%':
                    break
        if b[0] == 'STR' and b[1] == '+6%':
            if c[0] == 'STR' and c[1] == '+3%':
                    break
            if c[0] == 'STR' and c[1] == '+6%':
                    break


     except IndexError:
            continue
def DEXsetting():
    while True:
     try:
        if keyboard.is_pressed('Esc'):
                        print("STOP")
                        break
        click()
        time.sleep(1.0)
        pytesseract.pytesseract.tesseract_cmd = directory

        first_option_pos = {'left': 600, 'top': 427, 'width': 130, 'height': 16}
        second_option_pos = {'left': 600, 'top': 441, 'width': 130, 'height': 16}
        third_option_pos = {'left': 600, 'top': 454, 'width': 130, 'height': 16}



        with mss.mss() as sct:
            first_img = np.array(sct.grab(first_option_pos))[:,:,:3]
            second_img = np.array(sct.grab(second_option_pos))[:,:,:3]
            third_img = np.array(sct.grab(third_option_pos))[:,:,:3]


        cv2.imwrite('first_screen.jpg',first_img)
        Number1='first_screen.jpg'
        img1=cv2.imread(Number1,cv2.IMREAD_COLOR)
        img2=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
        img2=cv2.bitwise_not(img2)
        cv2.imwrite('gray1.jpg',img2)
        first_grayimg='gray1.jpg'

        cv2.imwrite('second_screen.jpg',second_img)
        Number2='second_screen.jpg'
        img3=cv2.imread(Number2,cv2.IMREAD_COLOR)
        img4=cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
        img4=cv2.bitwise_not(img4)
        cv2.imwrite('gray2.jpg',img4)
        second_grayimg='gray2.jpg'

        cv2.imwrite('third_screen.jpg',third_img)
        Number3='third_screen.jpg'
        img5=cv2.imread(Number3,cv2.IMREAD_COLOR)
        img6=cv2.cvtColor(img5,cv2.COLOR_BGR2GRAY)
        img6=cv2.bitwise_not(img6)
        cv2.imwrite('gray3.jpg',img6)
        third_grayimg='gray3.jpg'

        first_option=pytesseract.image_to_string(first_grayimg, lang='eng')
        second_option=pytesseract.image_to_string(second_grayimg, lang='eng')
        third_option=pytesseract.image_to_string(third_grayimg, lang='eng')
        p_first=cleanText(first_option)
        p_second=cleanText(second_option)
        p_third=cleanText(third_option)

        a=(p_first.split())
        b=(p_second.split())
        c=(p_third.split())
        print(a)
        print(b)
        print(c)
        print("-----")


        if a[0] == 'DEX' and a[1] == '+6%':
            if b[0] == 'DEX' and b[1] == '+3%':
                    break
            if c[0] == 'DEX' and c[1] == '+3%':
                    break
            if b[0] == 'DEX' and b[1] == '+6%':
                    break
            if c[0] == 'DEX' and c[1] == '+6%':
                    break
        if b[0] == 'DEX' and b[1] == '+6%':
            if c[0] == 'DEX' and c[1] == '+3%':
                    break
            if c[0] == 'DEX' and c[1] == '+6%':
                    break

     except IndexError:
            continue
def INTsetting():
    while True:
     try:
        if keyboard.is_pressed('Esc'):
                        print("STOP")
                        break
        click()
        time.sleep(1.0)
        pytesseract.pytesseract.tesseract_cmd = directory

        first_option_pos = {'left': 600, 'top': 427, 'width': 130, 'height': 16}
        second_option_pos = {'left': 600, 'top': 441, 'width': 130, 'height': 16}
        third_option_pos = {'left': 600, 'top': 454, 'width': 130, 'height': 16}



        with mss.mss() as sct:
            first_img = np.array(sct.grab(first_option_pos))[:,:,:3]
            second_img = np.array(sct.grab(second_option_pos))[:,:,:3]
            third_img = np.array(sct.grab(third_option_pos))[:,:,:3]


        cv2.imwrite('first_screen.jpg',first_img)
        Number1='first_screen.jpg'
        img1=cv2.imread(Number1,cv2.IMREAD_COLOR)
        img2=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
        img2=cv2.bitwise_not(img2)
        cv2.imwrite('gray1.jpg',img2)
        first_grayimg='gray1.jpg'

        cv2.imwrite('second_screen.jpg',second_img)
        Number2='second_screen.jpg'
        img3=cv2.imread(Number2,cv2.IMREAD_COLOR)
        img4=cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
        img4=cv2.bitwise_not(img4)
        cv2.imwrite('gray2.jpg',img4)
        second_grayimg='gray2.jpg'

        cv2.imwrite('third_screen.jpg',third_img)
        Number3='third_screen.jpg'
        img5=cv2.imread(Number3,cv2.IMREAD_COLOR)
        img6=cv2.cvtColor(img5,cv2.COLOR_BGR2GRAY)
        img6=cv2.bitwise_not(img6)
        cv2.imwrite('gray3.jpg',img6)
        third_grayimg='gray3.jpg'

        first_option=pytesseract.image_to_string(first_grayimg, lang='eng')
        second_option=pytesseract.image_to_string(second_grayimg, lang='eng')
        third_option=pytesseract.image_to_string(third_grayimg, lang='eng')
        p_first=cleanText(first_option)
        p_second=cleanText(second_option)
        p_third=cleanText(third_option)

        a=(p_first.split())
        b=(p_second.split())
        c=(p_third.split())
        print(a)
        print(b)
        print(c)
        print("-----")


        if a[0] == 'INT' and a[1] == '+6%':
            if b[0] == 'INT' and b[1] == '+3%':
                    break
            if c[0] == 'INT' and c[1] == '+3%':
                    break
            if b[0] == 'INT' and b[1] == '+6%':
                    break
            if c[0] == 'INT' and c[1] == '+6%':
                    break
        if b[0] == 'INT' and b[1] == '+6%':
            if c[0] == 'INT' and c[1] == '+3%':
                    break
            if c[0] == 'INT' and c[1] == '+6%':
                    break
     except IndexError:
            continue
def LUKsetting():
    while True:
     try:
        if keyboard.is_pressed('Esc'):
                        print("STOP")
                        break
        click()
        time.sleep(1.0)
        pytesseract.pytesseract.tesseract_cmd = directory

        first_option_pos = {'left': 600, 'top': 427, 'width': 130, 'height': 16}
        second_option_pos = {'left': 600, 'top': 441, 'width': 130, 'height': 16}
        third_option_pos = {'left': 600, 'top': 454, 'width': 130, 'height': 16}



        with mss.mss() as sct:
            first_img = np.array(sct.grab(first_option_pos))[:,:,:3]
            second_img = np.array(sct.grab(second_option_pos))[:,:,:3]
            third_img = np.array(sct.grab(third_option_pos))[:,:,:3]


        cv2.imwrite('first_screen.jpg',first_img)
        Number1='first_screen.jpg'
        img1=cv2.imread(Number1,cv2.IMREAD_COLOR)
        img2=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
        img2=cv2.bitwise_not(img2)
        cv2.imwrite('gray1.jpg',img2)
        first_grayimg='gray1.jpg'

        cv2.imwrite('second_screen.jpg',second_img)
        Number2='second_screen.jpg'
        img3=cv2.imread(Number2,cv2.IMREAD_COLOR)
        img4=cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
        img4=cv2.bitwise_not(img4)
        cv2.imwrite('gray2.jpg',img4)
        second_grayimg='gray2.jpg'

        cv2.imwrite('third_screen.jpg',third_img)
        Number3='third_screen.jpg'
        img5=cv2.imread(Number3,cv2.IMREAD_COLOR)
        img6=cv2.cvtColor(img5,cv2.COLOR_BGR2GRAY)
        img6=cv2.bitwise_not(img6)
        cv2.imwrite('gray3.jpg',img6)
        third_grayimg='gray3.jpg'

        first_option=pytesseract.image_to_string(first_grayimg, lang='eng')
        second_option=pytesseract.image_to_string(second_grayimg, lang='eng')
        third_option=pytesseract.image_to_string(third_grayimg, lang='eng')
        p_first=cleanText(first_option)
        p_second=cleanText(second_option)
        p_third=cleanText(third_option)

        a=(p_first.split())
        b=(p_second.split())
        c=(p_third.split())
        print(a)
        print(b)
        print(c)
        print("-----")


        if a[0] == 'LUK' and a[1] == '+6%':
            if b[0] == 'LUK' and b[1] == '+3%':
                    break
            if c[0] == 'LUK' and c[1] == '+3%':
                    break
            if b[0] == 'LUK' and b[1] == '+6%':
                    break
            if c[0] == 'LUK' and c[1] == '+6%':
                    break
        if b[0] == 'LUK' and b[1] == '+6%':
            if c[0] == 'LUK' and c[1] == '+3%':
                    break
            if c[0] == 'LUK' and c[1] == '+6%':
                    break
     except IndexError:
            continue

def HPsetting():
    while True:
     try:
        if keyboard.is_pressed('Esc'):
                        print("STOP")
                        break
        click()
        time.sleep(1.0)
        pytesseract.pytesseract.tesseract_cmd = directory

        first_option_pos = {'left': 600, 'top': 427, 'width': 130, 'height': 16}
        second_option_pos = {'left': 600, 'top': 441, 'width': 130, 'height': 16}
        third_option_pos = {'left': 600, 'top': 454, 'width': 130, 'height': 16}



        with mss.mss() as sct:
            first_img = np.array(sct.grab(first_option_pos))[:,:,:3]
            second_img = np.array(sct.grab(second_option_pos))[:,:,:3]
            third_img = np.array(sct.grab(third_option_pos))[:,:,:3]


        cv2.imwrite('first_screen.jpg',first_img)
        Number1='first_screen.jpg'
        img1=cv2.imread(Number1,cv2.IMREAD_COLOR)
        img2=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
        img2=cv2.bitwise_not(img2)
        cv2.imwrite('gray1.jpg',img2)
        first_grayimg='gray1.jpg'

        cv2.imwrite('second_screen.jpg',second_img)
        Number2='second_screen.jpg'
        img3=cv2.imread(Number2,cv2.IMREAD_COLOR)
        img4=cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
        img4=cv2.bitwise_not(img4)
        cv2.imwrite('gray2.jpg',img4)
        second_grayimg='gray2.jpg'

        cv2.imwrite('third_screen.jpg',third_img)
        Number3='third_screen.jpg'
        img5=cv2.imread(Number3,cv2.IMREAD_COLOR)
        img6=cv2.cvtColor(img5,cv2.COLOR_BGR2GRAY)
        img6=cv2.bitwise_not(img6)
        cv2.imwrite('gray3.jpg',img6)
        third_grayimg='gray3.jpg'

        first_option=pytesseract.image_to_string(first_grayimg, lang='eng')
        second_option=pytesseract.image_to_string(second_grayimg, lang='eng')
        third_option=pytesseract.image_to_string(third_grayimg, lang='eng')
        p_first=cleanText(first_option)
        p_second=cleanText(second_option)
        p_third=cleanText(third_option)

        a=(p_first.split())
        b=(p_second.split())
        c=(p_third.split())
        print(a)
        print(b)
        print(c)
        print("-----")


        if a[1] == 'HP' and a[2] == '+6%':
            if b[1] == 'HP' and b[2] == '+3%':
                    break
            if c[1] == 'HP' and c[2] == '+3%':
                    break
            if b[1] == 'HP' and b[2] == '+6%':
                    break
            if c[1] == 'HP' and c[2] == '+6%':
                    break
        if b[0] == 'HP' and b[1] == '+6%':
            if c[0] == 'HP' and c[1] == '+3%':
                    break
            if c[0] == 'HP' and c[1] == '+6%':
                    break
     except IndexError:
            continue

window = Tk()
window.title("9% tool")

l2 = Label(window, text='수상한 큐브 9퍼 제작툴', font=("맑은 고딕",20))
l2.grid(row = 0, column = 1)
em = Label(window, text='')
em.grid(row = 1, column = 1)
b1= Button(window, text="  STR 9%  ", command=STRsetting, font=("맑은 고딕",15))
b1.grid(row = 2, column = 1)
em1 = Label(window, text='')
em1.grid(row = 3, column = 1)
b2= Button(window, text="  DEX 9%  ", command=DEXsetting, font=("맑은 고딕",15))
b2.grid(row = 4, column = 1)
em2 = Label(window, text='')
em2.grid(row = 5, column = 1)
b3= Button(window, text="  INT 9%  ", command=INTsetting, font=("맑은 고딕",15))
b3.grid(row = 6, column = 1)
em3 = Label(window, text='')
em3.grid(row = 7, column = 1)
b4= Button(window, text="  LUK 9%  ", command=LUKsetting, font=("맑은 고딕",15))
b4.grid(row = 8, column = 1)
em4 = Label(window, text='')
em4.grid(row = 9, column = 1)
b5= Button(window, text="  HP 9%  ", command=HPsetting, font=("맑은 고딕",15))
b5.grid(row = 10, column = 1)
em5 = Label(window, text='')
em5.grid(row = 11, column = 1)

aimg = PhotoImage(file = "screenshot.png")
p1 = Label(window, image=aimg)
p1.grid(row = 13, column = 1)

w1 = Label(window, text='위 사진 처럼 마우스를 가져다대고,')
w1.grid(row = 14, column = 1)
w2 = Label(window, text='그후에 왼쪽 최상단으로 끌어서 맞춰주시기 바랍니다.')
w2.grid(row = 15, column = 1)
w3 = Label(window, text='본프로그램은 창모드 1366 x 768 해상도에서만')
w3.grid(row = 16, column = 1)
w4 = Label(window, text='작동합니다. 작동중에는 다른 동작 혹은')
w4.grid(row = 17, column = 1)
w5 = Label(window, text=' 메이플창 위에 다른 창을 띄우지 마시기')
w5.grid(row = 18, column = 1)
w6 = Label(window, text='바랍니다.')
w6.grid(row = 19, column = 1)
w5 = Label(window, text=' ')
w5.grid(row = 20, column = 1)
w5 = Label(window, text='현재 올스텟 +3%을 읽지 못하는 에러가 있습니다 ')
w5.grid(row = 21, column = 1)
w6 = Label(window, text='추후 개선될 예정이나, 워낙확률이 낮기때문에 ')
w6.grid(row = 22, column = 1)
w5 = Label(window, text='크게 신경쓰지 않으셔도됩니다.')
w5.grid(row = 23, column = 1)
w5 = Label(window, text=' ')
w5.grid(row = 24, column = 1)
w6 = Label(window, text='Esc 키를 꾹 눌러 강제종료 가능합니다.')
w6.grid(row = 25, column = 1)
w6 = Label(window, text='Made By 로슈//재배포를 엄격히 금합니다.')
w6.grid(row = 26, column = 1)


window.mainloop()
