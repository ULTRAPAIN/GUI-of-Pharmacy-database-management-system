from tkinter import *                              #--> Imported all tkinder modules 
from PIL import Image,ImageTk #--> PIL is a module which is  a python imaging libray
from tkinter import messagebox
import pymysql

tcet_root=Tk()
tcet_root.title("25-28{GUI}-Project")
height = tcet_root.winfo_screenheight() #--># getting screen's height
print(height)
width = tcet_root.winfo_screenwidth()   #--># getting screen's width 
print(width)
tcet_root.geometry("1536x864")
tcet_root.minsize(1536,864)
tcet_root.maxsize(1536,864)

def clear():
    user.delete(0,END)
    pass1.delete(0,END)
    pass2.delete(0,END)
    
def signin():
    tcet_root.destroy()
    import main
    
    
    
def signup():
        username=user.get()
        password=pass1.get()
        cp=pass2.get()
        
        if username=="Username"  and  password=="Password" and cp=="Confirm Password":
            messagebox.showerror("Invalid","PLEASE ENTER ALL THE FIELDS")
        
        elif (username!=""  and password=="Password" )and cp=="Confirm Password" :
            messagebox.showerror("Invalid","Enter  Password and Confirm Password")
        
        elif (username=="Username"  and password!="" )and cp=="Confirm Password" :
            messagebox.showerror("Invalid","Enter Username and Confirm Password")
        
        elif (username=="Username"  and password=="Password" )and cp!="" :
            messagebox.showerror("Invalid","Enter user name and  Password")
    
            
        elif (username=="Username"  and password!="" )and cp!="" :
            messagebox.showerror("Invalid","Enter Username")
            
        elif username!=""  and password!="" and cp!=password:
            messagebox.showerror("Invalid","Password Mismatch")
        
        else:
            con=pymysql.connect(host="localhost",user="root",password="dasu",database="pythongui")
            cur=con.cursor()
            cur.execute('select * from signup where username=%s',user.get())
            row=cur.fetchone()
            if row!=None:
                messagebox.showerror("Error","User Alreadyy Exists")
            else:
                cur.execute("insert into signup(username,password,cp) values(%s,%s,%s)",(user.get(),pass1.get(),pass2.get()))
                con.commit()
                con.close()
                messagebox.showinfo("Success","Your Account is created")
                clear()
                tcet_root.destroy()
                import main
            
            
        
         
#converting jpg images to Png images by using ImageTk function
image=Image.open("9.jpg")
BG=ImageTk.PhotoImage(image)  #--> Inserting photo
lab1=Label(image=BG)
lab1.pack()
f1=Frame(tcet_root,width=350,height=375,bg="blue",borderwidth=3,relief=SUNKEN)
f1.place(x=70,y=270)

header=Label(f1,text="Sign Up",foreground="white",background="blue",font=("Microsoft YaHei UI Light",22,"bold"))
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
##################################################
def on_enter2(e):
    pass2.delete(0,"end")

def on_leave2(e):
    name=pass2.get()
    if name=="":
        pass2.insert(0,"Confirm Password")
        

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


pass2 =Entry(f1,width=32,fg="white",border=0,bg="blue",font=("Microsoft YaHei UI Light",11,"bold"))
pass2.place(x=28,y=225)
pass2.insert(0,"Confirm Password")
Frame(f1,width=295,height=3,bg="white").place(x=25,y=251)
pass2.bind("<FocusIn>",on_enter2)
pass2.bind("<FocusOut>",on_leave2)


Button(f1,width=24,pady=7,text="Sign Up",cursor="hand2",fg="white",height=1,bg="green",font=("Microsoft YaHei UI Light",13,"bold"),border=0,command=signup).place(x=36,y=271)
lab2=Label(f1,text="I have an Account ?",fg="white",bg="blue",font=("Microsoft YaHei UI Light",10,"bold"))
lab2.place(x=50,y=325)


signin1=Button(f1,width=6,text="Sign In",border=0,bg="blue",cursor="hand2",fg="white",font=("Microsoft YaHei UI Light",11,"bold"),command=signin)
signin1.place(x=195,y=322)






tcet_root.mainloop()   #This function is used to create a gui window
