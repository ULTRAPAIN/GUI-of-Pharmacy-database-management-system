from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
from tkinter.ttk import Entry
from tkinter import Entry
def signin():
    root.destroy()
    import main

class Pharmacymanagementsystem:
    
    
    def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1550x800+0+0")

#----------------------------------------------MAKING THE GUI---------------------------------------------

# variables for RHS table
        self.refno_var=StringVar()
        self.MedName_var=StringVar()
# ADDING THE LABEL        
        lbl=Label(self.root,text="24/7 TCET PHARMA",bg="blue",fg="white",bd=15,relief=RIDGE,font=("times new roman",40,"bold"),padx=4,pady=4)
        lbl.pack(side=TOP,fill=X)

# ADDING THE LOGO
        logo=Image.open("logo2.png")
        logo=logo.resize((70,65),Image.ANTIALIAS)
        self.photologo=ImageTk.PhotoImage(logo)
        logobtn=Button(self.root,image=self.photologo,borderwidth=0,command=signin)
        logobtn.place(x=25,y=15)
        
#=========================================DATA FRAME====================================================        
        maindf=Frame(self.root,bd=15,relief=RIDGE,padx=20,bg="blue")
        maindf.place(x=0,y=120,width=1530,height=400)
        
#SUB-FRAME TO THE LEFT OF THE MAIN FRAME
        leftSF=LabelFrame(maindf,bd=10,relief=RIDGE,padx=20,text="MEDICINE INFORMATION",fg="darkgreen",font=("ARIAL",12,"bold"))
        leftSF.place(x=0,y=5,width=900,height=350)
        
#SUB-FRAME TO THE RIGHT OF THE MAIN FRAME
        rightSF=LabelFrame(maindf,bd=10,relief=RIDGE,padx=20,text=" NEW MEDICINE ADD  ",fg="darkgreen",font=("ARIAL",12,"bold"))
        rightSF.place(x=910,y=5,width=540,height=350)
        
#ADDING BUTTONS FRAME TO THE BOTTOM
        btnframe=Frame(self.root,bd=15,relief=GROOVE,padx=20)
        btnframe.place(x=0,y=520,width=1530,height=65)
        
        #------------------ADDING THE BUTTONS------------------------
        #add-button
        addbtn=Button(btnframe,text="ADD-MEDICINE",font=("arial",12,"bold"),bg="blue",fg="white")
        addbtn.grid(row=0,column=0)
        #update-button
        updatebtn=Button(btnframe,text="UPDATE",font=("arial",13,"bold"),width=14,bg="blue",fg="white")
        updatebtn.grid(row=0,column=1)
        #delete-button
        deletebtn=Button(btnframe,text="DELETE",font=("arial",13,"bold"),width=14,bg="red",fg="white")
        deletebtn.grid(row=0,column=2)
        #reset-button
        resetbtn=Button(btnframe,text="RESET",font=("arial",13,"bold"),width=14,bg="blue",fg="white")
        resetbtn.grid(row=0,column=3)
        #exit-button
        exitbtn=Button(btnframe,text="EXIT",font=("arial",13,"bold"),width=14,bg="blue",fg="white")
        exitbtn.grid(row=0,column=4)
        #search-button
        searchlbl=Label(btnframe,font=("arial",17,"bold"),text="SEARCH BY",padx=2,bg="red",fg="white")
        searchlbl.grid(row=0,column=5,sticky=W)
        
#searchbox

        ref_combobox=ttk.Combobox(btnframe,width=12,font=("arial",17,"bold"),state="readonly")
        ref_combobox["values"]=("Ref_no","medname","Lot")
        ref_combobox.grid(row=0,column=6)
        ref_combobox.current(0)
        
