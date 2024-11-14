import tkinter as tk
import subprocess

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

    # Funções para redirecionamento de cada nível usando subprocess
    def abrir_nivel1():
        tela_modulos.destroy()  # Fecha a tela atual
        subprocess.Popen(["python", "nivel1.py"])  # Abre o arquivo nivel1.py em um novo processo

    def abrir_nivel2():
        tela_modulos.destroy()  # Fecha a tela atual
        subprocess.Popen(["python", "nivel2.py"])  # Abre o arquivo nivel2.py em um novo processo

    def abrir_nivel3():
        tela_modulos.destroy()  # Fecha a tela atual
        subprocess.Popen(["python", "nivel3.py"])  # Abre o arquivo nivel3.py em um novo processo

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
        subprocess.Popen(["python", "interface.py"])

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
