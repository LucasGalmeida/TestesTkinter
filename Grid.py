import tkinter as tk

janela = tk.Tk()

lb1 = tk.Label(janela, text="Login:")
lb2 = tk.Label(janela, text="Senha:")

ed1 = tk.Entry(janela)
ed2 = tk.Entry(janela,show="*")

bt1 = tk.Button(janela, text="Confirmar")

lb1.grid(row=0, column=0)
lb2.grid(row=1, column=0)
ed1.grid(row=0, column=1)
ed2.grid(row=1, column=1)
bt1.grid(row=2, column=1)

janela.geometry("200x100+100+100")

janela.mainloop()

# stick > indica o sentido que o elemento estara na tela
# rowspan e columnspan > Mescla linhas e colunas
