import os
import sqlite3
from tkinter import*
from tkinter import ttk,messagebox
from turtle import width
from PIL import Image,ImageTk
import sqlite3
from dealer_info import Dealer_infoclass
from customer import customerclass

class searchclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1522x783+0+0")
        self.root.title("Shop-Management System")
        self.root.config(bg="blue")
        self.root.resizable(False,False)
        self.root.focus_force()
        title=Label(self.root,text=" नमस्ते ! \nWelcome to the Technical Era of Dropshipping\nHope You will Enjoying a Lot",font=("goudy old style",25,"bold"),bg="blue",fg="yellow").place(x=400,y=40)
        title=Label(self.root,text="If you have any suggestions regarding imporvement then please let share with us\nयदि आपके पास सुधार के संबंध में कोई सुझाव है तो कृपया हमारे साथ साझा करें :-",font=("goudy old style",15,"bold"),bg="blue",fg="yellow").place(x=250,y=700)

        self.menulogo=Image.open("Images/fti.png")
        self.menulogo=self.menulogo.resize((240,40),Image.ANTIALIAS)
        self.menulogo=ImageTk.PhotoImage(self.menulogo)

        lbl_menulogo=Label(self.root,image=self.menulogo,bg="blue")
        lbl_menulogo.place(x=900,y=710)


        self.logo=Image.open("Images/category.jpg")
        self.logo=self.logo.resize((550,350),Image.ANTIALIAS)
        self.logo=ImageTk.PhotoImage(self.logo)

        lbl_logo=Label(self.root,image=self.logo,bg="blue")
        lbl_logo.place(x=450,y=260)

        btn_Registers=Button(self.root,text="o o o  आगे बढेंं / Next =>",command=self.customers,bg="blue",font=("times new roman",15,"italic","bold"),bd=0,cursor="hand2",fg="white").place(x=570,y=200,width=280,height=40)

        btn_cancel=Button(self.root,text="[] [] [] रद्द करें / Destroy Page =>",command=self.cancel,bg="blue",font=("times new roman",15,"italic","bold"),bd=0,cursor="hand2",fg="white").place(x=1200,y=10,width=280,height=40)
        

    def customers(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=customerclass(self.new_win) 

    def cancel(self):
        messagebox.showinfo("Thanks!","पधारने के लिए धन्यवाद !\n आपका दिन शुभ हो",parent=self.root)
        self.root.destroy()
        os.system("python first.py")

if __name__=="__main__":
    root=Tk()
    obj=searchclass(root)
    root.mainloop()