import tkinter as tk


calculet=''
def inputText(symbol):
    global calculet
    

    calculet += str(symbol)
    textBox.delete(1.0,"end")
    textBox.insert(1.0,calculet)

def evaluate():
    global calculet

    try:
        calculet=str(eval(calculet))
        textBox.delete(1.0,"end")
        textBox.insert(1.0,calculet)
        calculet=""
       
    except:
        textBox.insert(1.0,"Error")

def clear():
    global calculet
    calculet=''
    textBox.delete(1.0,"end")

root=tk.Tk()
root.geometry("255x370")
root.resizable(False,False)
root.title='Calculeter'
root.config(bg="#8A7D7A")



textBox=tk.Text(root,height=2,width=15,font=('Arial',24),background="#408E8B",fg='White',borderwidth=4)
textBox.grid(columnspan=2)


btn_1=tk.Button(root,height=2,width=4,text="1",font=('Arial',15),bg="#65A697",command=lambda: inputText(1)).place(x=10,y=90)
btn_2=tk.Button(root,height=2,width=4,text="2",font=('Arial',15),bg="#65A697",command=lambda: inputText(2)).place(x=70,y=90)
btn_3=tk.Button(root,height=2,width=4,text="3",font=('Arial',15),bg="#65A697",command=lambda: inputText(3)).place(x=130,y=90)
btn_plas=tk.Button(root,height=2,width=4,text="+",font=('Arial',15),bg="#65A697",command=lambda: inputText('+')).place(x=190,y=90)

btn_4=tk.Button(root,height=2,width=4,text="4",font=('Arial',15),bg="#65A697",command=lambda: inputText(4)).place(x=10,y=160)
btn_5=tk.Button(root,height=2,width=4,text="5",font=('Arial',15),bg="#65A697",command=lambda: inputText(5)).place(x=70,y=160)
btn_6=tk.Button(root,height=2,width=4,text="6",font=('Arial',15),bg="#65A697",command=lambda: inputText(6)).place(x=130,y=160)
btn_minus=tk.Button(root,height=2,width=4,text="-",font=('Arial',15),bg="#65A697",command=lambda: inputText("-")).place(x=190,y=160)

btn_7=tk.Button(root,height=2,width=4,text="7",font=('Arial',15),bg="#65A697",command=lambda: inputText(7)).place(x=10,y=230)
btn_8=tk.Button(root,height=2,width=4,text="8",font=('Arial',15),bg="#65A697",command=lambda: inputText(8)).place(x=70,y=230)
btn_9=tk.Button(root,height=2,width=4,text="9",font=('Arial',15),bg="#65A697",command=lambda: inputText(9)).place(x=130,y=230)
btn_mul=tk.Button(root,height=2,width=4,text="x",font=('Arial',15),bg="#65A697",command=lambda: inputText("*")).place(x=190,y=230)

btn_clear=tk.Button(root,height=2,width=4,text="C",bg="#FF2E00",font=('Arial',15),fg="white",command=clear).place(x=10,y=300)
btn_0=tk.Button(root,height=2,width=4,text="0",font=('Arial',15),bg="#65A697",command=lambda: inputText(0)).place(x=70,y=300)
btn_elal=tk.Button(root,height=2,width=9,text="=",font=('Arial',15),bg="#65A697",command=evaluate).place(x=135,y=300)

root.mainloop()