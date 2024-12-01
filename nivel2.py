import tkinter as tk
from pymongo import MongoClient
from PIL import Image, ImageTk
import modulos

client = MongoClient('mongodb+srv://joaoalvarez:PjOwQniGDQGSJzvo@cluster0.tguge.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['ProjetoPI']
pontuacoes_collection = db['pontuacoes']
usuarios_collection = db['usuarios']

def salvar_pontuacao(nivel, pontuacao, nome_usuario):
    dados = {
        "nivel": nivel,
        "nome": nome_usuario,
        "pontuacao": pontuacao
    }
    pontuacoes_collection.insert_one(dados)

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

def iniciar_nivel2(nome_usuario):
    tela_nivel2 = tk.Tk()
    tela_nivel2.title(f"The Writing Board - Nível 2 (Jogador: {nome_usuario})")
    tela_nivel2.configure(bg="#2d3e50")
    tela_nivel2.attributes('-fullscreen', True)
    tela_nivel2.bind("<F11>", lambda event: tela_nivel2.attributes('-fullscreen', not tela_nivel2.attributes('-fullscreen')))
    tela_nivel2.bind("<Escape>", lambda event: tela_nivel2.attributes('-fullscreen', False))

    perguntas = buscar_perguntas(2)
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
            pontuacao += 10
            label_pontuacao.config(text=f"Pontuação: {pontuacao}")
        indice_pergunta += 1
        exibir_pergunta()

    def finalizar_quiz():
        salvar_pontuacao("nivel2", pontuacao, nome_usuario)
        casa = min(pontuacao // 10, 10)
        imagem_caminho = f"imagens/pinocasa{casa}.png"
        try:
            img = Image.open(imagem_caminho)
            if casa == 10:
                largura_maxima = 800
                altura_maxima = 800
                img.thumbnail((largura_maxima, altura_maxima))
            else:
                img = img.resize((tela_nivel2.winfo_width(), tela_nivel2.winfo_height()))
            img_tk = ImageTk.PhotoImage(img)
            imagem_label = tk.Label(tela_nivel2, image=img_tk, bg="#2d3e50")
            imagem_label.image = img_tk
            imagem_label.place(relx=0.5, rely=0.5, anchor="center")
        except Exception as e:
            print(f"Erro ao carregar a imagem {imagem_caminho}: {e}")
        botao_navegar_modulos = tk.Button(tela_nivel2, text="Voltar para Módulos", command=navegar_para_modulos, font=("Arial", 14, "bold"), bg="#fbd11b", fg="#2d3e50", activebackground="#fbd11b", activeforeground="#2d3e50", width=20, height=2, cursor="hand2", relief="raised", bd=4)
        botao_navegar_modulos.place(relx=0.5, rely=0.9, anchor="center")
        label_pergunta.pack_forget()
        label_pontuacao.pack_forget()

    def navegar_para_modulos():
        tela_nivel2.destroy()
        modulos.iniciar_modulos()

    label_pergunta = tk.Label(tela_nivel2, text="", font=("Arial", 16), bg="#2d3e50", fg="#fbd11b", wraplength=500, justify="center", padx=10, pady=10)
    label_pergunta.pack(pady=20)
    label_pontuacao = tk.Label(tela_nivel2, text=f"Pontuação: {pontuacao}", font=("Arial", 14, "bold"), bg="#2d3e50", fg="#fbd11b")
    label_pontuacao.pack(pady=10)

    opcoes_botoes = []
    for i in range(4):
        botao = tk.Button(tela_nivel2, text="", command=lambda i=i: verificar_resposta(i), font=("Arial", 14, "bold"), bg="#fbd11b", fg="#2d3e50", activebackground="#fbd11b", activeforeground="#2d3e50", width=40, height=3, cursor="hand2", relief="raised", bd=4)
        botao.pack(pady=10)
        opcoes_botoes.append(botao)

    exibir_pergunta()
    tela_nivel2.mainloop()

def tela_inicial2():
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
            iniciar_nivel2(nome_usuario)
        else:
            tk.messagebox.showerror("Erro", "Por favor, insira seu nome.")

    botao_iniciar = tk.Button(tela_inicial, text="Iniciar", command=iniciar_jogo, font=("Arial", 14, "bold"), bg="#fbd11b", fg="#2d3e50", activebackground="#fbd11b", activeforeground="#2d3e50", width=20, height=2, cursor="hand2", relief="raised", bd=4)
    botao_iniciar.pack(pady=40)
    tela_inicial.mainloop()

tela_inicial2()
