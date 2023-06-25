from tkinter import*
from PIL import Image,ImageTk
import os
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("WELCOME PAGE")
        self.root.geometry("1522x783+0+0")
        self.root.config(bg="White")
        self.root.resizable(False,False)

        # Adding Background----
        self.logo=Image.open("Images/welcome.png")
        self.logo=self.logo.resize((1522,783),Image.ANTIALIAS)
        self.logo=ImageTk.PhotoImage(self.logo)
        lbl_logo=Label(self.root,image=self.logo,)
        lbl_logo.place(x=0,y=0)


        btn_Registers=Button(self.root,text="Let's Dive Into The Marthon of Life -->",command=self.welcome,bg="light blue",font=("times new roman",12,"italic","underline","bold"),bd=0,cursor="hand2",fg="blue").place(x=800,y=555)

    def welcome(self):
        self.root.destroy()
        os.system("python login.py")

if __name__=="__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()