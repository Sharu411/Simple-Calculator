import tkinter
from tkinter import *
root=Tk()

root.title("Simple Calculator")
root.geometry("500x600+300+100")
root.resizable(False,False)
root.configure(bg="#1F1F1F")

equation=""

def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)
    
def clear():
    global equation
    equation=""
    label_result.config(text=equation)

def calculate():
    global equation
    result=""
    if equation!="":
        try:
            result=eval(equation)
        except:
            result="error"
            equation=""
    label_result.config(text=result)

label_result=Label(root,width=25,height=2,text="",font=("arial",30))
label_result.pack()
Button(root,text="(",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#696969",command=lambda:show("(")).place(x=15,y=105)
Button(root,text=")",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#696969",command=lambda:show(")")).place(x=135,y=105)
Button(root,text="/",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#696969",command=lambda:show("/")).place(x=255,y=105)
Button(root,text="%",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#696969",command=lambda:show("%")).place(x=375,y=105)


Button(root,text="7",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#696969",command=lambda:show("7")).place(x=15,y=200)
Button(root,text="8",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#696969",command=lambda:show("8")).place(x=135,y=200)
Button(root,text="9",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#696969",command=lambda:show("9")).place(x=255,y=200)
Button(root,text="*",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#696969",command=lambda:show("*")).place(x=375,y=200)

Button(root,text="4",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#696969",command=lambda:show("4")).place(x=15,y=300)
Button(root,text="5",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#696969",command=lambda:show("5")).place(x=135,y=300)
Button(root,text="6",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#696969",command=lambda:show("6")).place(x=255,y=300)
Button(root,text="-",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#696969",command=lambda:show("-")).place(x=375,y=300)


Button(root,text="1",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#696969",command=lambda:show("1")).place(x=15,y=400)
Button(root,text="2",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#696969",command=lambda:show("2")).place(x=135,y=400)
Button(root,text="3",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#696969",command=lambda:show("3")).place(x=255,y=400)
Button(root,text="+",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#696969",command=lambda:show("+")).place(x=375,y=400)

Button(root,text="C",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#007FFF",command=lambda:clear()).place(x=15,y=500)
Button(root,text="0",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#696969",command=lambda:show("0")).place(x=135,y=500)
Button(root,text=".",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#696969",command=lambda:show(".")).place(x=255,y=500)
Button(root,text="=",width=4,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#FF3030",command=lambda:calculate()).place(x=375,y=500)

root.mainloop()



