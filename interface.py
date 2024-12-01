import tkinter as tk
from PIL import Image, ImageTk

def iniciar_interface(nome="Usuário"):
    tela_interface = tk.Tk()
    tela_interface.title("The Writing Board - Interface")
    tela_interface.configure(bg="#1c2533")  

    tela_interface.attributes("-fullscreen", True)  

    main_frame = tk.Frame(tela_interface, bg="#1c2533", padx=20, pady=20) 
    main_frame.pack(expand=True, fill="both")

    try:
        img = Image.open("imagens/images.png")
        img = img.resize((180, 180))  
        logo = ImageTk.PhotoImage(img)
        logo_label = tk.Label(main_frame, image=logo, bg="#1c2533")
        logo_label.image = logo
        logo_label.pack(pady=(20, 10))
    except Exception as e:
        print(f"Erro ao carregar a imagem: {e}")

    mensagem_bem_vindo = tk.Label(
        main_frame,
        text=f"Bem-vindo, {nome}!",
        font=("Arial", 30, "bold"),
        bg="#1c2533",
        fg="#ffd700",  
        pady=10
    )
    mensagem_bem_vindo.pack(pady=(10, 5))

    linha = tk.Frame(main_frame, bg="#ffd700", height=3, width=300)  
    linha.pack(pady=(5, 15), fill="x")

    botoes_frame = tk.Frame(main_frame, bg="#1c2533")
    botoes_frame.pack(pady=40)

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

    estilo_botao = {
        "font": ("Arial", 16, "bold"),  
        "bg": "#ffd700",  
        "fg": "#1c2533", 
        "activebackground": "#e6c300", 
        "activeforeground": "white",
        "width": 25, 
        "height": 3,  
        "relief": "groove",
        "bd": 5,  
        "cursor": "hand2",
        "highlightthickness": 2,  
        "highlightbackground": "#ffd700",  
        "highlightcolor": "#ffd700"  
    }

    botao_modulos = tk.Button(botoes_frame, text="Módulos", command=abrir_modulos, **estilo_botao)
    botao_modulos.grid(row=0, column=0, padx=20, pady=15, sticky="ew")

    botao_regras = tk.Button(botoes_frame, text="Regras", command=abrir_regras, **estilo_botao)
    botao_regras.grid(row=0, column=1, padx=20, pady=15, sticky="ew")

    botao_ranking = tk.Button(botoes_frame, text="Ranking", command=abrir_ranking, **estilo_botao)
    botao_ranking.grid(row=1, column=0, padx=20, pady=15, sticky="ew")

    botao_perfil = tk.Button(botoes_frame, text="Perfil", command=abrir_perfil, **estilo_botao)
    botao_perfil.grid(row=1, column=1, padx=20, pady=15, sticky="ew")

    def voltar_login():
        tela_interface.destroy()
        import login 
        login.iniciar_login()  

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
        height=2,  
        relief="groove",
        bd=5,
        cursor="hand2",
        highlightthickness=2,
        highlightbackground="#ffd700",
        highlightcolor="#ffd700"
    )
    botao_sair.grid(row=2, column=0, columnspan=2, pady=(25, 0), sticky="ew") 

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