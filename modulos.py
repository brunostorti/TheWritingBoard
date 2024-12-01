import tkinter as tk
from PIL import Image, ImageTk

def iniciar_modulos():
    tela_modulos = tk.Tk()
    tela_modulos.title("Módulos de Redação")
    tela_modulos.configure(bg="#1c2533")  

    tela_modulos.attributes("-fullscreen", True)

    main_frame = tk.Frame(tela_modulos, bg="#1c2533", padx=20, pady=20)  
    main_frame.pack(expand=True, fill="both")

    try:
        img = Image.open("imagens/images.png") 
        img = img.resize((180, 180))  
        logo = ImageTk.PhotoImage(img)

        titulo_img = Image.open("imagens/titulo.png")  
        titulo_img = titulo_img.resize((240, 180))  
        titulo = ImageTk.PhotoImage(titulo_img)

        logos_frame = tk.Frame(main_frame, bg="#1c2533")
        logos_frame.pack(pady=(20, 10))

        logo_label = tk.Label(logos_frame, image=logo, bg="#1c2533")
        logo_label.image = logo
        logo_label.pack(side="left", padx=(10, 20))  

        titulo_label = tk.Label(logos_frame, image=titulo, bg="#1c2533")
        titulo_label.image = titulo
        titulo_label.pack(side="left")

    except Exception as e:
        print(f"Erro ao carregar as imagens: {e}")

    mensagem_bem_vindo = tk.Label(
        main_frame,
        text="Escolha um nível de redação",
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

    def abrir_nivel1():
        tela_modulos.destroy()
        import nivel1
        nivel1.tela_inicial1()

    def abrir_nivel2():
        tela_modulos.destroy()
        import nivel2
        nivel2.tela_inicial2()

    def abrir_nivel3():
        tela_modulos.destroy()
        import nivel3
        nivel3.tela_inicial3()

    def voltar_interface():
        tela_modulos.destroy()
        import interface
        interface.iniciar_interface()

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

    botao_nivel1 = tk.Button(botoes_frame, text="Nível 1", command=abrir_nivel1, **estilo_botao)
    botao_nivel1.grid(row=0, column=0, padx=20, pady=15, sticky="ew")

    botao_nivel2 = tk.Button(botoes_frame, text="Nível 2", command=abrir_nivel2, **estilo_botao)
    botao_nivel2.grid(row=1, column=0, padx=20, pady=15, sticky="ew")

    botao_nivel3 = tk.Button(botoes_frame, text="Nível 3", command=abrir_nivel3, **estilo_botao)
    botao_nivel3.grid(row=2, column=0, padx=20, pady=15, sticky="ew")

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