#var
        searchbox=Entry(btnframe,bd=3,relief=RIDGE,width=13,font=("arial",17,"bold"))
        searchbox.grid(row=0,column=7)
        #search-button
        searchbtn=Button(btnframe,text="SEARCH",font=("arial",13,"bold"),width=13,bg="blue",fg="white")
        searchbtn.grid(row=0,column=8)
        #show-all-button
        showallbtn=Button(btnframe,text="SHOW ALL",font=("arial",13,"bold"),width=9,bg="blue",fg="white")
        showallbtn.grid(row=0,column=9)
        
#-------------ADDING THE LABELS & ENTRY-BOX--------------------------
    #reference tag
    
        conn=mysql.connector.connect(host="localhost",username="root",password="dasu",database="pythongui")
        my_cursor=conn.cursor()
        my_cursor.execute("select ref from pharma")
        row=my_cursor.fetchall()
    
        refnolbl=Label(leftSF,text="Reference no :",padx=2,font=("arial",12,"bold"),pady=6)
        refnolbl.grid(row=0,column=0,sticky=W)

        
#reference-combobox
        ref_combobox=ttk.Combobox(leftSF,width=27,font=("arial",12,"bold"),state="readonly")
        ref_combobox["values"]=("Ref_no","medname","Lot")
        ref_combobox.grid(row=0,column=1)
        ref_combobox.current(0)
        
#company-name tag
        compnamelbl= Label(leftSF,text='Company Name:',padx=2,pady=6,font=("arial",12,"bold"))
        compnamelbl.grid(row=1, column=0, sticky=W)  
        #company-name entrybox    
        comp_entrybox=Entry(leftSF,bd=2,relief=RIDGE, width=29,font=("arial",12,"bold"))
        comp_entrybox.grid(row=1,column=1)

#type of medicine
        typmedlbl = Label(leftSF, text='Type of Medicine',padx=2,pady=6,font=("arial",12,"bold"))
        typmedlbl.grid(row=2, column=0, sticky=W)
        #combobox- medicine label
        typmedlbl_combo = ttk.Combobox(leftSF,width=27,font=("arial",12,"bold"), state='readonly',)
        typmedlbl_combo['values']=('Tablet', 'Liquid','Capsules','Topical Medicine','Drops','Inhales')
        typmedlbl_combo.grid(row=2, column=1)
        typmedlbl_combo.current(0)

#medicine-name tag
        mednamelbl= Label(leftSF,text='Medicine Name:',padx=2,pady=6,font=("arial",12,"bold"))
        mednamelbl.grid(row=3, column=0, sticky=W)  
        #adding the connection to mysql pharamacy table from database pythongui
        
        #medicine-name entrybox    
        medname_entrybox= ttk.Combobox(leftSF, width=27,font=("arial",12,"bold"),state="readonly")
        medname_entrybox["value"]=("med") 
        medname_entrybox.current(0)
        medname_entrybox.grid(row=3,column=1)

#lot-no tag
        lotno_lbl= Label(leftSF,text='Lot No:',padx=2,pady=6,font=("arial",12,"bold"))
        lotno_lbl.grid(row=4, column=0, sticky=W)  
        #company-name entrybox    
        lotno_entrybox= Entry(leftSF,bd=2, relief = RIDGE, width=29,font=("arial",12,"bold"))
        lotno_entrybox.grid(row=4,column=1)

#Issue-date label
        issuedate_lbl= Label(leftSF,text='Issue Date.:',padx=2,pady=6,font=("arial",12,"bold"))
        issuedate_lbl.grid(row=5, column=0, sticky=W)  
        #issuedate entrybox    
        issuedate_entrybox= Entry(leftSF,bd=2, relief = RIDGE, width=29,font=("arial",12,"bold"))
        issuedate_entrybox.grid(row=5,column=1)

#expiry-date tag
        expirydate_lbl= Label(leftSF,text='Expiry-date:',padx=2,pady=6,font=("arial",12,"bold"))
        expirydate_lbl.grid(row=6, column=0, sticky=W)  
        #expiry-date entrybox    
        expirydate_entrybox= Entry(leftSF,bd=2, relief = RIDGE, width=29,font=("arial",12,"bold"))
        expirydate_entrybox.grid(row=6,column=1)

