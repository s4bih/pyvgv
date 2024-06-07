import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def submit_form():
    name  = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    country=country_var.get()
    gender = gender_combobox.get()
    if name == "" or email == "" or  password == "" :
        messagebox.showerror("Error", "Please fill in all fields")
    else:
        messagebox.showinfo("Success", "Form submitted successfully")

window=tk.Tk()
window.title("Form")
window.geometry("400x400")



Style=ttk.Style()
Style.theme_use("clam")

Style.configure("TLabel",font=("Arial", 12),bg="gray")

Style.configure("TEntry",font=("Arial",12),bg="white",fg="black")

Style.configure("TButton",font=("Arial",12),bg="white",fg="black")

Style.configure("TCombobox",font=("Arial",12),bg="white",fg="black")

name_label=ttk.Label(window,text="Name",style="TLabel")
name_label.grid(column=0,row=0,padx=10,pady=10)

name_entry=ttk.Entry(window,style="TEntry")
name_entry.grid(column=1,row=0,padx=10,pady=10)


email_label=ttk.Label(window,text="email",style="TLabel")
email_label.grid(column=0,row=1,padx=10,pady=10)
email_entry=ttk.Entry(window,style="TEntry")
email_entry.grid(column=1,row=1,padx=10,pady=10)

gender_label=ttk.Label(window,text="Gender",style="TLabel")
gender_label.grid(column=0,row=2,padx=10,pady=10)

gender_variable=tk.StringVar()
gender_variable.set("Male")

male_radiobton=ttk.Radiobutton(window,text="Male",variable=gender_variable,value="Male",style="TRadiobutton")
male_radiobton.grid(column=0,row=3,padx=10,pady=10)

female_radiobton=ttk.Radiobutton(window,text="Female",variable=gender_variable,value="Female",style="TRadiobutton")
female_radiobton.grid(column=1,row=3,padx=10,pady=10)

password_label=ttk.Label(window,text="Password",style="TLabel")
password_label.grid(column=0,row=4,padx=10,pady=10)
password_entry=ttk.Entry(window,show="*",style="TEntry")
password_entry.grid(column=1,row=4,padx=10,pady=10)

submit_button=ttk.Button(window,text="Submit",command=submit_form,style="TButton")
submit_button.grid(column=1,row=6,padx=10,pady=10)

country_var=tk.StringVar()
country_var.set("Indonesia")

country_combobox=ttk.Combobox(window,textvariable=country_var,values=["India","USA","UK"],style="TCombobox")
country_combobox.grid(column=1,row=5,padx=10,pady=10)

submit_button_style=ttk.Style()
submit_button_style.map(
    style="TButton",
    foreground=[("pressed","red"),("active","blue")],
    background=[("pressed","black"),("active","white")]

)




gender_combobox=ttk.Combobox(window,values=["Male","Female","Other"],style="TCombobox")


window.mainloop()