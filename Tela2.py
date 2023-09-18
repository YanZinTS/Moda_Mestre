from Modulos import *
import customtkinter as Tk


def Clique():
    pass



def AbrirJanela2():
    Janela.withdraw()
    Janela2.deiconify()
    Janela3.withdraw()


def AbrirJanela3():
    Janela.withdraw()
    Janela2.withdraw()
    Janela3.deiconify()


Tk.set_appearance_mode('Dark')

#janelas do projeto
Janela = CriarJanela('Entrada de Produtos e Acréscimo no Estoque', '1400x700', 1, Redimensionar=False)
Janela.iconbitmap('imagens/Icone.ico')

Janela2 = CriarJanela('Caixa - Saída de Produtos', '900x500', 2, Redimensionar=False)
Janela2.withdraw()

Janela3 = CriarJanela('Gerenciamento de Estoque', '900x500', 2, Redimensionar=False)
Janela3.withdraw()

#Abas Dos Produtos
Aba = CriarAba(Janela, 1300, 600, 6, 6, 'Camiseta', 'Calça', 'Cueca', 'Meia', 'Tênis')

#informações do produto

quantidadeLabel = CriarLabel(Aba.tab('Camiseta'), 'Quantidade:', 3, 5, 'White')
quantidade = CriarCaixaDeTexto(Aba.tab('Camiseta'), 200, 20, 3, 6, 'Digite a quantidade do produto')

tamanhoLabel = CriarLabel(Aba.tab('Camiseta'), 'Tamanho:', 4, 5, 'White')
tamanho = CriarCaixaDeTexto(Aba.tab('Camiseta'), 200, 20, 5, 6, 'Digite o tamanho do produto')

adicionar = CriarBotao(Aba.tab('Camiseta'), 'Adicionar ao estoque', Clique, 6, 6, 150, 30, 'Green', 'Black')

#trocar de janelas
btn1 = CriarBotao(Aba.tab('Camiseta'), 'Caixa - Saída de Produtos', AbrirJanela2, 12, 6, 350, 30)
btn2 = CriarBotao(Aba.tab('Camiseta'), 'Gerenciamento de Estoque', AbrirJanela3, 12, 7, 250, 30)


#controle pro estoque
LabelCamiseta = CriarLabel(Aba.tab('Camiseta'), 'Camiseta Blunt', 1, 8, 'White')
LabelCamiseta.configure(font=('Arial', 17, 'bold'))

ImagemCamisa = CriarImagem(Aba.tab('Camiseta'), 'imagens/Camisa.jpg', 2, 8, 200,200)

quantidadeProduto = CriarLabel(Aba.tab('Camiseta'), '5', 3, 8, 'white')

precoProduto = CriarLabel(Aba.tab('Camiseta'), 'R$99,90', 4, 8, 'white')
precoProduto.configure(font=('Arial', 15))

tamanhoProduto = CriarComboBox(Aba.tab('Camiseta'), 65, 30, 5, 8, ('PP','P', 'M', 'G', 'GG'))


Janela.mainloop()