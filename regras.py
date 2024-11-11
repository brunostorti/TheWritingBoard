import tkinter as tk

def iniciar_regras():
    tela_regras = tk.Tk()
    tela_regras.title("The Writing Board - Regras")
    tela_regras.geometry("500x500")
    tela_regras.minsize(300, 400)  # Tamanho mínimo da janela

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

    # Usar um Label com wraplength para quebra de linha
    label_regras = tk.Label(tela_regras, text=regras_texto, font=("Arial", 12), wraplength=450, justify="left")
    label_regras.pack(pady=20, padx=10, fill=tk.BOTH, expand=True)  # Adicionando preenchimento e expansão

    # Botão "Voltar" para retornar à tela anterior (interface.py)
    def voltar_interface():
        tela_regras.destroy()
        import interface
        interface.iniciar_interface()

    botao_voltar = tk.Button(tela_regras, text="Voltar", command=voltar_interface)
    botao_voltar.pack(side=tk.BOTTOM, pady=20)

    tela_regras.mainloop()

if __name__ == "__main__":
    iniciar_regras()
