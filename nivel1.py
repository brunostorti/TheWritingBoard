import tkinter as tk
from tkinter import messagebox  # Para exibir mensagens de erro
from PIL import Image, ImageTk  # Para trabalhar com imagens
from pymongo import MongoClient
import modulos  # Certifique-se de importar o módulo corretamente

# Conectar ao MongoDB
client = MongoClient('mongodb+srv://joaoalvarez:PjOwQniGDQGSJzvo@cluster0.tguge.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['ProjetoPI']
pontuacoes_collection = db['pontuacoes']
usuarios_collection = db['usuarios']  # Nome correto da coleção de usuários

# Função para salvar a pontuação no banco de dados
def salvar_pontuacao(nivel, pontuacao, nome_usuario):
    dados = {
        "nivel": nivel,
        "nome": nome_usuario,  # Nome do usuário fornecido
        "pontuacao": pontuacao
    }
    pontuacoes_collection.insert_one(dados)  # Salva a pontuação no banco
    print(f"Pontuação salva para {nome_usuario}: {pontuacao}")  # Depuração

# Função para buscar as perguntas de um nível
def buscar_perguntas(nivel):
    perguntas_collection = db[f'perguntas{nivel}']
    perguntas_cursor = perguntas_collection.find()
    perguntas = []
    for pergunta in perguntas_cursor:
        perguntas.append({
            "pergunta": pergunta["pergunta"],
            "opcoes": pergunta["opcoes"],
            "correta": pergunta["correta"]
        })
    return perguntas

# Função para iniciar o quiz após o nome do usuário ser inserido
def iniciar_nivel1(nome_usuario):
    tela_nivel1 = tk.Tk()
    tela_nivel1.title(f"The Writing Board - Nível 1 (Jogador: {nome_usuario})")
    tela_nivel1.configure(bg="#2d3e50")

    # Tornando a janela em tela cheia
    tela_nivel1.attributes('-fullscreen', True)
    tela_nivel1.bind("<F11>", lambda event: tela_nivel1.attributes('-fullscreen', not tela_nivel1.attributes('-fullscreen')))
    tela_nivel1.bind("<Escape>", lambda event: tela_nivel1.attributes('-fullscreen', False))  # Esc para sair da tela cheia

    perguntas = buscar_perguntas(1)

    pontuacao = 0
    indice_pergunta = 0

    def exibir_pergunta():
        nonlocal indice_pergunta
        if indice_pergunta < len(perguntas):
            pergunta = perguntas[indice_pergunta]
            label_pergunta.config(text=pergunta["pergunta"])
            for i, opcao in enumerate(opcoes_botoes):
                opcao.config(text=pergunta["opcoes"][i])
        else:
            finalizar_quiz()

    def verificar_resposta(indice_opcao):
        nonlocal pontuacao, indice_pergunta
        if indice_opcao == perguntas[indice_pergunta]["correta"]:
            pontuacao += 5
            label_pontuacao.config(text=f"Pontuação: {pontuacao}")
        indice_pergunta += 1
        exibir_pergunta()

    def finalizar_quiz():
        salvar_pontuacao("nivel1", pontuacao, nome_usuario)  # Salva a pontuação no banco de dados

        # Determina a imagem a ser exibida
        casa = min(pontuacao // 5, 10)  # Garante que não passe de casa 10
        imagem_caminho = f"imagens/pinocasa{casa}.png"  # Caminho para a imagem

        try:
            img = Image.open(imagem_caminho)

            # Se a casa for a última (por exemplo, casa 10), ajusta a imagem para um tamanho grande, mantendo as proporções
            if casa == 10:
                largura_maxima = 800  # Largura máxima que a imagem pode ter
                altura_maxima = 800  # Altura máxima que a imagem pode ter
                img.thumbnail((largura_maxima, altura_maxima))  # Ajusta a imagem para o tamanho máximo mantendo a proporção
            else:
                img = img.resize((tela_nivel1.winfo_width(), tela_nivel1.winfo_height()))  # Ajusta o tamanho da imagem para tela cheia

            img_tk = ImageTk.PhotoImage(img)

            # Criar um label para a imagem
            imagem_label = tk.Label(tela_nivel1, image=img_tk, bg="#2d3e50")
            imagem_label.image = img_tk
            # Coloca a imagem na tela, mas sem sobrepor os botões
            imagem_label.place(relx=0.5, rely=0.5, anchor="center")  # Centraliza a imagem na tela

        except Exception as e:
            print(f"Erro ao carregar a imagem {imagem_caminho}: {e}")

        # Exibir botão para navegar para 'modulos.py' após terminar o quiz
        botao_navegar_modulos = tk.Button(tela_nivel1, text="Voltar para Módulos", command=navegar_para_modulos, font=("Arial", 18, "bold"), bg="#fbd11b", fg="#2d3e50", activebackground="#fbd11b", activeforeground="#2d3e50", width=20, height=2, cursor="hand2", relief="raised", bd=4)
        botao_navegar_modulos.place(relx=0.5, rely=0.9, anchor="center")  # Coloca o botão na parte inferior centralizada

        # Remove a exibição das perguntas e pontuação após o quiz
        label_pergunta.pack_forget()
        label_pontuacao.pack_forget()

    def navegar_para_modulos():
        tela_nivel1.destroy()  # Fecha a tela do nível
        modulos.iniciar_modulos()

    label_pergunta = tk.Label(tela_nivel1, text="", font=("Arial", 22), bg="#2d3e50", fg="#fbd11b", wraplength=800, justify="center", padx=10, pady=10)
    label_pergunta.pack(pady=40)

    label_pontuacao = tk.Label(tela_nivel1, text=f"Pontuação: {pontuacao}", font=("Arial", 18, "bold"), bg="#2d3e50", fg="#fbd11b")
    label_pontuacao.pack(pady=20)

    opcoes_botoes = []
    for i in range(4):
        botao = tk.Button(tela_nivel1, text="", command=lambda i=i: verificar_resposta(i), font=("Arial", 18, "bold"), bg="#fbd11b", fg="#2d3e50", activebackground="#fbd11b", activeforeground="#2d3e50", width=40, height=3, cursor="hand2", relief="raised", bd=4)
        botao.pack(pady=10)
        opcoes_botoes.append(botao)

    exibir_pergunta()

    tela_nivel1.mainloop()

# Função para exibir a tela inicial onde o usuário digita o nome
def tela_inicial1():
    tela_inicial = tk.Tk()
    tela_inicial.title("Informe seu nome")
    tela_inicial.geometry("800x600")
    tela_inicial.configure(bg="#2d3e50")

    tela_inicial.attributes('-fullscreen', True)
    tela_inicial.bind("<F11>", lambda event: tela_inicial.attributes('-fullscreen', not tela_inicial.attributes('-fullscreen')))
    tela_inicial.bind("<Escape>", lambda event: tela_inicial.attributes('-fullscreen', False))

    label_instrucoes = tk.Label(tela_inicial, text="Digite seu nome para começar", font=("Arial", 22), bg="#2d3e50", fg="#fbd11b")
    label_instrucoes.pack(pady=40)

    entrada_nome = tk.Entry(tela_inicial, font=("Arial", 20), bg="#fbd11b", fg="#2d3e50", bd=2, relief="solid", width=30)
    entrada_nome.pack(pady=20)

    def iniciar_jogo():
        nome_usuario = entrada_nome.get()
        if nome_usuario.strip():
            tela_inicial.destroy()
            iniciar_nivel1(nome_usuario)
        else:
            messagebox.showerror("Erro", "Por favor, insira seu nome.")

    botao_iniciar = tk.Button(tela_inicial, text="Iniciar Jogo", command=iniciar_jogo, font=("Arial", 20), bg="#fbd11b", fg="#2d3e50", relief="raised", bd=4)
    botao_iniciar.pack(pady=40)

    tela_inicial.mainloop()

if __name__ == "__main__":
    tela_inicial1()