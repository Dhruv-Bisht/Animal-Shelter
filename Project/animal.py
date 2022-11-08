from tkinter import *
import mysql.connector as mc 
import tkinter.messagebox as messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import customtkinter as ct
from Record import adoption_record
from Adoption import adoption



def insert():
    breed = e_breed.get()
    pf = e_pf.get()
    Id = e_Id.get()
    founder= e_founder.get()



    Id_lst = []
    con = mc.connect(host="localhost",
                    user="root",
                    password="root@232006",
                    database="project"
                )
    cursor = con.cursor()
    query = "SELECT * FROM ANIMAL"
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        Id_lst.append(row[2])


    if (breed == "" or pf == "" or Id == "" or founder == ""):
        messagebox.showinfo("Insert Status......","All Fields Should be Filled before Inserting🤦‍♂️🤦‍♂️")
    
    elif (Id in Id_lst):
        messagebox.showerror("Insert Status.....","There Should Be Unique Id😡😡\n(This ID Already Exist)")
    
    elif (int(Id) < 0):
        messagebox.showerror("Insert Status....","Id should not be negative...😡😡")

    else:
        con = mc.connect(host="localhost",
                    user="root",
                    password="root@232006",
                    database="project"
                )

        cursor = con.cursor()
        query = "INSERT INTO animal VALUES ('{}','{}','{}','{}')".format(breed, pf, Id, founder)
        cursor.execute(query)
        cursor.execute("commit")
        messagebox.showinfo("Insert Status......","Insertion Successfully👍👍")

        e_breed.delete(0,'end')
        e_pf.delete(0,'end')
        e_Id.delete(0,'end')
        e_founder.delete(0,'end')

        con.close()





def show():
    breed = e_breed.get()
    pf = e_pf.get()
    Id = e_Id.get()
    founder= e_founder.get()

    Id_lst = []
    con = mc.connect(host="localhost",
                    user="root",
                    password="root@232006",
                    database="project"
                )
    cursor = con.cursor()
    query = "SELECT * FROM ANIMAL"
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        Id_lst.append(row[2])

    if (Id == ""):
        messagebox.showinfo("Fectching Status......","ID is required to fetch details🤦‍♂️🤦‍♂️")
    
    elif (Id not in Id_lst):
        messagebox.showerror("Fetching Status.....","Enter a Valid ID😡😡")

    else:

        tr = ct.CTk()
        tr.geometry("1400x300") 
        tr.resizable(0,0)

        # ct.set_appearance_mode("dark") 
        # ct.set_default_color_theme("dark-blue") 


        con = mc.connect(host="localhost",
                    user="root",
                    password="root@232006",
                    database="project"
                )

        # Creating Labels
        tbreed = ct.CTkLabel(master=tr,
                               width=120,
                               height=25,
                               fg_color=("red", "red"),
                               corner_radius=8,
                               text="Breed:",
                               text_font=("Sans Serif",25))
        tbreed.place(x=10, y=20)
        
        tpf =ct.CTkLabel(master=tr,
                               width=120,
                               height=25,
                               fg_color=("red", "red"),
                               corner_radius=8,
                               text="Place Found At:",
                               text_font=("Sans Serif",25))
        tpf.place(x=10, y=90)

        tId = ct.CTkLabel(master=tr,
                               width=120,
                               height=25,
                               fg_color=("red", "red"),
                               corner_radius=8,
                               text="Animal ID:",
                               text_font=("Sans Serif",25))
        tId.place(x=10, y=160)

        tfounder = ct.CTkLabel(master=tr,
                               width=120,
                               height=25,
                               fg_color=("red", "red"),
                               corner_radius=8,
                               text="Rescued By:",
                               text_font=("Sans Serif",25))
        tfounder.place(x=10, y=230)

        cursor = con.cursor()
        if Id != "":
            query = "SELECT * FROM ANIMAL WHERE ID = {}".format(Id)
        # query = "SELECT * FROM ANIMAL"
        cursor.execute(query)
        rows = cursor.fetchall()

        for row in rows:
            tbreed.config(text = "Breed: {}".format(row[0]))
            tpf.config(text= "Place of Found: {}".format(row[1]))
            tId.config(text = "ID: {}".format(row[2]))
            tfounder.config(text = "Rescued By: {}".format(row[3]))

        con.close()

        tr.mainloop()




