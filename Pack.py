import tkinter as tk

janela = tk.Tk()

lb1 = tk.Label(janela, text="Teste", bg="gray")
lb1.pack(side=tk.LEFT, fill = tk.Y) # side=BOTTOM TOP LEFT RIGHT

janela.geometry("400x300+200+200")

janela.mainloop()