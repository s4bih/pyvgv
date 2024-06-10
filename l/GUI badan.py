import tkinter as tk
from tkinter import ttk

window=tk.Tk()
window.title(" ukur berat badan")
window.geometry("10000x10000")









country_var=tk.StringVar()
country_var.set("kg to lb")

result_text = tk.StringVar()

bb_label = ttk.Label(window, text="enter your weight", font=("Arial", 12))
bb_label.grid(column=50, row=1, padx=100, pady=10)
bb_entry = ttk.Entry(window,style="TEntry")
bb_entry.grid(column=2, row=2, padx=10, pady=10)


Style=ttk.Style()
Style.configure("TEntry",font=("Arial",12),bg="white",fg="black")
Style.configure("TCombobox",font=("Arial",12),bg="white",fg="black")

country_combobox=ttk.Combobox(window,textvariable=country_var,values=["kg to pound","pound to kg","kg to ounches","ounches to kg"],style="TCombobox")
country_combobox.grid(column=2,row=6,padx=10,pady=10)

def convert(pound_entry=bb_entry,kg_entry=bb_entry,ounches_entry=bb_entry):
    if country_var.get() == "kg to pound":
        kg = float(kg_entry.get())
        pound = kg * 2.20462
        pound_entry.insert(0, pound)
        result_text.set("kg to pound: " + str(pound))
    elif country_var.get() == "pound to kg":
        pound = float(pound_entry.get())
        kg = pound / 2.20462
        result_text.set("kg to pound: " + str(kg))
    elif country_var.get() == "kg to ounches":
        kg = float(kg_entry.get())
        ounches = kg * 35.27396
        result_text.set("kg to ounches: " + str(ounches))
    elif country_var.get() == "ounches to kg":
        ounches = float(ounches_entry.get())
        kg = ounches / 35.27396
        result_text.set("ounches to kg: " + str(kg))
    else:
        result_text.set("Invalid input")


submit_button = ttk.Button(window, text="Submit",command=convert,style="TButton")
submit_button.grid(column=2,row=7,padx=10,pady=10)

label_result = ttk.Label(window, textvariable=result_text, font=("Arial", 12))
label_result.grid(column=2, row=8, padx=10, pady=10)


window.mainloop()