from tkinter import *

def bt_click():
    print("bt_click")

    lb["text"] = "Funcionou!!!"

janela = Tk()

bt = Button(janela, width=20, text="OK", command=bt_click)
bt.place(x=100, y=100)

lb = Label(janela, text="Fala galera!!!")
lb.place(x=100, y=150)

# wxh+4+t
janela.geometry("300x300+200+200")

janela.mainloop()