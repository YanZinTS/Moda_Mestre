from Modulos import *
import customtkinter as Tk

Tk.set_appearance_mode('Dark')

Janela = CriarJanela('Janela Principal', '1500x700', 1, Redimensionar=False)

LabelCamiseta = CriarLabel(Janela, 'Camiseta Blunt', 2, 6, 'White')
LabelCamiseta.configure(font=('Arial', 17, 'bold'))

ImagemCamiseta = CriarImagem(Janela, 'imagens/Camisa.jpg', 3, 6, 200, 200)



Janela.mainloop()