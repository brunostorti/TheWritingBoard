import tkinter as tk

def iniciar_interface(nome="Usuário"):  # Valor padrão para o nome
    tela_interface = tk.Tk()
    tela_interface.title("The Writing Board - Interface")
    tela_interface.geometry("500x500")

    # Mensagem de boas-vindas
    mensagem_bem_vindo = tk.Label(
        tela_interface, text=f"Vamos jogar, {nome}!", font=("Arial", 18, "bold")
    )
    mensagem_bem_vindo.pack(pady=20)

    # Frame para organizar os botões
    botoes_frame = tk.Frame(tela_interface)
    botoes_frame.pack(pady=50)

    # Função para redirecionar para a tela de módulos
    def abrir_modulos():
        tela_interface.destroy()
        import modulos
        modulos.iniciar_modulos()

    # Função para redirecionar para a tela de regras
    def abrir_regras():
        tela_interface.destroy()
        import regras
        regras.iniciar_regras()

    # Função para redirecionar para a tela de ranking
    def abrir_ranking():
        tela_interface.destroy()
        import ranking
        ranking.iniciar_ranking()  # Certifique-se de que iniciar_ranking está implementada em ranking.py

    # Botões de navegação com largura e padding ajustados
    botao_modulos = tk.Button(botoes_frame, text="Módulos", width=15, command=abrir_modulos)
    botao_modulos.grid(row=0, column=0, padx=10, pady=5)

    botao_regras = tk.Button(botoes_frame, text="Regras", width=15, command=abrir_regras)
    botao_regras.grid(row=0, column=1, padx=10, pady=5)

    botao_ranking = tk.Button(botoes_frame, text="Ranking", width=15, command=abrir_ranking)
    botao_ranking.grid(row=0, column=2, padx=10, pady=5)

    # Função para voltar à tela de login
    def voltar_login():
        tela_interface.destroy()
        import login
        login.tela_login()

    # Botão "Sair" no canto superior direito
    botao_sair = tk.Button(tela_interface, text="Sair", command=voltar_login)
    botao_sair.pack(side=tk.TOP, anchor='ne', padx=10, pady=10)

    tela_interface.mainloop()

if __name__ == "__main__":
    iniciar_interface("Usuário")  # Altere o nome se necessário
