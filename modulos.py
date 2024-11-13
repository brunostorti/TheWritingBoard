import tkinter as tk

def iniciar_modulos():
    tela_modulos = tk.Tk()
    tela_modulos.title("The Writing Board - Módulos")
    tela_modulos.geometry("600x600")
    tela_modulos.configure(bg="#2d3e50")  # Cor de fundo azul-escuro

    # Título da tela com design aprimorado
    titulo = tk.Label(
        tela_modulos, 
        text="Selecione um Nível", 
        font=("Arial", 18, "bold"), 
        bg="#2d3e50", 
        fg="#f9d342"
    )
    titulo.pack(pady=30)

    # Frame para organizar os botões dos níveis
    botoes_frame = tk.Frame(tela_modulos, bg="#2d3e50")
    botoes_frame.pack(pady=40)

    # Definindo nome_usuario fixo (ou pode vir de outra tela)
    nome_usuario = "Usuário Teste"  # Substitua conforme necessário

    # Funções para redirecionamento de cada nível
    def abrir_nivel1():
        tela_modulos.destroy()  # Fecha a tela atual
        import nivel1  # Importa o arquivo nivel1.py
        nivel1.iniciar_nivel1(nome_usuario)  # Passa nome_usuario como argumento

    def abrir_nivel2():
        tela_modulos.destroy()  # Fecha a tela atual
        import nivel2  # Importa o arquivo nivel2.py
        nivel2.iniciar_nivel2(nome_usuario)  # Passa nome_usuario como argumento

    def abrir_nivel3():
        tela_modulos.destroy()  # Fecha a tela atual
        import nivel3  # Importa o arquivo nivel3.py
        nivel3.iniciar_nivel3(nome_usuario)  # Passa nome_usuario como argumento

    # Botões de seleção de nível com proporções e estilo aprimorados
    botao_nivel_1 = tk.Button(
        botoes_frame, 
        text="Nível 1", 
        width=15, 
        height=2, 
        command=abrir_nivel1, 
        font=("Arial", 12, "bold"), 
        bg="#5c80bc", 
        fg="white", 
        relief="raised", 
        activebackground="#4a6fa5", 
        cursor="hand2"
    )
    botao_nivel_1.grid(row=0, column=0, padx=15, pady=15)

    botao_nivel_2 = tk.Button(
        botoes_frame, 
        text="Nível 2", 
        width=15, 
        height=2, 
        command=abrir_nivel2, 
        font=("Arial", 12, "bold"), 
        bg="#5c80bc", 
        fg="white", 
        relief="raised", 
        activebackground="#4a6fa5", 
        cursor="hand2"
    )
    botao_nivel_2.grid(row=0, column=1, padx=15, pady=15)

    botao_nivel_3 = tk.Button(
        botoes_frame, 
        text="Nível 3", 
        width=15, 
        height=2, 
        command=abrir_nivel3, 
        font=("Arial", 12, "bold"), 
        bg="#5c80bc", 
        fg="white", 
        relief="raised", 
        activebackground="#4a6fa5", 
        cursor="hand2"
    )
    botao_nivel_3.grid(row=0, column=2, padx=15, pady=15)

    # Botão "Voltar" para retornar à tela anterior (interface.py)
    def voltar_interface():
        tela_modulos.destroy()
        import interface
        interface.iniciar_interface()

    botao_voltar = tk.Button(
        tela_modulos, 
        text="Voltar", 
        command=voltar_interface, 
        font=("Arial", 12, "bold"), 
        bg="#f9d342", 
        fg="#2d3e50", 
        relief="flat", 
        cursor="hand2"
    )
    botao_voltar.pack(side=tk.BOTTOM, pady=30)

    tela_modulos.mainloop()

if __name__ == "__main__":
    iniciar_modulos()
