from tkinter import *
from tkinter import ttk #them of tk
from tkinter import messagebox

GUI= Tk() #หน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') #ชื่อโปรแกรม
GUI.geometry('500x400') #ขนาดของจอ

L1=Label(GUI,text='Program Python',font=('Angsana New',30),fg='green')
L1.pack(ipadx=10,ipady=10)
######################
def Button1():
    text = 'ตอนนี้มีเงินบัญชีอยู่ 300 บาท'
    messagebox.showinfo('เงินในบัญชี',text) #แจ้งเตือน

FB1=Frame(GUI)#กระดาน
FB1.place(x=100,y=100)
B2=ttk.Button(FB1,text='เงินมีอยู่กี่บาท',command=Button1) #แสดงปุ่ม
B2.pack(ipadx=20,ipady=20)
########################
def Button2():
    text = '123456'
    messagebox.showinfo('เลขบัญชี',text) #แจ้งเตือน

FB1=Frame(GUI)#กระดาน
FB1.place(x=100,y=200)
B2=ttk.Button(FB1,text='เลขบัญชีธนาคาร',command=Button2) #แสดงปุ่ม
B2.pack(ipadx=20,ipady=20)
########################
def Button3():
    text = 'SCB'
    messagebox.showinfo('ธนาคาร',text) #แจ้งเตือน

FB1=Frame(GUI)#กระดาน
FB1.place(x=100,y=300)
B2=ttk.Button(FB1,text='ชื่อธนาคาร',command=Button3) #แสดงปุ่ม
B2.pack(ipadx=20,ipady=20)
########################


GUI.mainloop()
