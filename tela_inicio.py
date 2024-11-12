import tkinter as tk
from login import tela_login  # Importa a função tela_login de login.py

# Função para redirecionar o jogador para a tela de login
def abrir_tela_login():
    tela_inicio.destroy()  # Fecha a tela de início do Tkinter
    tela_login()  # Chama a função tela_login para exibir a tela de login

# Configurações da tela de início
tela_inicio = tk.Tk()
tela_inicio.title("The Writing Board - Tela de Início")
tela_inicio.geometry("600x600")  # Tamanho fixo para todas as telas
tela_inicio.configure(bg="#222831")  # Cor de fundo como nas outras telas

# Título do Jogo
titulo = tk.Label(
    tela_inicio,
    text="The Writing Board",
    font=("Arial", 32, "bold"),
    fg="#ffd369",  # Cor do texto, amarelo claro como nas outras telas
    bg="#222831"  # Cor de fundo da tela
)
titulo.pack(pady=50)

# Seção do Botão Iniciar
secao_botao = tk.Frame(tela_inicio, bg="#2d3e50", bd=5, relief="solid", padx=20, pady=20)
secao_botao.pack(pady=30)

botao_iniciar = tk.Button(
    secao_botao,
    text="Iniciar",
    font=("Arial", 14, "bold"),
    bg="#fbd11b",  # Cor do botão como nas outras telas
    fg="#222831",  # Cor do texto do botão
    activebackground="#e8c16e",  # Cor de fundo ao clicar
    activeforeground="white",
    relief="raised",
    bd=4,
    width=20,
    height=2,
    command=abrir_tela_login  # Modifica a função para chamar tela_login
)
botao_iniciar.pack()

# Inicia a tela
tela_inicio.mainloop()
