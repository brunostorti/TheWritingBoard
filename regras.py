import tkinter as tk

def iniciar_regras():
    tela_regras = tk.Tk()
    tela_regras.title("The Writing Board - Regras")
    tela_regras.geometry("500x500")
    tela_regras.configure(bg="#2d3e50")  # Cor de fundo alterada para #2d3e50
    tela_regras.minsize(300, 400)

    # Texto das regras com pontuações específicas
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
        tela_regras,
        text=regras_texto,
        font=("Arial", 12),
        wraplength=450,
        justify="left",
        bg="#2d3e50",  # Cor de fundo do label igual ao fundo da janela
        fg="#fbd11b"   # Cor do texto em amarelo claro
    )
    label_regras.pack(pady=20, padx=10, fill=tk.BOTH, expand=True)

    # Função para voltar à interface principal
    def voltar_interface():
        tela_regras.destroy()
        import interface
        interface.iniciar_interface()

    # Botão "Voltar" com estilo
    botao_voltar = tk.Button(
        tela_regras,
        text="Voltar",
        command=voltar_interface,
        font=("Arial", 10, "bold"),
        bg="#fbd11b",     # Cor do botão em amarelo claro
        fg="#2d3e50",     # Cor do texto em roxo escuro
        activebackground="#fbd11b",  # Mantém a cor ao clicar
        activeforeground="#2d3e50", # Cor do texto ao clicar
        relief="raised",
        cursor="hand2",
        padx=10,
        pady=5
    )
    botao_voltar.pack(side=tk.BOTTOM, pady=20)

    tela_regras.mainloop()

if __name__ == "__main__":
    iniciar_regras()
