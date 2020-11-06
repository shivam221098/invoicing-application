import tkinter as tk
from tkinter import ttk

# ** THIS IS INVOICE WINDOW name_lable IS PRODUCT NAME LABEL RESPSCTIVELY ALL OTHERS ** #
# root is FIRST window OBJECT here
root = tk.Tk()  
root.title("Invoice")

row_count = 0
dict_list = []
name_var = discount_var = type_var = ""


# The products which are added, this function will display all products
def product_detail():
    products = f"{len(dict_list)} products added:\n"
    for i in range(len(dict_list)):
        products += f"{i + 1}. " + dict_list[i].get("product") + "\n"
    return products


def execute_next_button():
    global row_count
    # TODO: @type_var is not working
    dict_list.append({"product": name_var.get(), "discount": discount_var.get(), "type": type_var.get()})
    product_detail_label = tk.Label(root, text=product_detail())
    product_detail_label.grid(row=0, column=7)
    row_creation()  # Further call for labels and entry boxes after clicking on next button
    # TODO: if any other button is clicked instead of "Next".


def row_creation():
    global row_count, name_var, discount_var, type_var
    # labels
    name_label = ttk.Label(root, text="Product Name : ")
    name_label.grid(row=row_count, column=0, sticky=tk.W)

    type_lable = ttk.Label(root, text="Category : ")
    type_lable.grid(row=row_count, column=2)

    discount_lable = ttk.Label(root, text="Discount % : ")
    discount_lable.grid(row=row_count, column=4)

    # entry boxes
    name_var = tk.StringVar()
    name_entrybox = ttk.Entry(root, width=20, textvariable= name_var)
    name_entrybox.grid(row=row_count, column=1)

    discount_var = tk.StringVar()
    discount_entrybox = ttk.Entry(root, width=20, textvariable= discount_var)
    discount_entrybox.grid(row=row_count, column=5)

    # combo Box
    type_var = tk.StringVar()
    name_combobox = ttk.Combobox(root, width=16, textvariable="type_var", state="readonly")
    name_combobox['values'] = ("Food", "Clothes", "Phones", "Electronics", "Furniture", "Luxury")
    name_combobox.current(3)
    name_combobox.grid(row=row_count, column=3)

    next_button = ttk.Button(root, text="Next", command=execute_next_button)
    next_button.grid(row=2, column=6)


row_creation()  # Initial call for all labels and entry boxes
root.mainloop()
