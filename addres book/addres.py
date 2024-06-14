import tkinter as tk
from tkinter import messagebox

def update_listbox():
    contact_listbox.delete(0, tk.END)
    for contact in contact_list:
        contact_listbox.insert(tk.END, contact["Name"])



def add_contact():
    name=name_entry.get()
    phone=phone_entry.get()
    address=address_entry.get()

    if name and phone and address:
        contact={"Name":name, "phone":phone,"address": address}
        contact_list.append(contact)
        update_listbox()
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Contact added successfully")

    else:
        messagebox.showerror("Error", "Please enter all details")






def view_contacts():
   selected_contact = contact_listbox.curselection()
   if selected_contact:
       contact=contact_list[selected_contact[0]]
       messagebox.showinfo("Contact", f"Name: {contact['Name']}\nPhone: {contact['phone']}\nAddress: {contact['address']}")


def update_contact():
    selected_contact = contact_listbox.curselection()
    if selected_contact:
        contact = contact_list[selected_contact[0]]
        name = name_entry.get()
        phone = phone_entry.get()
        address = address_entry.get()
        if name and phone and address:
            contact["Name"] = name
            contact["phone"] = phone
            contact["address"] = address
            update_listbox()
            messagebox.showinfo("Success", "Contact updated successfully")
        else:
            messagebox.showerror("Error", "Please enter all details")

def delete_contact():
    selected_contact = contact_listbox.curselection()
    if selected_contact:
        contact=contact_list[selected_contact[0]]
        contact_list.remove(contact)
        update_listbox()
        messagebox.showinfo("Success", "Contact deleted successfully")




root=tk.Tk()
root.geometry("300x300")
root.title("Address Book")

contact_list = []
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

phone_label = tk.Label(root, text="Phone:")
phone_label.grid(row=1, column=0)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1)

address_label = tk.Label(root, text="Address:")
address_label.grid(row=2, column=0)
address_entry = tk.Entry(root)
address_entry.grid(row=2, column=1)

add_button=tk.Button(root, text="Add", command=add_contact)
add_button.grid(row=3, column=1)

contact_listbox = tk.Listbox(root)
contact_listbox.grid(row=4, column=0, columnspan=2)

view_button=tk.Button(root, text="View", command=view_contacts)
view_button.grid(row=5, column=0)

update_button=tk.Button(root, text="Update", command=update_contact)
update_button.grid(row=5, column=1)

delete_button=tk.Button(root, text="Delete", command=delete_contact)
delete_button.grid(row=5, column=2)


root.mainloop()
