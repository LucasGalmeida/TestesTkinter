import tkinter as tk

janela = tk.Tk()

lb1 = tk.Label(janela,text="teste")
lb1.grid(row=20, column=10)

lb2 = tk.Label(janela,text="teste2")
lb2.grid(row=21, column=11)


janela.geometry("500x200+600+200")

janela.mainloop()