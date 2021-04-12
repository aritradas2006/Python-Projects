from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

root = Tk()
root.title("Currency Converter")
root.geometry("726x263")
root.minsize(726, 263)

Label(root, text="Currency Converter", font=("Segoe UI", 20, "bold","underline")).grid(row=0, column=1, sticky='W', columnspan=3)
Label(root, text="Currency to be converted: ", font=("Segoe UI", 15,"underline")).grid(row=1, column=0, sticky='W', pady=25, padx=10)
Label(root, text="Result: ", font=("Segoe UI", 15, "underline")).grid(row=2, column=0, sticky='W', pady=10, padx=10)

cur = IntVar()
res = IntVar()
cur.set("")
res.set(0)

etr = Entry(root, width=10, textvariable=cur)
etr.grid(row=1, column=1, sticky='W', padx=10)
etr.focus()

res_label=Label(root,text=res.get())
res_label.grid(row=2,column=1,sticky='W', padx=10)

cur_val = StringVar()
res_val = StringVar()
cur_val.set("INR - Indian Rupee")
res_val.set("USD - United States Dollar")

cur_values = ("INR - Indian Rupee", "USD - United States Dollar", "EUR - Euro", "JPY - Japanese Yen", "GBP - Pound Sterling","AUD - Australian Dollar", "CAD - Canadian Dollar", "CHF - Swiss Franc", "CNY - Chinese Yuan Renminbi", "NZD - New Zealand Dollar")
cur1_values = ("INR", "USD", "EUR", "JPY", "GBP","AUD", "CAD", "CHF", "CNY", "NZD")

cur_1 = Combobox(root, values=cur_values, textvariable=cur_val,state='readonly', width=30).grid(row=1, column=1, sticky='W', padx=100)
cur_2 = Combobox(root, values=cur_values, textvariable=res_val,state='readonly', width=30).grid(row=2, column=1, sticky='W', padx=100)

cur_dict = {
    "INR": [0, 0.014, 0.011, 1.46, 0.0098, 0.018, 0.017, 0.013, 0.088, 0.019],
    "USD": [73.36, 0, 0.83, 106.88, 0.72, 1.29, 1.27, 0.92, 6.47, 1.38],
    "EUR": [88.12, 1.20, 0, 128.40, 0.87, 1.55, 1.52, 1.10, 7.76, 1.66],
    "JPY": [0.69, 0.0094, 0.0078, 0, 0.0067, 0.012, 0.012, 0.0086, 0.061, 0.013],
    "GBP": [101.76, 1.39, 1.16, 148.25, 0, 1.79, 1.76, 1.27, 8.97, 1.92],
    "AUD": [56.91, 0.78, 0.65, 82.91, 0.56, 0, 0.98, 0.71, 5.02, 1.07],
    "CAD": [57.91, 0.79, 0.66, 84.36, 0.57, 1.02, 0, 0.72, 5.11, 1.09],
    "CHF": [79.90, 1.09, 0.91, 116.34, 0.79, 1.40, 1.38, 0, 7.04, 1.50],
    "CNY": [11.34, 0.15, 0.13, 16.52, 0.11, 0.20, 0.20, 0.14, 0, 0.21],
    "NZD": [53.08, 0.72, 0.60, 77.30, 0.52, 0.93, 0.92, 0.66, 4.68, 0]
}

final=Label(root,text="",font=("Segoe UI", 15,"bold"))
final.grid(row=4,column=1,sticky='W',pady=10)

def calculate(event=''):
    if cur_val.get()==res_val.get():
        messagebox.showerror("Error","Both the currencies cannot be same.")
        return

    cur_index=cur_values.index(cur_val.get())
    res_index=cur_values.index(res_val.get())

    cu=cur1_values[cur_index]
    re=cur1_values[res_index]

    mul_factor=cur_dict[cu][res_index]

    res=cur.get()*mul_factor
    res_label.configure(text=res)
    
    final.configure(text=f"{cur.get()} {cu} is equal to {str(res)} {re}.",font=("Segoe UI", 15,"bold"))

calc = Button(root, width=15, text="Calculate", padding=(10, 10),command=calculate)
calc.grid(row=3, column=1, sticky='W', padx=40)

etr.bind('<Return>',calculate)
root.mainloop()