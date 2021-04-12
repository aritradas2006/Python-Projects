import tkinter as tk
from tkinter import ttk

win=tk.Tk()
win.title("Perfect Square")

ttk.Label(win,text="Enter integer N: ").grid(row=0,column=0,sticky=tk.W)
n=tk.StringVar()
n.set("")
ent=ttk.Entry(win,width=30,textvariable=n)
ent.grid(row=0,column=1,sticky=tk.W)
ent.focus()

def chk():
    for i in range(1,int(n.get())+1):
        if i*i==int(n.get()):
            res.configure(text=f"{n.get()} is perfect square {n.get()} = {str(i)} ^ 2")
            break
        
        res.configure(text=f"{n.get()} is not a perfect square.")

val=ttk.Button(win,width=30,text="Validate",command=chk)
val.grid(row=1,column=1,sticky=tk.W)

res=ttk.Label(win,text="")
res.grid(row=2,column=1,sticky=tk.W)
win.mainloop()