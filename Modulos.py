import customtkinter as Tk
from PIL import Image

#criar uma janela
def CriarJanela(Titulo, Tamanho, Tipo, Cor = 0, Redimensionar = False):
    Tk.set_appearance_mode("Dark")
    if Tipo == 1:
        Janela = Tk.CTk()
    else:
        Janela = Tk.CTkToplevel()
    Janela.title(Titulo)
    if Cor != 0:
        Janela.configure(fg_color=Cor)
    if Redimensionar == True:
        Janela.resizable(width=True, height=True)
    else:
        Janela.resizable(width=False, height=False)
    Colunas = list(range(13))
    Linhas = list(range(13))
    Janela.grid_columnconfigure(Colunas, weight=1)
    Janela.grid_rowconfigure(Linhas, weight=1)
    Janela.geometry(Tamanho)
    return Janela


#criar um Botão
def CriarBotao(Local, Texto, Comando, Linha, Coluna, Largura, Altura, Cor = 0, CorHover = 0):
    botao = Tk.CTkButton(Local, text=Texto, command=Comando, width=Largura, height=Altura)
    botao.grid(row=Linha, column=Coluna)
    if Cor != 0:
        botao.configure(fg_color=Cor)
    if CorHover != 0:
        botao.configure(hover_color=CorHover)
    return botao


#criar uma Caixa De Texto
def CriarCaixaDeTexto(Local, Largura, Altura, Linha, Coluna, Texto = 0, Password = False):
    Caixa = Tk.CTkEntry(Local, width=Largura, height=Altura)
    Caixa.grid(row=Linha, column=Coluna)
    if Texto != 0:
        Caixa.configure(placeholder_text=Texto)
    if Password == True:
        Caixa.configure(show='*')
    return Caixa


#criar o Label
def CriarLabel(Local, Texto, Linha, Coluna, Cor = 'Black'):
    Label = Tk.CTkLabel(Local, text=Texto)
    Label.grid(row=Linha, column=Coluna)
    if Cor != 'black':
        Label.configure(text_color=Cor)
    return Label

#criar o CheckBox
def CriarCheckBox(Local, Texto, Linha, Coluna, Comando=0):
    check = Tk.CTkCheckBox(Local, text=Texto)
    check.grid(row=Linha, column=Coluna)
    if Comando != 0:
        check.configure(command=Comando)
    return check


#criar o Switch
def CriarSwitch(Local, Texto, Linha, Coluna, Comando=0):
    switch = Tk.CTkSwitch(Local, text=Texto)
    switch.grid(row=Linha, column=Coluna)
    if Comando != 0:
        switch.configure(command=Comando)
    return switch


#criar ComboBox
def CriarComboBox(Local, Largura, Altura, Linha, Coluna, Lista, Comando=0):
    check = Tk.CTkComboBox(Local, width=Largura, height=Altura, values=Lista)
    check.grid(row=Linha, column=Coluna)
    if Comando != 0:
        check.configure(command=Comando)
    return check


#criar o ProgressBar
def CriarProgressBar(Local, Largura, Altura, Linha, Coluna, Enchimento, Comando = 0):
    progressBar = Tk.CTkProgressBar(Local, width=Largura, height=Altura)
    progressBar.grid(row=Linha, column=Coluna)
    progressBar.set(Enchimento)
    if Comando != 0:
        progressBar.configure(command=Comando)
    return progressBar


#criar o Slider
def CriarSlider(Local, Largura, Altura, Linha, Coluna, Comando = 0):
    slider = Tk.CTkSlider(Local, width=Largura, height=Altura)
    slider.grid(row=Linha, column=Coluna)
    if Comando != 0:
        slider.configure(command=Comando)
    return slider

#---------------Caixa de Texto (rolagem)---------------
def CriarTexto(Local,Linha,Coluna,Texto,Largura=0,Altura=0):
    caixatxt= Tk.CTkTextbox(Local,wrap="word")
    caixatxt.grid(row=Linha,column=Coluna,sticky="nsew")
    caixatxt.insert("0.0",Texto,)
    if Largura!=0:
        caixatxt.configure(width=Largura)
    if Altura!=0:
        caixatxt.configure(height=Altura)
    return caixatxt

#---------------Imagem---------------
def CriarImagem(Local,Caminho,Linha, Coluna,Altura,Largura):
    imagem_pillow = Image.open(Caminho)
    imageTk = Tk.CTkImage(imagem_pillow,size=[Largura,Altura])
    imagem = Tk.CTkLabel(Local, image=imageTk, text= '')
    imagem.grid(row=Linha, column =Coluna)
    return imagem