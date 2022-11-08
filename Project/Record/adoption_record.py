from tkinter import *
import mysql.connector as mc 
import tkinter.messagebox as messagebox
from tkinter import ttk
import customtkinter as ct


def data():

        root = Tk()
        root.geometry("470x190")

        root.title("Adoption Record")
        root.iconbitmap('cool(2).ico')

        style = ttk.Style()
        root.config(background="black")
        style.theme_use('default')
        style.configure("Treeview",
                        foreground = "black",
                        background = "white",
                        relief="flat",
                        rowheight=25,
                        fieldbackground="white",
                        font=('Sans serif',12)
                    )   
        style.configure("Treeview.Heading",
                    background="red",
                    foreground="white",
                    font=("Times New Roman",20),
                    padx = 20,
                    margin=20,
                    relief="flat",
                    )   

        root.resizable(0,0)
        treev = ttk.Treeview(root, selectmode ='browse')
        treev.pack(side ='right')
        verscrlbar = ttk.Scrollbar(root,
                                orient ="vertical",
                                command = treev.yview)
        verscrlbar.pack(side ='right', fill ='x')
        
        treev.configure(xscrollcommand = verscrlbar.set)
        
        treev["columns"] = ("1", "2", "3","4","5")
        
        treev['show'] = 'headings'
        
        treev.column("1", width = 90, anchor ='c')
        treev.column("2", width = 90, anchor ='se')
        treev.column("3", width = 90, anchor ='se')
        treev.column("4", width = 90, anchor ='se') 
        treev.column("5", width = 90, anchor ='se') 



        treev.heading("1", text ="Name")
        treev.heading("2", text ="Address")
        treev.heading("3", text ="Adopter Id")
        treev.heading("4", text="Job") 
        treev.heading("5", text="Phone")





        con = mc.connect(host="localhost",
                        user="root",
                        password="root@232006",
                        database="project"
        )

        cursor = con.cursor()
        query = "SELECT * FROM ADOPTION order by id"
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.execute("commit")

        treev.tag_configure('oddrow',background='white')
        treev.tag_configure('evenrow',background='lightblue')

        count = 0
        for row in rows:
            if count%2 == 0:
                treev.insert("", "end", text="",values =(row[0],row[1],row[2],row[3],row[4]),tags=('evenrow'))
            else:
                treev.insert("", "end", text="",values =(row[0],row[1],row[2],row[3],row[4]),tags=('oddrow'))                
            count += 1
        
        con.close()
        
        root.mainloop()


    

