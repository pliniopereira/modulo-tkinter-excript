from tkinter import *

janela = Tk()

lb = Label(janela, text="Fala galera!!!")
lb.place(x=100, y=100)

# wxh+4+t
janela.geometry("300x300+200+200")

janela.mainloop()