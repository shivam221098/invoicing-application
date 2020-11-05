import tkinter as tk
from tkinter import ttk

# ** THIS IS INVOICE WINDOW name_lable IS PRODUCT NAME LABEL RESPSCTIVELY ALL OTHERS ** #

# root is FIRST window OBJECT here
root = tk.Tk()  
root.title("Invoice")

# labels
name_label = ttk.Label(root, text="Product Name : ")
name_label.grid(row=0, column=0, sticky=tk.W)

type_lable = ttk.Label(root, text="Category : ")
type_lable.grid(row=0,column=2)

discount_lable = ttk.Label(root, text="Discount % : ")
discount_lable.grid(row=0, column=4)

# entry boxes
name_var = tk.StringVar()
name_entrybox = ttk.Entry(root, width=20, textvariable= name_var)
name_entrybox.grid(row=0,column=1)

discount_var = tk.StringVar()
discount_entrybox = ttk.Entry(root, width=20, textvariable= name_var)
discount_entrybox.grid(row=0,column=5)

# combo Box
type_var = tk.StringVar()
name_combobox = ttk.Combobox(root, width=16, textvariable="type_var", state="readonly")
name_combobox['values'] = ("Food","Clothes","Phones","Electronics","Furniture","Luxury")
name_combobox.current(3)
name_combobox.grid(row=0,column=3)








root.mainloop()