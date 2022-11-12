from tkinter import *
import os

pcr = Tk()

pcr.geometry("700x600")

def ekle():

    os.system('kitapekle.py')


headingFrame1 = Frame(pcr,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text="Kütüphaneye Hoş Geldiniz", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(pcr, text="Kitap Ekle", bg='black', fg='white',command=ekle)
btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

btn2 = Button(pcr, text="Kitap sil", bg='black', fg='white')
btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

btn3 = Button(pcr, text="Kitapları gör", bg='black', fg='white')
btn3.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

btn4 = Button(pcr, text="Öğrenciye Kitap Ver", bg='black', fg='white')
btn4.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

btn5 = Button(pcr, text="Kitabı Geri Al", bg='black', fg='white')
btn5.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)


pcr.mainloop()
