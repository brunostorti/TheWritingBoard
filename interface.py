import tkinter as tk
from PIL import Image, ImageTk

def iniciar_interface(nome="Usuário"):
    tela_interface = tk.Tk()
    tela_interface.title("The Writing Board - Interface")
    tela_interface.configure(bg="#1c2533")  # Fundo mais sofisticado (azul-acinzentado)

    # Habilitar tela cheia
    tela_interface.attributes("-fullscreen", True)  # Habilita a tela cheia

    # Frame principal para centralizar tudo, com margem nas laterais
    main_frame = tk.Frame(tela_interface, bg="#1c2533", padx=20, pady=20)  # Adicionando padding
    main_frame.pack(expand=True, fill="both")

    # Adicionando a logo ao centro superior
    try:
        img = Image.open("imagens/images.png")
        img = img.resize((180, 180))  # Redimensionar para 180x180 para ajuste fino
        logo = ImageTk.PhotoImage(img)
        logo_label = tk.Label(main_frame, image=logo, bg="#1c2533")
        logo_label.image = logo
        logo_label.pack(pady=(20, 10))
    except Exception as e:
        print(f"Erro ao carregar a imagem: {e}")

    # Mensagem de boas-vindas com estilo elegante
    mensagem_bem_vindo = tk.Label(
        main_frame,
        text=f"Bem-vindo, {nome}!",
        font=("Arial", 30, "bold"),
        bg="#1c2533",
        fg="#ffd700",  # Dourado suave
        pady=10
    )
    mensagem_bem_vindo.pack(pady=(10, 5))

    # Linha decorativa cortada
    linha = tk.Frame(main_frame, bg="#ffd700", height=3, width=300)  # Largura reduzida para ser menor
    linha.pack(pady=(5, 15), fill="x")

    # Criando um frame para botões com borda arredondada e sombreamento
    botoes_frame = tk.Frame(main_frame, bg="#1c2533")
    botoes_frame.pack(pady=40)

    # Funções de navegação
    def abrir_modulos():
        tela_interface.destroy()
        import modulos
        modulos.iniciar_modulos()

    def abrir_regras():
        tela_interface.destroy()
        import regras
        regras.iniciar_regras()

    def abrir_ranking():
        tela_interface.destroy()
        import ranking
        ranking.iniciar_ranking(nome)

    def abrir_perfil():
        tela_interface.destroy()
        import perfil
        perfil.iniciar_perfil()

    # Estilo aprimorado dos botões com bordas arredondadas e efeitos
    estilo_botao = {
        "font": ("Arial", 16, "bold"),  # Tamanho maior da fonte
        "bg": "#ffd700",  # Dourado
        "fg": "#1c2533",  # Texto em azul-acinzentado
        "activebackground": "#e6c300",  # Amarelo mais intenso ao clicar
        "activeforeground": "white",
        "width": 25,  # Botões mais largos
        "height": 3,  # Botões mais altos
        "relief": "groove",
        "bd": 5,  # Borda mais grossa
        "cursor": "hand2",
        "highlightthickness": 2,  # Efeito de borda ao passar o mouse
        "highlightbackground": "#ffd700",  # Cor da borda
        "highlightcolor": "#ffd700"  # Cor da borda ativa
    }

    # Botões organizados com espaçamento
    botao_modulos = tk.Button(botoes_frame, text="Módulos", command=abrir_modulos, **estilo_botao)
    botao_modulos.grid(row=0, column=0, padx=20, pady=15, sticky="ew")

    botao_regras = tk.Button(botoes_frame, text="Regras", command=abrir_regras, **estilo_botao)
    botao_regras.grid(row=0, column=1, padx=20, pady=15, sticky="ew")

    botao_ranking = tk.Button(botoes_frame, text="Ranking", command=abrir_ranking, **estilo_botao)
    botao_ranking.grid(row=1, column=0, padx=20, pady=15, sticky="ew")

    botao_perfil = tk.Button(botoes_frame, text="Perfil", command=abrir_perfil, **estilo_botao)
    botao_perfil.grid(row=1, column=1, padx=20, pady=15, sticky="ew")

    # Botão "Sair" posicionado abaixo dos outros botões
    def voltar_login():
        tela_interface.destroy()
        import login
        login.tela_login()

    botao_sair = tk.Button(
        botoes_frame,
        text="Sair",
        command=voltar_login,
        font=("Arial", 16, "bold"),
        bg="#ffd700",
        fg="#1c2533",
        activebackground="#e6c300",
        activeforeground="white",
        width=25,
        height=2,  # Um pouco menor em altura
        relief="groove",
        bd=5,
        cursor="hand2",
        highlightthickness=2,
        highlightbackground="#ffd700",
        highlightcolor="#ffd700"
    )
    botao_sair.grid(row=2, column=0, columnspan=2, pady=(25, 0), sticky="ew")  # Movido para linha abaixo e centralizado

    # Rodapé premium com sombra
    rodape = tk.Frame(tela_interface, bg="#ffd700", height=40, width=900)
    rodape.pack(side="bottom", fill="x")
    texto_rodape = tk.Label(
        rodape,
        text="© 2024 The Writing Board - IMT - Instituto Mauá de Tecnologia",
        font=("Arial", 11, "italic"),
        bg="#ffd700",
        fg="#1c2533"
    )
    texto_rodape.pack()

    tela_interface.mainloop()

if __name__ == "__main__":
    iniciar_interface("Usuário")
