import tkinter as tk
from PIL import Image, ImageTk

def iniciar_modulos():
    tela_modulos = tk.Tk()
    tela_modulos.title("Módulos de Redação")
    tela_modulos.configure(bg="#1c2533")  # Fundo sofisticado (azul-acinzentado)

    # Habilitar tela cheia
    tela_modulos.attributes("-fullscreen", True)

    # Frame principal para centralizar tudo
    main_frame = tk.Frame(tela_modulos, bg="#1c2533", padx=20, pady=20)  # Adicionando padding
    main_frame.pack(expand=True, fill="both")

    # Adicionando a logo images.png e título.png ao topo centralizado
    try:
        img = Image.open("imagens/images.png")  # Caminho da logo
        img = img.resize((180, 180))  # Redimensionar para ajuste
        logo = ImageTk.PhotoImage(img)

        titulo_img = Image.open("imagens/titulo.png")  # Caminho da imagem título
        titulo_img = titulo_img.resize((240, 180))  # Ajustar o tamanho da imagem título
        titulo = ImageTk.PhotoImage(titulo_img)

        # Criando um frame para armazenar as duas imagens
        logos_frame = tk.Frame(main_frame, bg="#1c2533")
        logos_frame.pack(pady=(20, 10))

        # Colocando as imagens lado a lado com espaçamento adequado
        logo_label = tk.Label(logos_frame, image=logo, bg="#1c2533")
        logo_label.image = logo
        logo_label.pack(side="left", padx=(10, 20))  # Ajuste entre as imagens (menor)

        titulo_label = tk.Label(logos_frame, image=titulo, bg="#1c2533")
        titulo_label.image = titulo
        titulo_label.pack(side="left")

    except Exception as e:
        print(f"Erro ao carregar as imagens: {e}")

    # Mensagem de boas-vindas
    mensagem_bem_vindo = tk.Label(
        main_frame,
        text="Escolha um nível de redação",
        font=("Arial", 30, "bold"),
        bg="#1c2533",
        fg="#ffd700",  # Dourado suave
        pady=10
    )
    mensagem_bem_vindo.pack(pady=(10, 5))

    # Linha decorativa cortada
    linha = tk.Frame(main_frame, bg="#ffd700", height=3, width=300)  # Largura reduzida
    linha.pack(pady=(5, 15), fill="x")

    # Criando um frame para botões com borda arredondada
    botoes_frame = tk.Frame(main_frame, bg="#1c2533")
    botoes_frame.pack(pady=40)

    # Funções de navegação
    def abrir_nivel1():
        tela_modulos.destroy()
        import nivel1
        nivel1.iniciar_nivel1()

    def abrir_nivel2():
        tela_modulos.destroy()
        import nivel2
        nivel2.iniciar_nivel2()

    def abrir_nivel3():
        tela_modulos.destroy()
        import nivel3
        nivel3.iniciar_nivel3()

    def voltar_interface():
        tela_modulos.destroy()
        import interface
        interface.iniciar_interface()

    # Estilo dos botões
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

    # Botões para os níveis
    botao_nivel1 = tk.Button(botoes_frame, text="Nível 1", command=abrir_nivel1, **estilo_botao)
    botao_nivel1.grid(row=0, column=0, padx=20, pady=15, sticky="ew")

    botao_nivel2 = tk.Button(botoes_frame, text="Nível 2", command=abrir_nivel2, **estilo_botao)
    botao_nivel2.grid(row=1, column=0, padx=20, pady=15, sticky="ew")

    botao_nivel3 = tk.Button(botoes_frame, text="Nível 3", command=abrir_nivel3, **estilo_botao)
    botao_nivel3.grid(row=2, column=0, padx=20, pady=15, sticky="ew")

    # Botão "Voltar"
    botao_voltar = tk.Button(
        botoes_frame,
        text="Voltar",
        command=voltar_interface,
        font=("Arial", 16, "bold"),
        bg="#ffd700",
        fg="#1c2533",
        activebackground="#e6c300",
        activeforeground="white",
        width=25,
        height=2,
        relief="groove",
        bd=5,
        cursor="hand2",
        highlightthickness=2,
        highlightbackground="#ffd700",
        highlightcolor="#ffd700"
    )
    botao_voltar.grid(row=3, column=0, columnspan=2, pady=(30, 0), sticky="ew")

    # Rodapé
    rodape = tk.Frame(tela_modulos, bg="#ffd700", height=40, width=900)
    rodape.pack(side="bottom", fill="x")
    texto_rodape = tk.Label(
        rodape,
        text="© 2024 The Writing Board - IMT - Instituto Mauá de Tecnologia",
        font=("Arial", 11, "italic"),
        bg="#ffd700",
        fg="#1c2533"
    )
    texto_rodape.pack()

    tela_modulos.mainloop()

if __name__ == "__main__":
    iniciar_modulos()
