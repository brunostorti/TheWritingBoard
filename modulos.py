import tkinter as tk

def iniciar_modulos():
    tela_modulos = tk.Tk()
    tela_modulos.title("The Writing Board - Módulos")
    tela_modulos.geometry("500x500")

    titulo = tk.Label(tela_modulos, text="Selecione um Nível", font=("Arial", 18, "bold"))
    titulo.pack(pady=20)

    botoes_frame = tk.Frame(tela_modulos)
    botoes_frame.pack(pady=50)

    # Funções para cada nível com redirecionamento
    def nivel_1():
        tela_modulos.destroy()  # Fecha a tela atual antes de abrir a próxima
        import nivel1
        nivel1.iniciar_nivel1()

    def nivel_2():
        tela_modulos.destroy()
        import nivel2
        nivel2.iniciar_nivel2()

    def nivel_3():
        import nivel3
        nivel3.iniciar_nivel3()  # Chama a função do nível 3 sem destruir a tela

    # Botões de seleção de nível
    botao_nivel_1 = tk.Button(botoes_frame, text="Nível 1", width=20, command=nivel_1)
    botao_nivel_1.grid(row=0, column=0, padx=10)

    botao_nivel_2 = tk.Button(botoes_frame, text="Nível 2", width=20, command=nivel_2)
    botao_nivel_2.grid(row=0, column=1, padx=10)

    botao_nivel_3 = tk.Button(botoes_frame, text="Nível 3", width=20, command=nivel_3)
    botao_nivel_3.grid(row=0, column=2, padx=10)

    # Botão "Voltar" para retornar à tela anterior (interface.py)
    def voltar_interface():
        tela_modulos.destroy()
        import interface
        interface.iniciar_interface()  # Agora, essa função pode ser chamada sem argumentos

    botao_voltar = tk.Button(tela_modulos, text="Voltar", command=voltar_interface)
    botao_voltar.pack(side=tk.BOTTOM, pady=20)

    tela_modulos.mainloop()

if __name__ == "__main__":
    iniciar_modulos()
