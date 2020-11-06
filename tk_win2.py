import tkinter as tk
from tkinter import ttk

# ** THIS IS INVOICE WINDOW name_lable IS PRODUCT NAME LABEL RESPSCTIVELY ALL OTHERS ** #

# root is FIRST window OBJECT here
root = tk.Tk()  
root.title("Invoice")

'''# labels
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
discount_entrybox = ttk.Entry(root, width=20, textvariable= discount_var)
discount_entrybox.grid(row=0,column=5)

# combo Box
type_var = tk.StringVar()
name_combobox = ttk.Combobox(root, width=16, textvariable="type_var", state="readonly")
name_combobox['values'] = ("Food","Clothes","Phones","Electronics","Furniture","Luxury")
name_combobox.current(3)
name_combobox.grid(row=0,column=3)'''

row_count = 0
dict_list = []

def row_creation():
    global row_count
    global
    # labels
    name_label = ttk.Label(root, text="Product Name : ")
    name_label.grid(row=row_count, column=0, sticky=tk.W)

    type_lable = ttk.Label(root, text="Category : ")
    type_lable.grid(row=row_count,column=2)

    discount_lable = ttk.Label(root, text="Discount % : ")
    discount_lable.grid(row=row_count, column=4)

    # entry boxes
    name_var = tk.StringVar()
    name_entrybox = ttk.Entry(root, width=20, textvariable= name_var)
    name_entrybox.grid(row=row_count,column=1)

    discount_var = tk.StringVar()
    discount_entrybox = ttk.Entry(root, width=20, textvariable= discount_var)
    discount_entrybox.grid(row=row_count,column=5)

    # combo Box
    type_var = tk.StringVar()
    name_combobox = ttk.Combobox(root, width=16, textvariable="type_var", state="readonly")
    name_combobox['values'] = ("Food","Clothes","Phones","Electronics","Furniture","Luxury")
    name_combobox.current(3)
    name_combobox.grid(row=row_count,column=3)

    name = name_var.get()
    ye = type_var.get()
    dis = discount_var.get()

    print(name,ye)
    

    dict_list.append({"ProductName":name,"Category":ye,"Discount":dis})

    row_count += 1
    print(dict_list)
    print(name,ye)
   


next_button = ttk.Button(root, text="Next", command=row_creation)
next_button.grid(row=row_count+2,column=6)


row_creation()
root.mainloop()
