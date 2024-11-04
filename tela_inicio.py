import tkinter as tk

# Função para redirecionar o jogador para a tela de login
def abrir_tela_login():
    tela_inicio.destroy()
    import login  # Importa o módulo de login
    login.tela_login()  # Chama a função que inicia a tela de login

# Configurações da tela de início
tela_inicio = tk.Tk()
tela_inicio.title("The Writing Board - Tela de Início")
tela_inicio.geometry("500x400")  # Define o tamanho inicial da janela

# Ajuste para redimensionamento responsivo
tela_inicio.columnconfigure(0, weight=1)
tela_inicio.rowconfigure([0, 1, 2], weight=1)

# Título do Jogo
titulo = tk.Label(tela_inicio, text="The Writing Board", font=("Arial", 24, "bold"))
titulo.grid(row=0, column=0, pady=(100, 20))  # Posiciona o título com espaçamento flexível

# Botão para a tela de login
botao_login = tk.Button(tela_inicio, text="Iniciar", font=("Arial", 16), command=abrir_tela_login)
botao_login.grid(row=1, column=0, pady=20, ipadx=10, ipady=5)  # Define espaçamento interno para o botão

# Ajusta a escala da interface para manter a proporção ao redimensionar a janela
def ajustar_tamanho(event):
    largura = event.width
    altura = event.height

    # Ajuste de fonte para título com base na largura
    novo_tamanho_titulo = max(16, int(largura / 25))
    titulo.config(font=("Arial", novo_tamanho_titulo, "bold"))

    # Ajuste de fonte para o botão
    novo_tamanho_botao = max(10, int(largura / 35))
    botao_login.config(font=("Arial", novo_tamanho_botao))

# Vincula o evento de redimensionamento
tela_inicio.bind("<Configure>", ajustar_tamanho)

# Inicia o loop da tela
tela_inicio.mainloop()
