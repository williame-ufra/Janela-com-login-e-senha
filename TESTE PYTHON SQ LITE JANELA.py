import tkinter as tk

janela = tk.Tk()

janela.title("Janela principal")
janela["bg"] = "violet"
janela["background"] = "violet"

#LarguraxAltura+Esquerda+Topo
#300x300+100+100
janela.geometry("300x300+100+100")
janela.mainloop()
