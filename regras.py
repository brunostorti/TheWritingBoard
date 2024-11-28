import tkinter as tk
from PIL import Image, ImageTk

def iniciar_regras():
    tela_regras = tk.Tk()
    tela_regras.title("The Writing Board - Regras")
    tela_regras.attributes("-fullscreen", True)  # Tela cheia
    tela_regras.configure(bg="#1c2533")  # Cor de fundo compatível com a interface
    tela_regras.minsize(800, 900)  # Tamanho mínimo, ajustando conforme o conteúdo

    # Frame principal para organizar os elementos
    frame_principal = tk.Frame(tela_regras, bg="#1c2533")
    frame_principal.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    # Frame para colocar a logo e o título lado a lado
    frame_logo_titulo = tk.Frame(frame_principal, bg="#1c2533")
    frame_logo_titulo.pack(pady=(10, 20))

    # Adicionando a logo à esquerda
    try:
        img = Image.open("imagens/images.png")
        img = img.resize((150, 150))  # Redimensiona a imagem para 150x150
        logo = ImageTk.PhotoImage(img)
        logo_label = tk.Label(frame_logo_titulo, image=logo, bg="#1c2533")
        logo_label.image = logo
        logo_label.pack(side=tk.LEFT, padx=(0, 20))  # Posiciona à esquerda com espaçamento
    except Exception as e:
        print(f"Erro ao carregar a imagem da logo: {e}")

    # Adicionando a imagem de título à direita
    try:
        titulo_img = Image.open("imagens/titulo.png")
        titulo_img = titulo_img.resize((800, 250))  # Aumenta a imagem para 800x200
        titulo_logo = ImageTk.PhotoImage(titulo_img)
        titulo_label = tk.Label(frame_logo_titulo, image=titulo_logo, bg="#1c2533")
        titulo_label.image = titulo_logo
        titulo_label.pack(side=tk.LEFT)  # Posiciona à direita da logo
    except Exception as e:
        print(f"Erro ao carregar a imagem do título: {e}")

    # Moldura estilizada para as regras
    moldura_regras = tk.Frame(
        frame_principal,
        bg="#3e5060",  # Fundo mais escuro
        relief="groove",  # Estilo de borda
        bd=5  # Largura da borda
    )
    moldura_regras.pack(pady=10, fill=tk.BOTH, expand=True)

    # Texto das regras
    regras_texto = """
Bem-vindo ao The Writing Board!

Objetivo:
Complete cada nível respondendo corretamente às perguntas sobre redação.
Cada nível possui uma dificuldade específica e pontuação diferenciada.

Pontuações por Nível:
- Nível 1: Cada acerto vale 5 pontos.
- Nível 2: Cada acerto vale 10 pontos.
- Nível 3: Cada acerto vale 30 pontos.

Boa sorte e lembre-se: pratique sua escrita e análise!
"""

    # Label das regras estilizada
    label_regras = tk.Label(
        moldura_regras,
        text=regras_texto,
        font=("Arial", 16),
        wraplength=800,
        justify="left",
        bg="#3e5060",
        fg="#ffd700",  # Cor dourada
        padx=20,
        pady=20
    )
    label_regras.pack(fill=tk.BOTH, expand=True)

    # Função para voltar à interface principal
    def voltar_interface():
        tela_regras.destroy()
        import interface  # Substitua isso pelo nome correto do arquivo interface.py
        interface.iniciar_interface()

    # Botão estilizado "Voltar" com tamanho ajustado
    botao_voltar = tk.Button(
        frame_principal,
        text="Voltar",
        command=voltar_interface,
        font=("Arial", 14, "bold"),  # Tamanho de fonte reduzido
        bg="#ffd700",      # Cor dourada
        fg="#1c2533",      # Texto em azul escuro
        activebackground="#e6c300",  # Amarelo mais intenso
        activeforeground="#1c2533",
        relief="ridge",
        cursor="hand2",
        width=12,   # Largura do botão reduzida
        height=2    # Altura do botão reduzida
    )
    botao_voltar.pack(side=tk.BOTTOM, pady=20)  # Menor espaçamento entre o botão e o fundo

    tela_regras.mainloop()

if __name__ == "__main__":
    iniciar_regras()