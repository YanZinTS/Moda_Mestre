from Modulos import *
import customtkinter as Tk

Tk.set_appearance_mode('Dark')
Tk.set_default_color_theme('themes/dark-blue.json')

Janela = CriarJanela('Janela Principal', '1500x700', 1, Redimensionar=False)

Janela.mainloop()