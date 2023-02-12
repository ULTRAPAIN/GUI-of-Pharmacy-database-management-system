print("welcome to pharmacy managemnet system")
from tkinter import *                              #--> Imported all tkinder modules 
from PIL import Image,ImageTk #--> PIL is a module which is  a python imaging libray
from tkinter import messagebox
import pymysql
import sys


tcet_root=Tk()
tcet_root.title("25-28{GUI}-Project")
height = tcet_root.winfo_screenheight() #--># getting screen's height
print(height)
width = tcet_root.winfo_screenwidth()   #--># getting screen's width 
print(width)
tcet_root.geometry("1536x864")
tcet_root.minsize(1536,864)
tcet_root.maxsize(1536,864)

def pharma(s):
    s.destroy()
    tcet_root.destroy()
    import test2

def signup():
    tcet_root.destroy()
    import main2

def signin():
    username=user.get()
    password=pass1.get()
    
    if username=="Username" and password=="Password":
        messagebox.showerror("Error","All fields are Required")
        
    elif username==""  and  password=="":
        messagebox.showerror("Invalid","PLEASE ENTER username and password ")
    
    elif username=="" and password!="":
        messagebox.showerror("Invalid","PLEASE ENTER your username! ")
    
    elif username!=""  and  password=="":
        messagebox.showerror("Invalid","PLEASE ENTER your  password ")
    
    else:
        con=pymysql.connect(host="localhost",user="root",password="dasu",database="pythongui")
        cur=con.cursor()
        cur.execute("select * from signup where username=%s and password=%s",(user.get(),pass1.get()))
        row=cur.fetchone()
        if row==None:
            messagebox.showerror("Error","  invalid Username and Password")
        else:
            messagebox.showinfo("Success","Welcome")
            screen=Toplevel(tcet_root,width=500,height=400,border=0)
            screen.title("HELLO EVERYONE")
            screen.geometry("925x500+300+200")
            screen.config(bg="white")
            image1=Image.open("welcome.jpg")
            bg=ImageTk.PhotoImage(image1)  #--> Inserting photo
            lab3=Label(screen,image=bg)
            lab3.pack()
            Next=Button(screen,width=6,text="Next",border=0,bg="blue",cursor="hand2",fg="white",font=("Microsoft YaHei UI Light",11,"bold"),command=lambda:[pharma(screen)])
            Next.place(relx=0.5,rely=0.77,anchor=CENTER)

            screen.mainloop()
        
    
        
    
    

#converting jpg images to Png images by using ImageTk function
image=Image.open("8jpg.jpg")
BG=ImageTk.PhotoImage(image)  #--> Inserting photo
lab1=Label(image=BG)
lab1.pack()
f1=Frame(tcet_root,width=350,height=350,bg="blue",borderwidth=3,relief=SUNKEN)
f1.place(x=45,y=270)


header=Label(f1,text="Sign In",foreground="white",background="blue",font=("Microsoft YaHei UI Light",22,"bold"))
header.place(x=115,y=5)
#############################################-------------------------
def on_enter(e):
    user.delete(0,"end")

def on_leave(e):
    name=user.get()
    if name== "":
        user.insert(0,"Username")
#################################################
def on_enter1(e):
    pass1.delete(0,"end")

def on_leave1(e):
    name=pass1.get()
    if name== "":
        pass1.insert(0,"Password")

user =Entry(f1,width=32,fg="white",border=0,bg="blue",font=("Microsoft YaHei UI Light",11,"bold"))
user.place(x=28,y=75)
user.insert(0,"Username")
Frame(f1,width=295,height=3,bg="white").place(x=25,y=99)
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)
######################################

pass1 =Entry(f1,width=32,fg="white",border=0,bg="blue",font=("Microsoft YaHei UI Light",11,"bold"))
pass1.place(x=28,y=150)
pass1.insert(0,"Password")
Frame(f1,width=295,height=3,bg="white").place(x=25,y=175)
pass1.bind("<FocusIn>",on_enter1)
pass1.bind("<FocusOut>",on_leave1)

Button(f1,width=24,pady=7,text="Sign in",cursor="hand2",fg="white",height=1,bg="green",font=("Microsoft YaHei UI Light",13,"bold"),border=0,command=signin).place(x=36,y=195)
lab2=Label(f1,text="Dont have an Account ?",fg="white",bg="blue",font=("Microsoft YaHei UI Light",10,"bold"))
lab2.place(x=90,y=245)


signup1=Button(f1,width=6,text="Sign up",border=0,bg="blue",cursor="hand2",fg="white",font=("Microsoft YaHei UI Light",11,"bold"),command=signup)
signup1.place(x=138,y=268)






tcet_root.mainloop()   #This function is used to create a gui window
