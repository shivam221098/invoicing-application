import tkinter as tk
from tkinter import ttk

# root is FIRST window OBJECT here
root = tk.Tk()  
#tk.Label(root, text="Enter Your Company Details", font="Times").grid()
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
    # getting variable values from entryboxes
    company_name = name_var.get()
    company_email = email_var.get()
    company_phone = phone_var.get()
    comapany_address = address_var.get()


next_button = ttk.Button(root, text="Next", command=next_window)
next_button.grid(row=4,column=6)

root.mainloop()
