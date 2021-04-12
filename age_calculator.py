from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
from datetime import date
from tkinter import messagebox
root = Tk()
root.title("Age Calculator")

pic=ImageTk.PhotoImage(Image.open(r"C:\Users\Luciano\Downloads\calculator.png"))
disp_pic = Label(root, text="", image=pic)
disp_pic.grid(row=0, column=0, padx=30)

name = StringVar()
year = IntVar()
month = IntVar()
day = IntVar()

name.set("")
year.set("")
month.set("")
day.set("")

Label(root, text="Name").grid(row=1, column=0, sticky=W, padx=20, pady=(20,10))
Label(root, text="Year").grid(row=2, column=0, sticky=W, padx=20, pady=10)
Label(root, text="Month").grid(row=3, column=0, sticky=W, padx=20, pady=10)
Label(root, text="Day").grid(row=4, column=0, sticky=W, padx=20, pady=10)

name_entry=Entry(root,width=30,textvariable=name).grid(row=1,column=0,sticky=W,padx=80,pady=(20,10))
year_entry=Entry(root,width=30,textvariable=year).grid(row=2,column=0,sticky=W,padx=80,pady=10)
month_entry=Entry(root,width=30,textvariable=month).grid(row=3,column=0,sticky=W,padx=80,pady=10)
day_entry=Entry(root,width=30,textvariable=day).grid(row=4,column=0,sticky=W,padx=80,pady=10)

def error_check():
    if str(name.get()).isalpha() == False:
        messagebox.showerror("Error", "Only strings are allowed in the name field.")
    if str(year.get()).isnumeric() == False:
        messagebox.showerror("Error", "Only numbers are allowed in year,month or day fields.") 

def calc():
    error_check()
    current_date = date.today()
    given_date = date(int(year.get()), int(month.get()), int(day.get()))
    diff = str(current_date - given_date).split(" ")
    diff = int(diff[0])
    diff_year = diff//365
    diff_month = (diff % 365) // 30
    diff_day = ((diff % 365) // 30) % 30
    messagebox.showinfo("Result", f"{name.get()}, you are {str(diff_year)} years, {str(diff_month)} months and {str(diff_day)} days old.")

calculate_age = Button(root, width=20, text="Calculate Age",command=calc).grid(row=5,column=0,sticky=W,padx=100,pady=10)

root.mainloop()