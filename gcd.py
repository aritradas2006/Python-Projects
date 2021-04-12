import tkinter as tk
from tkinter import ttk

win=tk.Tk()
win.title("GCD and LCM Finder")

ttk.Label(win,text="Enter value of m:   ").grid(row=0,column=0,padx=4,pady=5,sticky='W')
m=tk.IntVar()
m.set("")
etr=ttk.Entry(win,width=25,textvariable=m)
etr.grid(row=0,column=1,sticky='W')
etr.focus()

ttk.Label(win,text="Enter value of n:   ").grid(row=1,column=0,padx=4,pady=5,sticky='W')
n=tk.IntVar()
n.set("")
ttk.Entry(win,width=25,textvariable=n).grid(row=1,column=1,sticky='W')

ttk.Label(win,text="Choose function:   ").grid(row=2,column=0,padx=4,pady=5,sticky='W')
ch=tk.StringVar()

def a(event):
    if m.get()>n.get():
        y=m.get()
        x=n.get()
    else:
        y=n.get()
        x=m.get()
    
    def gcd(x,y):
        while(y>0):
            q=y//x
            r=y%x
            x=r
            y=q
        res.configure(text="GCD(m, n) = "+str(y))

    if ch.get()=="GCD":
        gcd(x,y)
    elif ch.get()=="LCM":
        lcm=(x*y)/gcd(x,y)
        res.configure(text="LCM(m, n) = "+str(lcm))    

combo=ttk.Combobox(win,textvariable=ch,value=("GCD","LCM"),state="readonly",width=22)
combo.grid(row=2,column=1,sticky='W',padx=4,pady=5)
combo.bind("<<ComboboxSelected>>",a)

res=ttk.Label(win,text="")
res.grid(row=3,column=1,sticky='W',padx=4,pady=5)
win.mainloop()