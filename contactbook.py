import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        self.root.geometry("500x400")
        self.contacts = []

        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Contact Manager", font=("Arial", 20), bg="#f0f0f0")
        self.title_label.pack(pady=20)

        button_names = ["Add Contact", "Contact List", "Search Contact", "Update Contact", "Delete Contact", "Exit"]
        button_commands = [self.add_contact, self.contact_list, self.search_contact, self.update_contact, self.delete_contact, self.root.quit]
        button_bg_colors = ["#4CAF50", "#2196F3", "#FFC107", "#FF9800", "#F44336", "#9E9E9E"]

        self.button_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.button_frame.pack(pady=20)

        for i in range(len(button_names)):
            button = tk.Button(self.button_frame, text=button_names[i], command=button_commands[i], width=15, bg=button_bg_colors[i], fg="white")
            button.grid(row=i, column=0, padx=10, pady=5)

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter the name:")
        phone_num = simpledialog.askstring("Input", "Enter the phone number:")
        email = simpledialog.askstring("Input", "Enter the email:")
        address = simpledialog.askstring("Input", "Enter the address:")
        
        if name and phone_num and email and address:
            new_contact = {"name": name, "phone_num": phone_num, "email": email, "address": address}
            self.contacts.append(new_contact)
            messagebox.showinfo("Success", "Contact added successfully.")
        else:
            messagebox.showerror("Error", "All fields are required.")

    def contact_list(self):
        if self.contacts:
            contacts_str = "\n".join([f"{i+1}. Name: {contact['name']}, Phone: {contact['phone_num']}, Email: {contact['email']}, Address: {contact['address']}" for i, contact in enumerate(self.contacts)])
            messagebox.showinfo("Contact List", contacts_str)
        else:
            messagebox.showinfo("Contact List", "The contact list is empty.")

    def search_contact(self):
        search_name = simpledialog.askstring("Search", "Enter the name to search:")
        found_contacts = [contact for contact in self.contacts if contact['name'].lower() == search_name.lower()]
        
        if found_contacts:
            contacts_str = "\n".join([f"Name: {contact['name']}, Phone: {contact['phone_num']}, Email: {contact['email']}, Address: {contact['address']}" for contact in found_contacts])
            messagebox.showinfo("Search Result", contacts_str)
        else:
            messagebox.showinfo("Search Result", "No contacts found with that name.")

    def update_contact(self):
        update_name = simpledialog.askstring("Update", "Enter the name of the contact to update:")
        
        for contact in self.contacts:
            if contact['name'].lower() == update_name.lower():
                contact['name'] = simpledialog.askstring("Update", "Enter the new name:", initialvalue=contact['name'])
                contact['phone_num'] = simpledialog.askstring("Update", "Enter the new phone number:", initialvalue=contact['phone_num'])
                contact['email'] = simpledialog.askstring("Update", "Enter the new email:", initialvalue=contact['email'])
                contact['address'] = simpledialog.askstring("Update", "Enter the new address:", initialvalue=contact['address'])
                messagebox.showinfo("Success", "Contact updated successfully.")
                return
        else:
            messagebox.showinfo("Error", "No contacts found with that name.")

    def delete_contact(self):
        delete_name = simpledialog.askstring("Delete", "Enter the name of the contact to delete:")
        
        for contact in self.contacts:
            if contact['name'].lower() == delete_name.lower():
                self.contacts.remove(contact)
                messagebox.showinfo("Success", "Contact deleted successfully.")
                return
        else:
            messagebox.showinfo("Error", "No contacts found with that name.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()