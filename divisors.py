import tkinter as tk
from tkinter import ttk

win=tk.Tk()

ttk.Label(win,text="Enter the value of N    ").grid(row=0,column=0,padx=4,pady=8,sticky=tk.W)

tx=tk.StringVar()
tx.set("The divisors of N   :     ")
d=ttk.Label(win,text=tx.get())
d.grid(row=1,column=0,sticky=tk.W,padx=2)

result=ttk.Label(win,text="")
result.grid(row=1,column=1,sticky=tk.W)

n=tk.IntVar()
n.set("")
etr=ttk.Entry(win,width=15,textvariable=n)
etr.grid(row=0,column=1,sticky=tk.W)
etr.focus()

def div():
    fact=""
    for i in range(1,n.get()+1):
        if n.get()%i==0:
            fact=fact+str(i)+"   "

    result.configure(text=fact)

val=ttk.Button(win,text="Validate",command=div)
val.grid(row=2,column=1,pady=2,sticky=tk.W)
win.mainloop()