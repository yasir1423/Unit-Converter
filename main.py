import tkinter as tk
from tkinter import ttk
#Conversion Function
def Convert_length(value,from_unit,to_unit):
    factors={"Centimeter":1,"Meter":100,"Inch":2.54,"Foot":30.48}#1meter=100cm,1 inch=2.54cm,1 foot=30.48cms
    #Convert to cm first, then to target unit.
    return value*factors[from_unit]/factors[to_unit] # 12*1/100 m
def convert_weight(value,from_unit,to_unit):
    factors={"Gram":1,"Kilogram":1000,"Pound":453.592}#1kilogram=1000g,1pound=453.6g
    return value*factors[from_unit]/factors[to_unit]
def convert_temperature(value,from_unit,to_unit):
    if from_unit==to_unit:
        return value
    if from_unit=="Celsius":
        if to_unit=="Fahrenheit":
            return (value*9/5)+32 #C=(F-32)*5/9
        elif to_unit=="Kelvin":
            return value+273.16
    if from_unit=="Fahrenheit":
        if to_unit=="Celsius":
            return (value-32)*5/9
        elif to_unit=="Kelvin":
            return  (value-32)*5/9+273.16
    if from_unit=="Kelvin":
        if to_unit=="Celsius":
            return value-273.16
        elif to_unit=="Fahrenheit":
            return (value-273.16)*9/5+32
#Update Result Automatically
def update_result(*args):
    try:
        value=float(value_entry.get())
        category=category_var.get()
        from_unit=from_var.get()
        to_unit=to_var.get()
        if category=="Length":
            result=Convert_length(value,from_unit,to_unit)
        elif category=="Weight":
            result=convert_weight(value,from_unit,to_unit)
        elif category=="Temperature":
            result=convert_temperature(value,from_unit,to_unit)
        result_var.set(f"{result:.4f}")
    except:
        result_var.set("")
#Update Units Based on category
def update_units(event=None):
    category=category_var.get()
    if category=="Length":
        unit=["Centimeter","Meter","Inch","Foot"]
    elif category=="Weight":
        unit=["Gram","Kilogram","Pound"]
    elif category=="Temperature":
        unit=["Kelvin","Celsius","Fahrenheit"]
    from_menu["values"]=unit
    to_menu["values"]=unit
    from_var.set(unit[0])
    to_var.set(unit[1])
    update_result()
#Tkinter Window
root=tk.Tk()
root.title("Unit Convertor")
root.geometry("600x300")
#Dropdown from category
tk.Label(root,text="Select Category").pack()
category_var=tk.StringVar()
category_menu=ttk.Combobox(root,textvariable=category_var,values=["Length","Weight","Temperature"])
category_menu.pack()
category_menu.current(0)
category_menu.bind("<<ComboboxSelected>>",update_units)
#Dropdown for from unit
tk.Label(root,text="From Unit").pack()
from_var=tk.StringVar()
from_menu=ttk.Combobox(root,textvariable=from_var)
from_menu.pack()
#Dropdoen for to unit
tk.Label(root,text="To Unit").pack()
to_var=tk.StringVar()
to_menu=ttk.Combobox(root,textvariable=to_var)
to_menu.pack()
#Input Feild
tk.Label(root,text="Enter Value:").pack()
value_entry=tk.Entry(root)
value_entry.pack()
#Result Label
tk.Label(root,text="Converted Value:").pack()
result_var=tk.StringVar()
result_label=tk.Label(root,textvariable=result_var,font=("Arial",12,"bold"))
result_label.pack()
#Initial Setup
update_units()
#Auto-Update on typing or selecting units
value_entry.bind("<KeyRelease>",update_result)
from_menu.bind("<<ComboboxSelected>>",update_result)
to_menu.bind("<<ComboboxSelected>>",update_result)
category_menu.bind("<<ComboboxSelected>>",update_units)
root.mainloop()