def update():
    breed = e_breed.get()
    pf = e_pf.get()
    Id = e_Id.get()
    founder= e_founder.get()

    Id_lst = []
    con = mc.connect(host="localhost",
                    user="root",
                    password="root@232006",
                    database="project"
                )
    cursor = con.cursor()
    query = "SELECT * FROM ANIMAL"
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        Id_lst.append(row[2])

    def update1(root):
            breed = te_breed.get()
            pf = te_pf.get()
            Id = te_Id.get()
            founder= te_founder.get()        
            con = mc.connect(host="localhost",
                        user="root",
                        password="root@232006",
                        database="project"
                    )
            cursor = con.cursor()
            query = cursor.execute("UPDATE animal set breed='"+ breed +"', place_found='"+ pf +"',founder='"+ founder +"' where id='"+ Id +"'")
            cursor.execute(query)
            cursor.execute("commit")
            messagebox.showinfo("Update Status......","Update Successfully👍👍")

            te_breed.delete(0,'end')
            te_pf.delete(0,'end')
            te_Id.delete(0,'end')
            te_founder.delete(0,'end')
            root.destroy()

    if (Id == ""):
        messagebox.showinfo("Update Status......","Id Should be Filled😡😡")

    elif (Id not in Id_lst):
        messagebox.showerror("Update Status.....","Enter a Valid ID😡😡")
    else:
        e_Id.delete(0,END)
        root = ct.CTk()
        root.geometry("500x400")
        l = Label(root,
                width=20,
                font=("Times New Roman",25),
                foreground="white",
                background="blue",
                text="Update Record"
            )
        l.place(x=80,y=10)

        tbreed = Label(root,
                            width=7,
                            font=("Sans Serif",15),
                            foreground="white",
                            background="#FF0000",
                            text="Breed:"
                        )
        tbreed.place(x=23, y=100)
        te_breed = Entry(root,
                            width=20,
                            font=("Sans Serif",15),
                            background="#3D3D3D",
                            border=0
                        )
        te_breed.place(x=300,y=100)
        tpf =  Label(root,
                            width=15,
                            font=("Sans Serif",15),
                            foreground="white",
                            background="#FF0000",
                            text="Place Found at:"
                        )
        tpf.place(x=23, y=180)
        te_pf =  Entry(root,
                            width=20,
                            font=("Sans Serif",15),
                            background="#3D3D3D",
                            border=0
                        )
        te_pf.place(x=300,y=180)

        tId = Label(root,
                            width=10,
                            font=("Sans Serif",15),
                            foreground="white",
                            background="#FF0000",
                            text="Animal ID:"
                        )
        tId.place(x=23, y=260)
        te_Id =  Entry(root,
                            width=20,
                            font=("Sans Serif",15),
                            background="#3D3D3D",
                            border=0
                        )
        te_Id.place(x=300,y=260)

        tfounder = Label(root,
                            width=15,
                            font=("Sans Serif",15),
                            foreground="white",
                            background="#FF0000",
                            text="Rescued By:"
                        )
        tfounder.place(x=23, y=340)
        te_founder =  Entry(root,
                            width=20,
                            font=("Sans Serif",15),
                            background="#3D3D3D",
                            border=0
                        )
        te_founder.place(x=300,y=340)


        con = mc.connect(host="localhost",
                    user="root",
                    password="root@232006",
                    database="project"
                )

        query = "SELECT * FROM ANIMAL WHERE ID = {}".format(Id)
        cursor = con.cursor()
        # query = "SELECT * FROM ANIMAL"
        cursor.execute(query)
        rows = cursor.fetchall()

        for row in rows:
            te_breed.insert(0,(row[0]))
            te_pf.insert(0,(row[1]))
            te_Id.insert(0,(row[2]))
            te_founder.insert(0,(row[3]))


        btn = Button(root, text="Update", command=lambda:update1(root),width=40, background="#1E90FF",foreground="white",font=('Times New Roman',15), border=0)
        btn.place(x=23,y=400)

        con.close()
        root.mainloop()




