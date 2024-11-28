import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Biblioteca para manipular imagens


def iniciar_interface(nome="Usuário"):
    tela_interface = tk.Tk()
    tela_interface.title("The Writing Board - Interface")
    tela_interface.geometry("600x500")
    tela_interface.configure(bg="#2d3e50")  # Cor de fundo da tela principal


    # Barra de título
    barra_titulo = tk.Frame(tela_interface, bg="#fbd11b", height=70)
    barra_titulo.pack(side=tk.TOP, fill=tk.X)


    # Carregar e exibir a imagem no cabeçalho
    try:
        imagem = Image.open("/mnt/data/images.jpeg")  # Caminho da imagem enviada
        imagem = imagem.resize((50, 50), Image.ANTIALIAS)  # Redimensiona a imagem
        imagem_tk = ImageTk.PhotoImage(imagem)


        logo_label = tk.Label(barra_titulo, image=imagem_tk, bg="#fbd11b")
        logo_label.image = imagem_tk  # Mantém a referência para exibir a imagem
        logo_label.pack(side=tk.LEFT, padx=10)
    except Exception as e:
        print(f"Erro ao carregar a imagem: {e}")


    # Título ao lado da imagem
    titulo_label = tk.Label(
        barra_titulo,
        text="The Writing Board",
        font=("Arial", 16, "bold"),
        bg="#fbd11b",
        fg="#2d3e50"
    )
    titulo_label.pack(side=tk.LEFT, pady=20)


    # Mensagem de boas-vindas
    mensagem_bem_vindo = tk.Label(
        tela_interface,
        text=f"Bem-vindo, {nome}!",
        font=("Arial", 18, "bold"),
        bg="#2d3e50",
        fg="white"
    )
    mensagem_bem_vindo.pack(pady=20)


    # Criar um frame com borda para os botões
    botoes_frame = tk.Frame(tela_interface, bg="#34495e", bd=5, relief="ridge")
    botoes_frame.pack(pady=30, padx=20)


    # Configuração de estilo dos botões
    estilo_botao = {
        "font": ("Arial", 12, "bold"),
        "bg": "#fbd11b",
        "fg": "#2d3e50",
        "activebackground": "#f8c320",
        "activeforeground": "white",
        "width": 15,
        "height": 2,
        "relief": "raised",
        "bd": 2,
        "cursor": "hand2"
    }


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


    def voltar_login():
        tela_interface.destroy()
        import login
        login.tela_login()


    # Botões organizados em grade no frame
    botao_modulos = tk.Button(botoes_frame, text="Módulos", command=abrir_modulos, **estilo_botao)
    botao_modulos.grid(row=0, column=0, padx=15, pady=10)


    botao_regras = tk.Button(botoes_frame, text="Regras", command=abrir_regras, **estilo_botao)
    botao_regras.grid(row=0, column=1, padx=15, pady=10)


    botao_ranking = tk.Button(botoes_frame, text="Ranking", command=abrir_ranking, **estilo_botao)
    botao_ranking.grid(row=1, column=0, padx=15, pady=10)


    botao_perfil = tk.Button(botoes_frame, text="Perfil", command=abrir_perfil, **estilo_botao)
    botao_perfil.grid(row=1, column=1, padx=15, pady=10)


    # Botão sair no canto superior direito
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
        cursor="hand2"
    )
    botao_sair.place(x=550, y=10, anchor="ne")  # Posicionado no canto superior direito


    # Rodapé com informações adicionais
    rodape = tk.Frame(tela_interface, bg="#34495e", height=40)
    rodape.pack(side=tk.BOTTOM, fill=tk.X)


    rodape_label = tk.Label(
        rodape,
        text="Desenvolvido por IMT- Mauá © 2024",
        font=("Arial", 10),
        bg="#34495e",
        fg="white"
    )
    rodape_label.pack(pady=10)


    tela_interface.mainloop()


if __name__ == "__main__":
    iniciar_interface("Usuário")