#uses tag
        uses_lbl= Label(leftSF,text='Uses:',padx=2,pady=4,font=("arial",12,"bold"))
        uses_lbl.grid(row=7, column=0, sticky=W)  
        #uses entrybox    
        uses_entrybox= Entry(leftSF,bd=2, relief = RIDGE, width=29,font=("arial",12,"bold"))
        uses_entrybox.grid(row=7,column=1)

#side-effect tag
        sideeffect_lbl= Label(leftSF,text='Side-Effect:',padx=2,pady=6,font=("arial",12,"bold"))
        sideeffect_lbl.grid(row=8, column=0, sticky=W)  
        #company-name entrybox    
        sideeffect_entrybox= Entry(leftSF,bd=2, relief = RIDGE, width=29,font=("arial",12,"bold"))
        sideeffect_entrybox.grid(row=8,column=1)

#prescription & Warning
        PW_lbl= Label(leftSF,text='Prec&Warning:',padx=15,font=("arial",12,"bold"))
        PW_lbl.grid(row=0, column=2, sticky=W)
        #prescription & warning entrybox   
        PW_lbl= Entry(leftSF,font=("arial",12,"bold"),bg='white',bd=2,relief= RIDGE,width=29)
        PW_lbl.grid(row=0, column=3)

#Dosage
        dosage_lbl= Label(leftSF,text='Dosage:',padx=15 ,pady=6,font=("arial",12,"bold"))
        dosage_lbl.grid(row=1,column=2, sticky=W)
        #dosage  entrybox   
        dosage= Entry(leftSF,font=("arial",12,"bold"),bg='white',bd=2,relief= RIDGE,width=29)
        dosage.grid(row=1,column=3)

#tablet price
        TbltPrice_lbl= Label(leftSF,text="Tablet Price: ",padx=15 ,pady=6,font=("arial",12,"bold"))
        TbltPrice_lbl.grid(row=2, column=2, sticky=W)
        #tablet price entrybox   
        TbltPrice_lbl= Entry(leftSF,font=("arial",12,"bold"),bg='white',bd=2,relief= RIDGE,width=29)
        TbltPrice_lbl.grid(row=2,column=3)

#Product-QT 
        ProductQT_lbl= Label(leftSF,text="Product QT: ",padx=15 ,pady=6,font=("arial",12,"bold"))
        ProductQT_lbl.grid(row=3, column=2, sticky=W)
        #Product-QT entrybox   
        ProductQT_lbl= Entry(leftSF,font=("arial",12,"bold"),bg='white',bd=2,relief= RIDGE,width=29)
        ProductQT_lbl.grid(row=3,column=3)

#adding the images
#tagline
        tagline= Label(leftSF,text='EAT HEALTHY - STAY HEALTHY',padx=2,pady=6,font=('arial',12,'bold'),bg="white",fg="black",width=37)
        tagline.place(x=430,y=140)

#img-1
        img1=Image.open("11.jpg")
        img1=img1.resize((150,135),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.photoimg1,borderwidth=0)
        b1.place(x=475,y=330)
