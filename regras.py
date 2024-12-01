import tkinter as tk
from PIL import Image, ImageTk

def iniciar_regras():
    tela_regras = tk.Tk()
    tela_regras.title("The Writing Board - Regras")
    tela_regras.attributes("-fullscreen", True)
    tela_regras.configure(bg="#1c2533")

    frame_principal = tk.Frame(tela_regras, bg="#1c2533")
    frame_principal.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    frame_logo_titulo = tk.Frame(frame_principal, bg="#1c2533")
    frame_logo_titulo.pack(pady=(10, 30))

    try:
        img = Image.open("imagens/images.png")
        img = img.resize((120, 120))
        logo = ImageTk.PhotoImage(img)
        logo_label = tk.Label(frame_logo_titulo, image=logo, bg="#1c2533")
        logo_label.image = logo
        logo_label.pack(side=tk.LEFT, padx=(0, 20))
    except Exception as e:
        print(f"Erro ao carregar a logo: {e}")

    
    except Exception as e:
        print(f"Erro ao carregar o título: {e}")

    linha = tk.Canvas(frame_principal, bg="#ffd700", height=2, highlightthickness=0)
    linha.pack(fill=tk.X, pady=20)

    moldura_regras = tk.Frame(
        frame_principal,
        bg="#2a3b4d",
        relief="groove",
        bd=5,
        highlightbackground="#ffd700",
        highlightthickness=2
    )
    moldura_regras.pack(pady=20, padx=40, fill=tk.BOTH, expand=True)

    regras_texto = """
🖋️ **Bem-vindo ao The Writing Board!**

Objetivo:
- Complete cada nível respondendo corretamente às perguntas sobre redação.
- Cada nível possui uma dificuldade específica e pontuação diferenciada.

🎯 **Pontuações por Nível:**
- **Nível 1:** Cada acerto vale 5 pontos.
- **Nível 2:** Cada acerto vale 10 pontos.
- **Nível 3:** Cada acerto vale 30 pontos.

✨ Boa sorte e lembre-se: pratique sua escrita e análise!
"""
    label_regras = tk.Label(
        moldura_regras,
        text=regras_texto,
        font=("Segoe UI", 22),
        wraplength=900,
        justify="left",
        bg="#2a3b4d",
        fg="#ffffff",
        padx=20,
        pady=20
    )
    label_regras.pack(fill=tk.BOTH, expand=True)

    def voltar_interface():
        tela_regras.destroy()
        import interface
        interface.iniciar_interface()

    botao_voltar = tk.Button(
        frame_principal,
        text="⏪ Voltar",
        command=voltar_interface,
        font=("Segoe UI", 14, "bold"),
        bg="#ffd700",
        fg="#1c2533",
        activebackground="#e6c300",
        activeforeground="#1c2533",
        relief="raised",
        cursor="hand2",
        width=15,
        height=2
    )
    botao_voltar.pack(pady=(30, 10))

    rodape = tk.Frame(tela_regras, bg="#ffd700", height=40)
    rodape.pack(side=tk.BOTTOM, fill=tk.X)
    texto_rodape = tk.Label(
        rodape,
        text="© 2024 The Writing Board - IMT - Instituto Mauá de Tecnologia",
        font=("Segoe UI", 11, "italic"),
        bg="#ffd700",
        fg="#1c2533"
    )
    texto_rodape.pack()

    tela_regras.mainloop()

if __name__ == "__main__":
    iniciar_regras()