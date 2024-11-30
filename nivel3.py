import tkinter as tk
from pymongo import MongoClient
from tkinter import messagebox
from PIL import Image, ImageTk  # Certifique-se de importar o Image e ImageTk corretamente
import modulos  # Certifique-se de importar o módulo de módulos corretamente

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

# Função para iniciar o quiz de um nível
def iniciar_nivel3(nome_usuario):
    tela_nivel3 = tk.Tk()
    tela_nivel3.title(f"The Writing Board - Nível 3 (Jogador: {nome_usuario})")
    tela_nivel3.configure(bg="#2d3e50")

    # Tornando a janela em tela cheia
    tela_nivel3.attributes('-fullscreen', True)
    tela_nivel3.bind("<F11>", lambda event: tela_nivel3.attributes('-fullscreen', not tela_nivel3.attributes('-fullscreen')))
    tela_nivel3.bind("<Escape>", lambda event: tela_nivel3.attributes('-fullscreen', False))  # Esc para sair da tela cheia

    perguntas = buscar_perguntas(3)  # Busca as perguntas do nível 3

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
            pontuacao += 30
            label_pontuacao.config(text=f"Pontuação: {pontuacao}")
        indice_pergunta += 1
        exibir_pergunta()

    def finalizar_quiz():
        salvar_pontuacao("nivel3", pontuacao, nome_usuario)  # Salva a pontuação no banco de dados

        # Determina a imagem a ser exibida com base na pontuação
        casa = min(pontuacao // 30, 10)  # Cada 30 pontos representam uma casa, e no máximo até casa 10
        imagem_caminho = f"imagens/pinocasa{casa}.png"  # Caminho para a imagem

        try:
            img = Image.open(imagem_caminho)

            # Ajusta o tamanho da imagem dependendo da casa (caso seja a última casa, ajusta para um tamanho maior)
            if casa == 10:
                largura_maxima = 800  # Largura máxima da imagem
                altura_maxima = 800  # Altura máxima da imagem
                img.thumbnail((largura_maxima, altura_maxima))  # Ajusta a imagem para o tamanho máximo mantendo a proporção
            else:
                img = img.resize((tela_nivel3.winfo_width(), tela_nivel3.winfo_height()))  # Ajusta a imagem para tela cheia

            img_tk = ImageTk.PhotoImage(img)

            # Criar um label para a imagem
            imagem_label = tk.Label(tela_nivel3, image=img_tk, bg="#2d3e50")
            imagem_label.image = img_tk
            # Coloca a imagem na tela, mas sem sobrepor os botões
            imagem_label.place(relx=0.5, rely=0.5, anchor="center")  # Centraliza a imagem na tela

        except Exception as e:
            print(f"Erro ao carregar a imagem {imagem_caminho}: {e}")

        # Exibir botão para navegar para 'modulos.py' após terminar o quiz
        botao_navegar_modulos = tk.Button(tela_nivel3, text="Voltar para Módulos", command=navegar_para_modulos, font=("Arial", 18, "bold"), bg="#fbd11b", fg="#2d3e50", activebackground="#fbd11b", activeforeground="#2d3e50", width=20, height=2, cursor="hand2", relief="raised", bd=4)
        botao_navegar_modulos.pack(pady=135)  # Aumente o valor de "pady" para mover o botão para baixo

        # Remove a exibição das perguntas e pontuação após o quiz
        label_pergunta.pack_forget()
        label_pontuacao.pack_forget()

    def navegar_para_modulos():
        tela_nivel3.destroy()  # Fecha a tela do nível
        modulos.iniciar_modulos()  # Substitua esta linha com a navegação para a tela de módulos

    label_pergunta = tk.Label(tela_nivel3, text="", font=("Arial", 22), bg="#2d3e50", fg="#fbd11b", wraplength=450, justify="center")
    label_pergunta.pack(pady=40)

    label_pontuacao = tk.Label(tela_nivel3, text=f"Pontuação: {pontuacao}", font=("Arial", 18, "bold"), bg="#2d3e50", fg="#fbd11b")
    label_pontuacao.pack(pady=20)

    opcoes_botoes = []
    for i in range(4):
        botao = tk.Button(tela_nivel3, text="", command=lambda i=i: verificar_resposta(i), font=("Arial", 18, "bold"), bg="#fbd11b", fg="#2d3e50", activebackground="#fbd11b", activeforeground="#2d3e50", width=40, height=3, cursor="hand2", relief="raised", bd=4)
        botao.pack(pady=10)
        opcoes_botoes.append(botao)

    exibir_pergunta()  # Exibe a primeira pergunta

    tela_nivel3.mainloop()

# Função para exibir a tela inicial onde o usuário digita seu nome
def tela_inicial3():
    tela_inicial = tk.Tk()
    tela_inicial.title("Informe seu nome")
    tela_inicial.geometry("800x600")
    tela_inicial.configure(bg="#2d3e50")

    # Tornando a janela em tela cheia
    tela_inicial.attributes('-fullscreen', True)
    tela_inicial.bind("<F11>", lambda event: tela_inicial.attributes('-fullscreen', not tela_inicial.attributes('-fullscreen')))
    tela_inicial.bind("<Escape>", lambda event: tela_inicial.attributes('-fullscreen', False))  # Esc para sair da tela cheia

    label_instrucoes = tk.Label(tela_inicial, text="Digite seu nome para começar", font=("Arial", 22), bg="#2d3e50", fg="#fbd11b")
    label_instrucoes.pack(pady=40)

    entrada_nome = tk.Entry(tela_inicial, font=("Arial", 20), bg="#fbd11b", fg="#2d3e50", bd=2, relief="solid", width=30)
    entrada_nome.pack(pady=20)

    def iniciar_jogo():
        nome_usuario = entrada_nome.get()
        if nome_usuario.strip():  # Verifica se o nome não está vazio
            tela_inicial.destroy()  # Fecha a tela de nome
            iniciar_nivel3(nome_usuario)  # Inicia o jogo no nível 3 com o nome inserido
        else:
            # Se o nome estiver vazio, exibe um erro
            tk.messagebox.showerror("Erro", "Por favor, insira seu nome.")

    botao_iniciar = tk.Button(tela_inicial, text="Iniciar Jogo", command=iniciar_jogo, font=("Arial", 20), bg="#fbd11b", fg="#2d3e50", relief="raised", bd=4)
    botao_iniciar.pack(pady=40)

    tela_inicial.mainloop()

# Chama a função para exibir a tela inicial
tela_inicial3()