#img-2
        img2=Image.open("12.jpg")
        img2=img2.resize((150,135),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        b1=Button(self.root,image=self.photoimg2,borderwidth=0)
        b1.place(x=620,y=330)
 #img-3
        img3=Image.open("13.jpg")
        img3=img3.resize((130,130),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        b1=Button(self.root,image=self.photoimg3,borderwidth=0)
        b1.place(x=770,y=330)

#SUB-FRAME TO THE RIGHT OF THE MAIN FRAME

        rightSF=LabelFrame(maindf,bd=10,relief=RIDGE,padx=20,text="NEW MEDICINE",fg="darkgreen",font=("arial",12,"bold"))
        rightSF.place(x=910,y=5,width=540,height=350)

#Adding the images
#img-4
        img4=Image.open("14.jpg")
        img4=img4.resize((200,75),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(self.root,image=self.photoimg4,borderwidth=0)
        b1.place(x=960,y=160)
#img-5
        img5=Image.open("10.jpg")
        img5=img5.resize((200,75),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b1=Button(self.root,image=self.photoimg5,borderwidth=0)
        b1.place(x=1160,y=160)

# Adding the labels
            #reference number
        refno_lbl= Label(rightSF,text='Reference No:',pady=6,font=('arial',12,'bold'))
        refno_lbl.place(x=0,y=80)
            #entry-box
        refno_box= Entry(rightSF,textvariable=self.refno_var,font=('arial',12,'bold'),bg='white',bd=2,relief= RIDGE,width=14)
        refno_box.place(x=135,y=80)
        global ref_val
        global med_value
        ref_val = refno_box.get()
        

            #medicine name
        med_lbl= Label(rightSF, text='Medicine Name:',pady=6,font=('arial',12,'bold'))
        med_lbl.place(x=0,y=110)
            #entry-box
        med_entry= Entry(rightSF,textvariable=self.MedName_var,font=('arial',12,'bold'), bg='white',bd=2,relief= RIDGE,width=14)
        med_entry.place(x=135,y=111)
        med_value =med_entry.get()
# Adding the entry-table
#creating the frame
        table_frame= Frame(rightSF, bd=4, relief=RIDGE,bg="white")
        table_frame.place(x=0,y=150, width=290,height=160)
        
        sc_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y=ttk.Scrollbar(table_frame, orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)

        self.medicine_table=ttk.Treeview(table_frame,column=("ref","med-name"), xscrollcommand= sc_x.set,yscrollcommand= sc_y.set)
        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)
        
        self.medicine_table.heading('ref',text="Reference")
        self.medicine_table.heading('med-name',text="Medicine-Name")
        
        self.medicine_table["show"]="headings"   
        self.medicine_table.pack(fill=BOTH, expand=1)
        
        self.medicine_table.column("ref", width=100)
        self.medicine_table.column("med-name", width=100)  
        
        
        
        
#ADDING THE BUTTONS
# creating the frame to set the buttons

        frame=Frame(rightSF,bd=4, relief=RIDGE, bg='blue')
        frame.place(x=330, y=150, width=135,height=145)

#adding the buttons
        add_btn= Button(frame,text='ADD',bg='green',width=12,command=lambda: [addbtn(self)], fg='black',font=('helvetica',12,'bold'),pady=2)
        add_btn.grid(row=0,column=0)

        update_btn= Button(frame,text='UPDATE',bg='purple',width=12,fg='black',font=('helvetica',12,'bold'),pady=2)
        update_btn.grid(row=1,column=0)

        delete_btn= Button(frame,text='DELETE',bg='red',width=12,fg='black',font=('helvetica',12,'bold'),pady=2)
        delete_btn.grid(row=2,column=0)

        clear_btn= Button(frame, text='CLEAR',bg='blue',width=12,fg='black', font=('helvetica',12,'bold'),pady=2)
        clear_btn.grid(row=3,column=0)


#ADDING THE DATABASE FRAME
        database_frame=Frame(self.root, bd=15, relief=RIDGE)
        database_frame.place(x=0,y=580, width=1530,height=240)



#MAIN TABLE AND SCROLLBAR
        table_frame=Frame(database_frame,bd=15, relief=RIDGE)
        table_frame.place(x=0,y=1,width=1500,height=180)
        
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y=ttk.Scrollbar(table_frame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        self.pharmacy_table=ttk.Treeview(table_frame, column=("ref","companyname","type","tabletname","lotno","issuedate",
                                                             "expdate","uses","sideeffect","warning","dosage","price",
                                                              "productqt"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        
                                        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=BOTTOM, fill=Y)

        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)
        
        self.pharmacy_table['show']="headings"
        
        self.pharmacy_table.heading("ref",text="Reference No")
        self.pharmacy_table.heading("companyname",text="Company Name")
        self.pharmacy_table.heading("type",text="Med Type")
        self.pharmacy_table.heading("tabletname",text="Medicine Name")
        self.pharmacy_table.heading("lotno",text="Lot No.")
        self.pharmacy_table.heading("issuedate",text="Issue Date")
        self.pharmacy_table.heading("expdate",text="Expiry-Date")
        self.pharmacy_table.heading("uses",text="Uses")
        self.pharmacy_table.heading("sideeffect",text="Side-Effect")
        self.pharmacy_table.heading("warning",text="Prec & Wrning")
        self.pharmacy_table.heading("dosage",text="Dosage")
        self.pharmacy_table.heading("price",text="Price")
        self.pharmacy_table.heading("productqt",text="Product QTs")
        self.pharmacy_table.pack(fill=BOTH,expand=1)
        
        self.pharmacy_table.column("ref",width=100)
        self.pharmacy_table.column("companyname",width=100)
        self.pharmacy_table.column("type",width=100)
        self.pharmacy_table.column("tabletname",width=100)
        self.pharmacy_table.column("lotno",width=100)
        self.pharmacy_table.column("issuedate",width=100)
        self.pharmacy_table.column("expdate",width=100)
        self.pharmacy_table.column("uses",width=100)
        self.pharmacy_table.column("sideeffect",width=100)
        self.pharmacy_table.column("warning",width=100)
        self.pharmacy_table.column("dosage",width=100)
        self.pharmacy_table.column("price",width=100)
        self.pharmacy_table.column("productqt",width=100)
        
        
        
        def addbtn(self):
                print("I am under add button")
                conn=mysql.connector.connect(host="localhost",username="root",password="dasu",database="pythongui")
                my_cursor=conn.cursor()
                print(f"ref no = {ref_val} ")
                my_cursor.execute("insert into pharma (ref,medname)values(%s,%s)",(self.refno_var.get(),self.MedName_var.get()))
                conn.commit()
              
                conn.close()
                messagebox.showinfo("success","Medicine added")
                
                
      
#         btnframe=Frame(self.root,bd=15,relief=RIDGE,bg="green")
#         btnframe.place(x=0,y=580,width=1530,height=210)
        
#         #------------------ADDING THE BUTTONS------------------------
#         #add-button
#         addbtn=Button(btnframe,text="ADD-MEDICINE",font=("helvetica",12,"bold"),bg="GREEN",fg="white")
#         addbtn.grid(row=0,column=0)
#         #update-button
#         updatebtn=Button(btnframe,text="UPDATE",font=("helvetica",12,"bold"),bg="GREEN",fg="white")
#         updatebtn.grid(row=0,column=1)
#         #delete-button
#         deletebtn=Button(btnframe,text="DELETE",font=("helvetica",12,"bold"),bg="GREEN",fg="white")
#         deletebtn.grid(row=0,column=2)
#         #reset-button
#         resetbtn=Button(btnframe,text="RESET",font=("helvetica",12,"bold"),bg="green",fg="white")
#         resetbtn.grid(row=0,column=3)
#         #exit-button
#         exitbtn=Button(btnframe,text="EXIT",font=("helvetica",12,"bold"),bg="GREEN",fg="white")
#         exitbtn.grid(row=0,column=4)
#         #search-button
#         searchlbl=Label(btnframe,font=("helvetica",17,"bold"),text="SEARCH BY",padx=2,relief=SUNKEN,bg="GREEN",fg="white")
#         searchlbl.grid(row=0,column=5,sticky=NW)

        

if __name__=="__main__":
    root=Tk()
    obj=Pharmacymanagementsystem(root)
    root.mainloop()