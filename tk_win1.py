import os
import json
import tkinter as tk
from tkinter import ttk


# This function is responsible for creating a separate directory for each company
# And in that directory all company related information will be stored
def make_directory(name):
    try:
        os.mkdir(name)
        return "created"
    except FileExistsError:
        return "exists"


# Function is responsible for storing invoices related to a company
def store_info(name, email, phone, address):
    status = make_directory(name)

    # If directory is not present, a new will be created and information is saved
    if status is "created":
        company_info = {"name": name,
                        "email": email,
                        "phone": phone,
                        "address": address}

        with open(f"{name.strip()}/company_information.json", "w", encoding="utf-8") as file:
            file.write(json.dumps(company_info))

    # If directory is present
    elif status is "exists":
        # TODO: There are chances that directory is present but there is no information of company
        #  (empty directory case)
        with open(f"{name.strip()}/company_information.json", "r", encoding="utf-8") as file:
            company_info = json.loads(file.read())
        # print(company_info)
    # TODO: E-mail validation


# root is FIRST window OBJECT here
root = tk.Tk()  
# tk.Label(root, text="Enter Your Company Details", font="Times").grid()
root.title("Company Details")

# labels
name_label = ttk.Label(root, text="Company Name : ")
name_label.grid(row=0, column=0, sticky=tk.W)

email_label = ttk.Label(root, text="Company Em@il : ")
email_label.grid(row=1, column=0, sticky=tk.W)       # sticky = tk.W is sticking lable to the mostleft

phone_label = ttk.Label(root, text="Company Phone No.: ")
phone_label.grid(row=2, column=0)

address_label = ttk.Label(root, text="Company Address : ")
address_label.grid(row=3, column=0, sticky=tk.W)   

# entryboxes
name_var = tk.StringVar()
name_entrybox = ttk.Entry(root, width=20, textvariable= name_var)
name_entrybox.grid(row=0,column=1)
name_entrybox.focus()        # get the cursor to the name field

email_var = tk.StringVar()   # email vaiable
email_entrybox = ttk.Entry(root, width=20, textvariable= email_var)
email_entrybox.grid(row=1,column=1)

phone_var = tk.StringVar()   # phone variable
phone_entrybox = ttk.Entry(root, width=20, textvariable= phone_var)
phone_entrybox.grid(row=2,column=1)

address_var = tk.StringVar() # address variable
address_entrybox = ttk.Entry(root, width=20, textvariable= address_var)
address_entrybox.grid(row=3,column=1)


# next-> window button
def next_window():
    # getting variable values from entry boxes
    company_name = name_var.get()
    company_email = email_var.get()
    company_phone = phone_var.get()
    company_address = address_var.get()

    store_info(company_name, company_email, company_phone, company_address)  # Stores the information


next_button = ttk.Button(root, text="Next", command=next_window)
next_button.grid(row=4,column=6)

root.mainloop()
