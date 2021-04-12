import tkinter as tk
from tkinter import ttk

win=tk.Tk()
win.title("Adder")

ttk.Label(win,text="Enter value of integer N : ").grid(row=0,column=0,sticky=tk.W,padx=4,pady=4)

n=tk.IntVar()
ent=ttk.Entry(win,width=28,textvariable=n)
ent.grid(row=0,column=1,sticky=tk.W,padx=4,pady=4)
ent.focus()

res=ttk.Label(win,text="")
res.grid(row=1,column=1,sticky=tk.W,padx=4,pady=4)

def add():
    s=0
    for i in range(1,n.get()+1):
        s=s+i

    if n.get()==0 or n.get()==1:
        st=" = "
    elif n.get()==2:
        st=" 1 + 2 = "
    elif n.get()==3:
        st=" 1 + 2 + 3 = "
    else:
        st=f" 1 + 2 + 3 + ... + {str(n.get())} = "
    res.configure(text="The sum is"+st+str(s))

val=ttk.Button(win,text="Validate",width=28,command=add)
val.grid(row=2,column=1,sticky=tk.W,padx=4,pady=4)

win.mainloop()