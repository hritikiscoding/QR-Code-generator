
from tkinter import *
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage
class QR_code:
    def __init__(self,root):
        self.root=root
        self.root.title("QR Code Generator || Developed By Hritik")
        self.root.geometry("1000x600+200+100")
        self.root.resizable(False,False)
        title=Label(root,text="QR Code Generator",font=("times new roman",50),bg='black',fg='white').place(x=0,y=0,relwidth=1)
        
        # student details
        self.std_id=StringVar()
        self.std_name=StringVar()
        self.std_department=StringVar()
        self.std_batch=StringVar()

        std_frame=Frame(root,bd=2,bg='white',relief=RIDGE)
        std_frame.place(x=50,y=100,width=550,height=480)
        std_title=Label(std_frame,text="Student Details",font=('Arial Black',25),bg='grey',fg='white').place(x=0,y=0,relwidth=1)
        
        lbl_id=Label(std_frame,text="Student Id",font=('Arial Black',15),bg='white').place(x=20,y=60)
        lbl_name=Label(std_frame,text="Student Name",font=('Arial Black',15),bg='white').place(x=20,y=120)
        lbl_department=Label(std_frame,text="Department",font=('Arial Black',15),bg='white').place(x=20,y=180)
        llb_batch=Label(std_frame,text="Batch",font=('Arial Black',15),bg='white').place(x=20,y=240)

        
        
        lbl_id=Entry(std_frame,font=('Arial Black',15,),bg='lightyellow',textvariable=self.std_id).place(x=220,y=60)
        lbl_name=Entry(std_frame,font=('Arial Black',15),bg='lightyellow',textvariable=self.std_name).place(x=220,y=120)
        lbl_department=Entry(std_frame,font=('Arial Black',15),bg='lightyellow',textvariable=self.std_department).place(x=220,y=180)
        llb_batch=Entry(std_frame,font=('Arial Black',15),bg='lightyellow',textvariable=self.std_batch).place(x=220,y=240)

       
       
       
        btn_gen=Button(std_frame,text="Generate QR",font=("times new roman",15,'bold'),bg='black',fg='white',command=self.generate).place(x=70,y=320,width=200)
        btn_gen=Button(std_frame,text="Clear",font=("times new roman",15,'bold'),bg='grey',fg='white',command=self.clear).place(x=320,y=320,width=150)

        self.msg=''
        self.lbl_msg=Label(std_frame,text=self.msg,font=("times new roman",25),fg='green',bg='white')
        self.lbl_msg.place(x=50,y=400,width=400)

        #studen qr 

        qr_frame=Frame(root,bd=2,bg='white',relief=RIDGE)
        qr_frame.place(x=650,y=100,width=260,height=480)
        qr_title=Label(qr_frame,text=" StudentQR Code",font=('Arial Black',15),bg='grey',fg='white').place(x=0,y=0,relwidth=1)

        
        self.qr_code=Label(qr_frame,text="Qr Not \nAvailable",font=("times new roman ",20),bg='white',fg='black',bd=1,relief=RIDGE)
        self.qr_code.place(x=27,y=100,width=200,height=200)

    def generate(self):
        if(self.std_id.get()=='' or self.std_name.get()=='' or self.std_department.get()=='' or self.std_batch.get()==''):
            self.msg='All fields are required!!'
            self.lbl_msg.config(text=self.msg,fg='red')
        else:
             qr_data=(f"Student Id:{self.std_id.get()}\nStudent Name:{self.std_name.get()}\nDepartment:{self.std_department.get()}\nBatch:{self.std_batch.get()}")
             qr_code=qrcode.make(qr_data)
             qr_code=resizeimage.resize_cover(qr_code,[180,180])
             qr_code.save("QRcode generator/student qr/student_"+str(self.std_id.get())+'.png')
             self.im=ImageTk.PhotoImage(file="QRcode generator/student qr/student_"+str(self.std_id.get())+'.png')
             self.qr_code.config(image=self.im)

             
             #updating alert
             self.msg='QR generated successfully'
             self.lbl_msg.config(text=self.msg,fg='green')
    def clear(self):
        self.std_id.set('')
        self.std_name.set('')
        self.std_department.set('')
        self.std_batch.set('')

        

root=Tk()
obj=QR_code(root)
root.mainloop()