import tkinter as tk

def iniciar_interface(nome="Usuário"):
    tela_interface = tk.Tk()
    tela_interface.title("The Writing Board - Interface")
    tela_interface.geometry("600x500")
    tela_interface.configure(bg="#2d3e50")  # Cor de fundo alterada para #2d3e50

    # Mensagem de boas-vindas com estilo aprimorado
    mensagem_bem_vindo = tk.Label(
        tela_interface,
        text=f"Vamos jogar, {nome}!",
        font=("Arial", 20, "bold"),
        bg="#2d3e50",
        fg="#fbd11b"  # Cor de texto alterada para #fbd11b (amarelo claro)
    )
    mensagem_bem_vindo.pack(pady=20)

    # Frame para organizar os botões de navegação
    botoes_frame = tk.Frame(tela_interface, bg="#2d3e50")
    botoes_frame.pack(pady=30)

    # Função para redirecionar para a tela de módulos
    def abrir_modulos():
        tela_interface.destroy()
        import modulos
        modulos.iniciar_modulos()

    # Função para redirecionar para a tela de regras
    def abrir_regras():
        tela_interface.destroy()
        import regras
        regras.iniciar_regras()

    # Função para redirecionar para a tela de ranking, passando o nome do usuário
    def abrir_ranking():
        tela_interface.destroy()
        import ranking
        ranking.iniciar_ranking(nome)

    # Função para redirecionar para a tela de perfil
    def abrir_perfil():
        tela_interface.destroy()
        import perfil
        perfil.iniciar_perfil()

    # Configuração de estilo para os botões com bordas arredondadas
    estilo_botao = {
        "font": ("Arial", 12, "bold"),
        "bg": "#fbd11b",  # Cor do botão alterada para #fbd11b (amarelo claro)
        "fg": "#2d3e50",  # Cor do texto do botão alterada para #2d3e50 (roxo escuro)
        "activebackground": "#f8c320",  # Cor de fundo do botão ao clicar
        "activeforeground": "white",
        "width": 15,
        "height": 2,  # Altura dos botões aumentada
        "relief": "raised",
        "bd": 2,
        "cursor": "hand2"
    }

    # Botões de navegação com o novo estilo, organizados em duas linhas
    botao_modulos = tk.Button(botoes_frame, text="Módulos", command=abrir_modulos, **estilo_botao)
    botao_modulos.grid(row=0, column=0, padx=15, pady=10)

    botao_regras = tk.Button(botoes_frame, text="Regras", command=abrir_regras, **estilo_botao)
    botao_regras.grid(row=0, column=1, padx=15, pady=10)

    botao_ranking = tk.Button(botoes_frame, text="Ranking", command=abrir_ranking, **estilo_botao)
    botao_ranking.grid(row=1, column=0, padx=15, pady=10)

    botao_perfil = tk.Button(botoes_frame, text="Perfil", command=abrir_perfil, **estilo_botao)
    botao_perfil.grid(row=1, column=1, padx=15, pady=10)

    # Função para voltar à tela de login
    def voltar_login():
        tela_interface.destroy()
        import login
        login.tela_login()

    # Botão "Sair" no canto superior direito com estilo aprimorado
    botao_sair = tk.Button(
        tela_interface,
        text="Sair",
        command=voltar_login,
        font=("Arial", 10, "bold"),
        bg="#fbd11b",
        fg="#2d3e50",
        activebackground="#f8c320",
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        padx=8,
        pady=4
    )
    botao_sair.pack(side=tk.TOP, anchor='ne', padx=10, pady=10)

    tela_interface.mainloop()

if __name__ == "__main__":
    iniciar_interface("Usuário")
