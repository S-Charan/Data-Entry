import tkinter
from tkinter import ttk
from tkinter import messagebox

def enter_data():
    accepted = terms_var.get()

    if accepted == "Accepted":
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()

        if first_name and last_name:
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()

            # cources INFO
            register_status = register_var.get()
            cources = numcource_spinbox.get()
            semisters = semister_spinbox.get()

            print("First Name : ", first_name, )
            print("Last Name : ", last_name, )
            print("Title : ", title)
            print("Age : ", age)
            print("Nationality : ", nationality)
            print("Number of Coureces : ", cources)
            print("Number of Semisters", semisters)
            print("Registration Status : ", register_status)

        else:
            tkinter.messagebox.showwarning(title="Error",message="FirstName and LastName Required ")


    else:
        tkinter.messagebox.showwarning(title="Error",message="Accept the Terms and Conditions ")



window =tkinter.Tk()
window.title("data entry ")

frame = tkinter.Frame(window)
frame.pack()

#saving user info
user_info_frame = tkinter.LabelFrame(frame, text="User Information ")
user_info_frame.grid(row=0,column=0,padx=20,pady=10)

first_name_label = tkinter.Label(user_info_frame, text="First Name ")
first_name_label.grid(row=0,column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name ")
last_name_label.grid(row=0,column=1)

first_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1,column=0)
last_name_entry = tkinter.Entry(user_info_frame)
last_name_entry.grid(row=1,column=1)

title_label = tkinter.Label(user_info_frame,text="Title")
title_label.grid(row=0,column=3)
title_combobox = ttk.Combobox(user_info_frame, values=["","Mr","Ms","Dr."])
title_combobox.grid(row=1,column=3)

age_label = tkinter.Label(user_info_frame,text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame,from_=18,to=100)
age_label.grid(row=2,column=0)
age_spinbox.grid(row=3,column=0)

nationality_label = tkinter.Label(user_info_frame,text="Nationality")
nationality_combobox = ttk.Combobox(user_info_frame,values=["Africa", "Antarcatica","Asia","Europe","North America","South America","Oceania"])
nationality_label.grid(row=2,column=1)
nationality_combobox.grid(row=3,column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)

#saving cource info
cource_frame = tkinter.LabelFrame(frame,text="Cources")
cource_frame.grid(row=1,column=0,sticky='news',padx=20,pady=10)

register_label = tkinter.Label(cource_frame,text="Registration Status")
register_var = tkinter.StringVar(value="Not Registered ")
register_check = tkinter.Checkbutton(cource_frame,text="Curently Registered", variable=register_var,onvalue="Registered",offvalue="Not Registered")
register_label.grid(row=0,column=0)
register_check.grid(row=1,column=0)

numcourceslabel = tkinter.Label(cource_frame,text="Cources completed ")
numcource_spinbox = tkinter.Spinbox(cource_frame, from_=0, to='infinity')
numcourceslabel.grid(row=0,column=1)
numcource_spinbox.grid(row=1,column=1)

semister_label = tkinter.Label(cource_frame,text = "Semister ")
semister_spinbox = tkinter.Spinbox(cource_frame, from_=0,to='infinity')
semister_label.grid(row=0,column=2)
semister_spinbox.grid(row=1,column=2)

for widget in cource_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)


#conditions
terms_frame = tkinter.LabelFrame(frame,text="Terms and Conditions ")
terms_frame.grid(row=2,column=0,sticky="news",padx=20,pady=10)

terms_var = tkinter.StringVar(value="Not Accepted ")
terms_check = tkinter.Checkbutton(terms_frame,text = "I accept the Terms and Conditions",variable=terms_var,onvalue="Accepted",offvalue="Not Accepted")
terms_check.grid(row=0,column=0)

#enter button
enter_button = tkinter.Button(frame,text = "Enter",command= enter_data)
enter_button.grid(row=3,column=0,sticky="news",padx=20,pady=10)


window.mainloop()