from tkinter import *
import mysql.connector as mc 
import tkinter.messagebox as messagebox
from PIL import Image,ImageTk
import customtkinter as ct


def adopt():
        tr = ct.CTk()
        tr.geometry("500x450") 
        tr.resizable(0,0)


        tr.iconbitmap(r'favicon.ico')
        tr.title("Adoption Details..")

        ct.set_appearance_mode("dark")  
        ct.set_default_color_theme("dark-blue")



        heading = ct.CTkLabel(master=tr,
                               width=120,
                               height=25,
                               fg_color=("Blue", "Blue"),
                               corner_radius=8,
                               text="Adoption Details",
                               text_font=("Sans Serif",45))
        heading.place(x=30,y=10)
        # Creating Labels
        name = ct.CTkLabel(master=tr,
                               width=120,
                               height=25,
                               fg_color=("red", "red"),
                               corner_radius=8,
                               text="Name:",
                               text_font=("Sans Serif",15))
        name.place(x=25, y=90)
        e_name = ct.CTkEntry(master=tr,
                    placeholder_text="name",
                    width=180,
                    height=25,
                    border_width=2,
                    corner_radius=10,
                    text_font=("Sans Serif",15)
                )
        e_name.place(x=170, y=90)


        address = ct.CTkLabel(master=tr,
                               width=120,
                               height=25,
                               fg_color=("red", "red"),
                               corner_radius=8,
                               text="Address:",
                               text_font=("Sans Serif",15))
        address.place(x=25, y=130)
        e_address = ct.CTkEntry(master=tr,
                    placeholder_text="address",
                    width=180,
                    height=25,
                    border_width=2,
                    corner_radius=10,
                    text_font=("Sans Serif",15)
                )
        e_address.place(x=170, y=130)


        Id = ct.CTkLabel(master=tr,
                               width=120,
                               height=25,
                               fg_color=("red", "red"),
                               corner_radius=8,
                               text="Animal ID:",
                               text_font=("Sans Serif",15))
        Id.place(x=25, y=180)
        e_Id = ct.CTkEntry(master=tr,
                    placeholder_text="Adopter ID",
                    width=180,
                    height=25,
                    border_width=2,
                    corner_radius=10,
                    text_font=("Sans Serif",15)
                )
        e_Id.place(x=170, y=180)


        job = ct.CTkLabel(master=tr,
                               width=120,
                               height=25,
                               fg_color=("red", "red"),
                               corner_radius=8,
                               text="JOB:",
                               text_font=("Sans Serif",15))
        job1 = ct.CTkLabel(master=tr,
                               width=120,
                               height=25,
                               fg_color=("red", "red"),
                               corner_radius=8,
                               text="( Company Name /",
                               text_font=("Sans Serif",15))
        job2 = ct.CTkLabel(master=tr,
                               width=120,
                               height=25,
                               fg_color=("red", "red"),
                               corner_radius=8,
                               text="Company Address )",
                               text_font=("Sans Serif",15))
        job.place(x=25, y=240)
        job1.place(x=5,y=270)
        job2.place(x=5,y=293)
        e_job = ct.CTkEntry(master=tr,
                    placeholder_text="Job",
                    width=180,
                    height=25,
                    border_width=2,
                    corner_radius=10,
                    text_font=("Sans Serif",15)
                )
        e_job.place(x=170, y=235)


        phone = ct.CTkLabel(master=tr,
                               width=120,
                               height=25,
                               fg_color=("red", "red"),
                               corner_radius=8,
                               text="Phone No:",
                               text_font=("Sans Serif",15))
        phone.place(x=25, y=330)
        e_phone = ct.CTkEntry(master=tr,
                    placeholder_text="Phone",
                    width=180,
                    height=25,
                    border_width=2,
                    corner_radius=10,
                    text_font=("Sans Serif",15)
                )
        e_phone.place(x=170, y=328)



        def insert(tr):
                name = e_name.get()
                address = e_address.get()
                Id = e_Id.get()
                job = e_job.get()
                phone = e_phone.get()

                Id_lst = []
                con = mc.connect(host="localhost",
                                user="root",
                                password="root@232006",
                                database="project"
                                )
                cursor = con.cursor()
                query = "SELECT * FROM ADOPTION"
                cursor.execute(query)
                rows = cursor.fetchall()

                for row in rows:
                    Id_lst.append(row[2])


                if (name == "" or address == "" or Id == "" or job == "" or phone == ""):
                    messagebox.showinfo("Insert status","Fill all the Details🤦‍♂️🤦‍♂️")
                elif (Id in Id_lst):
                    messagebox.showerror("Insert status","This Id Already Exists.....")
                elif (len(phone)>11):
                    messagebox.showinfo("Insert status","Enter a Valid Phone Number")
                elif (int(Id)<0):
                    messagebox.showerror("Insert status","Id should not be negative😡😡") 
                else:
                    con = mc.connect(host="localhost",
                                user="root",
                                password="root@232006",
                                database="project"
                            )

                    cursor = con.cursor()
                    query = f"INSERT INTO adoption VALUES ('{name}','{address}','{Id}','{job}','{phone}')"
                    cursor.execute(query)
                    cursor.execute("commit")

                    messagebox.showinfo("Insert Status......","Insertion Successfully.....")

                    e_name.delete(0,'end')
                    e_address.delete(0,'end')
                    e_Id.delete(0,'end')
                    e_job.delete(0,'end')
                    e_phone.delete(0,'end')

                    con.close()
                    
                    tr.destroy()

                con.close()




            # Button......
        insert_btn = ct.CTkButton(master=tr,
                    command=lambda:insert(tr),
                    fg_color = ('dodger blue','dodger blue'),
                    text="Insert",
                    bg_color=('dodger blue','dodger blue'),
                    text_font=("Times New Roman",15),
                    width=475
            )
        insert_btn.place(x=15, y=400)


        
        tr.mainloop()



