def suggestion():
    # global textbox1
    # suggest = textbox1.cget()
    suggest = textbox1.get("1.0",END)
    con = mc.connect(host="localhost",
                    user="root",
                    password="root@232006",
                    database="project"
                )
    cursor = con.cursor()
    # query = "SELECT * FROM ANIMAL WHERE ID = {}".format(Id)
    query = "INSERT INTO SUGGESTION values ('{}')".format(suggest)
    cursor.execute(query)
    cursor.execute("commit")

    messagebox.showinfo("Suggestion Status","Your Suggestion Has been Send....👍👍")
    textbox1.destroy()

    # con.close()





def show_animal(): 
            root = Tk()
            # root.geometry("400x250")
            root.resizable(0,0)
            root.geometry("380x190")
            style = ttk.Style()

            root.title("Animal Record.....")
            root.iconbitmap('dog(1).ico')


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
            # style.map("Treeview",
            #         background=[('selected','blue')]
                    #  ) 


            treev = ttk.Treeview(root, selectmode ='browse')
            treev.pack(side ='right')
            verscrlbar = ttk.Scrollbar(root,
                                    orient ="vertical",
                                    command = treev.yview)
            verscrlbar.pack(side ='right', fill ='x')
            
            treev.configure(xscrollcommand = verscrlbar.set)
            
            treev.configure(xscrollcommand = verscrlbar.set)
            
            treev["columns"] = ("1", "2", "3","4")
            
            treev['show'] = 'headings'
            
            treev.column("1", width = 90, anchor ='c')
            treev.column("2", width = 90, anchor ='c')
            treev.column("3", width = 90, anchor ='c')
            treev.column("4", width = 90, anchor ='c') 



            treev.heading("1", text ="Breed")
            treev.heading("2", text ="Place Found at")
            treev.heading("3", text ="Animal Id")
            treev.heading("4", text="Rescued By") 





            con = mc.connect(host="localhost",
                            user="root",
                            password="root@232006",
                            database="project"
            )

            cursor = con.cursor()
            query = "SELECT * FROM ANIMAL order by ID ASC"
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.execute("commit")

            treev.tag_configure('oddrow',background='white')
            treev.tag_configure('evenrow',background='lightblue')

            count = 0
            for row in rows:
                if count % 2 == 0:
                        treev.insert("", "end", text="",values =(row[0],row[1],row[2],row[3]),tags=('evenrow'))
                else:
                        treev.insert("", "end", text="",values =(row[0],row[1],row[2],row[3]),tags=('oddrow'))
                count += 1
            #     dict1 = {row[2]:(row[0],row[1],row[2],row[3])}

            # for z in sorted(dict1.keys()):
            #     # print(z)    
            #     pass
            
           
            con.close()
            root.mainloop()
            # k = 1
 




root = ct.CTk()
root.geometry("640x500")
root.resizable(0,0)
root.title("KV Animal Shelter......")
root.iconbitmap('favicon.ico')





#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# color = rgb((52,54,56))

suggestion_lab = ct.CTkLabel(master=root,
                               width=120,
                               height=25,
                               fg_color=("Green", "green"),
                               corner_radius=8,
                               text="Suggestion / FeedBack",
                               text_font=("Times New Roman",15)
                    )
suggestion_lab.place(x=420,y=90)
textbox1 = Text(root,height=11,width=18,background="#343638",font=("Sans serif",15), border=0)
textbox1.place(x=520, y=160)


heading = ct.CTkLabel(master=root,
                               width=120,
                               height=25,
                               fg_color=("Green", "blue"),
                               corner_radius=8,
                               text="KV Animal Shelter",
                               text_font=("Times New Roman",49)
                    )
heading.place(x=60, y=0)


ct.set_appearance_mode("dark")  # Modes: system (default), light, dark
ct.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

# root.wm_attributes('-transparentcolor','red')

animal_details = ct.CTkLabel(master=root,
                               width=120,
                               height=25,
                               fg_color=("red", "red"),
                               corner_radius=8,
                               text="Animal Details",
                               text_font=("Sans Serif",25))
animal_details.place(x=90,y=90)
# Creating Labels
breed = ct.CTkLabel(master=root,
                               width=120,
                               height=25,
                               fg_color=("red", "red"),
                               corner_radius=8,
                               text="Breed:",
                               text_font=("Sans Serif",15))
