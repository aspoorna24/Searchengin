from tkinter import *
import wikipedia
from tkinter import messagebox
from tkinter.font import Font

def get_me():
    txt.delete(1.0,END)
    ent=en.get()
    try:
        ans=wikipedia.summary(ent)
    except:
        txt.insert(INSERT,"please check your input")
    txt.insert(INSERT,ent)
    txt.insert(INSERT,"  : ")
    txt.insert(INSERT,ans)
def get_cl():
   
    txt.delete(1.0,END)
def ge_pr():
    s = messagebox.askquestion("exit?","Do you want to exit")
    if s== "yes":
        root.quit()
root = Tk()
my_font=Font(family="Times New Roman",size=14,underline=1 )
tx=Label(root,text="Search The Person You Want",font=my_font)
tx.pack()
t=Label(root,text="Remember to enter the correct spelling",fg="red")
t.pack()
top=Frame(root)
en=Entry(top)
en.pack()
butt=Button(top,text="search",command=get_me)
butt.pack()

top.pack(side=TOP)

bot=Frame(root)
scroll =Scrollbar(bot)
scroll.pack(side=RIGHT,fill=Y)

txt=Text(bot,width=40,height=20,yscrollcommand = scroll.set,wrap=WORD)
scroll.config(command=txt.yview)
txt.pack()
but=Button(bot,text="clear",command=get_cl)
bu=Button(bot,text="Exit",command=ge_pr)

but.pack(side=RIGHT)
bu.pack(side=RIGHT)
bot.pack(side=BOTTOM)
root.geometry("400x450+300+200")
root.mainloop()
