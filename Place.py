import tkinter as tk

# Modulo utilizada para passar paremetros
from functools import partial

# Cria a janela
janela = tk.Tk()

# Define o background
janela["bg"] = "gray"

# Define o titulo da janela
janela.title("Janela Principal")

# Escreve na janela
lb = tk.Label(janela, text="Salve Salve !!")

# Posiciona a string escrita
lb.place(x=50, y=130)


# Funcao que realiza uma ação ao clicar no botao
def bt_click():
    ed1.delete(0,tk.END)
    ed1.insert(0,"You Die...")
    lb["text"] = "Faliceu..."


def bt_click2():
    ed2.delete(0,tk.END)
    ed2.insert(0,"Forever Young")
    lb["text"] = "Jovem d++"
    #ed2.get() pega o texto

# Cria um botao para a janela
bt1 = tk.Button(janela, width=40, text="Clique para morrer instantaneamente", command=bt_click)
# bt1["command"] = partial(bt_click, bt1) # Passa "parametro" para a funcao bt_click
bt1.place(x=50, y=150)

# Cria campo de texto
ed1 = tk.Entry(janela)
ed1.place(x=350, y=155)

# Cria um botao para a janela
bt2 = tk.Button(janela, width=40, text="Clique para viver eternamente", command=bt_click2)
bt2.place(x=50, y=190)

ed2 = tk.Entry(janela)
ed2.place(x=350, y=195)

# Define a dimensao da janela
# Largura x Altura + Esquerda do video + Topo do video
# 300x300+100+100
janela.geometry("800x600+200+200")

janela.mainloop()