breed.place(x=23, y=170)
e_breed = ct.CTkEntry(master=root,
                    placeholder_text="Breed",
                    width=180,
                    height=25,
                    border_width=2,
                    corner_radius=10,
                    text_font=("Sans Serif",15)
                )
e_breed.place(x=200,y=168)

pf = ct.CTkLabel(master=root,
                               width=120,
                               height=25,
                               fg_color=("red", "red"),
                               corner_radius=8,
                               text="place Found:",
                               text_font=("Sans Serif",15))
pf.place(x=23, y=220)
e_pf = ct.CTkEntry(master=root,
                    placeholder_text="Place Found at",
                    width=180,
                    height=25,
                    border_width=2,
                    corner_radius=10,
                    text_font=("Sans Serif",15)
                )
e_pf.place(x=200,y=222)

Id = ct.CTkLabel(master=root,
                               width=120,
                               height=25,
                               fg_color=("red", "red"),
                               corner_radius=8,
                               text="Animal ID:",
                               text_font=("Sans Serif",15))
Id.place(x=23, y=270)
e_Id = ct.CTkEntry(master=root,
                    placeholder_text="ID",
                    width=180,
                    height=25,
                    border_width=2,
                    corner_radius=10,
                    text_font=("Sans Serif",15)
                )
e_Id.place(x=200,y=272)

founder = ct.CTkLabel(master=root,
                               width=120,
                               height=25,
                               fg_color=("red", "red"),
                               corner_radius=8,
                               text="Rescued By:",
                               text_font=("Sans Serif",15))
founder.place(x=23, y=320)
e_founder = ct.CTkEntry(master=root,
                    placeholder_text="Rescued by",
                    width=180,
                    height=25,
                    border_width=2,
                    corner_radius=10,
                    text_font=("Sans Serif",15)
                )
e_founder.place(x=200,y=323)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# Button......
insert_btn = ct.CTkButton(master=root,
                    command=insert,
                    fg_color = ('dodger blue','dodger blue'),
                    text="Insert",
                    bg_color=('dodger blue','dodger blue'),
                    text_font=("Times New Roman",15)
            )
insert_btn.place(x=20, y=400)

show_btn= ct.CTkButton(master=root,
                    command=show,
                    fg_color = ('dodger blue','dodger blue'),
                    text = "Show",
                    bg_color=('dodger blue','dodger blue'),
                    text_font=("Times New Roman",15)
            )
show_btn.place(x=175, y=400)

adoption_btn = ct.CTkButton(master=root,
                    command=adoption.adopt,
                    fg_color = ('dodger blue','dodger blue'),
                    text="Adoption",
                    bg_color=('dodger blue','dodger blue'),
                    text_font=("Times New Roman",15)
            )
adoption_btn.place(x=330, y=400)

update_btn = ct.CTkButton(master=root,
                    command=update,
                    fg_color = ('dodger blue','dodger blue'),
                    text="Update",
                    bg_color=('dodger blue','dodger blue'),
                    text_font=("Times New Roman",15)
            )
update_btn.place(x=490, y=400)

adoptionRecord_btn = ct.CTkButton(master=root,
                    command=adoption_record.data,
                    fg_color = ('dodger blue','dodger blue'),
                    text="Adoption Record",
                    bg_color=('dodger blue','dodger blue'),
                    text_font=("Times New Roman",15)
            )
adoptionRecord_btn.place(x=20, y=440)

suggestion_btn = ct.CTkButton(master=root,
                    command=suggestion,
                    fg_color = ('dodger blue','dodger blue'),
                    text="Suggestion",
                    bg_color=('dodger blue','dodger blue'),
                    text_font=("Times New Roman",15)
            )
suggestion_btn.place(x=195, y=440)

animal_record_btn = ct.CTkButton(master=root,
                    command=show_animal,
                    fg_color = ('dodger blue','dodger blue'),
                    text="Animal Record",
                    bg_color=('dodger blue','dodger blue'),
                    text_font=("Times New Roman",15)
            )
animal_record_btn.place(x=350, y=440)



#---------------------------------------------------------------------------------------------------------#


root.mainloop()































