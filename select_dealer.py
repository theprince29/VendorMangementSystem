import os
import sqlite3
from tkinter import*
from tkinter import ttk,messagebox
from turtle import width
from PIL import Image,ImageTk
import sqlite3
from dealer_info import Dealer_infoclass

class searchclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("300x200+220+130")
        self.root.title("Shop-Management System")
        self.root.config(bg="White")
        self.root.resizable(False,False)
        self.root.focus_force()

        lbl_utype=Label(self.root,text="Enter-Password",bg="white",font=("times new roman",15)).place(x=90,y=20)
        self.txt_utype=Entry(self.root,justify=CENTER,font=("goudy old style",15),bg="light gray")
        self.txt_utype.place(x=65,y=60,width=180)
        btn_add=Button(self.root,text="Proceed",command=self.search,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=100,y=100,width=110,height=28)

    def search(self):
        con=sqlite3.connect(database=r'sms.db')
        cur=con.cursor()
        try:
            if self.txt_utype.get()=="":
                messagebox.showerror("Error","Password must be Required!!",parent=self.root) 
            else:
                cur.execute("select * from dealer where password=?",(self.txt_utype.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.DealerTable.delete(*self.DealerTable.get_children())
                    self.DealerTable.insert('',END,values=row)
                    self.root.destroy()
                    os.system("python dealer_info.py")
                else:
                    messagebox.showerror("Error","No Record Found!!!",parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

if __name__=="__main__":
    root=Tk()
    obj=searchclass(root)
    root.mainloop()