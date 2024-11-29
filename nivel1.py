import tkinter as tk
from pymongo import MongoClient

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
    # Busca as perguntas para o nível específico
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
    tela_nivel1.geometry("500x500")
    tela_nivel1.configure(bg="#2d3e50")

    perguntas = buscar_perguntas(1)  # Busca as perguntas do nível 1

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
        tela_nivel1.destroy()  # Fecha a tela do nível

    label_pergunta = tk.Label(tela_nivel1, text="", font=("Arial", 14), bg="#2d3e50", fg="#fbd11b", wraplength=450, justify="center")
    label_pergunta.pack(pady=20)

    label_pontuacao = tk.Label(tela_nivel1, text=f"Pontuação: {pontuacao}", font=("Arial", 12, "bold"), bg="#2d3e50", fg="#fbd11b")
    label_pontuacao.pack(pady=10)

    opcoes_botoes = []
    for i in range(4):
        botao = tk.Button(tela_nivel1, text="", command=lambda i=i: verificar_resposta(i), font=("Arial", 12, "bold"), bg="#fbd11b", fg="#2d3e50", activebackground="#fbd11b", activeforeground="#2d3e50", width=25, height=2, cursor="hand2")
        botao.pack(pady=5)
        opcoes_botoes.append(botao)

    exibir_pergunta()  # Exibe a primeira pergunta

    tela_nivel1.mainloop()

# Função para exibir a tela inicial onde o usuário digita o nome
def tela_inicial():
    tela_inicial = tk.Tk()
    tela_inicial.title("Informe seu nome")
    tela_inicial.geometry("400x300")
    tela_inicial.configure(bg="#2d3e50")

    label_instrucoes = tk.Label(tela_inicial, text="Digite seu nome para começar", font=("Arial", 14), bg="#2d3e50", fg="#fbd11b")
    label_instrucoes.pack(pady=20)

    entrada_nome = tk.Entry(tela_inicial, font=("Arial", 12), bg="#fbd11b", fg="#2d3e50")
    entrada_nome.pack(pady=10)

    def iniciar_jogo():
        nome_usuario = entrada_nome.get()
        if nome_usuario.strip():  # Verifica se o nome não está vazio
            tela_inicial.destroy()  # Fecha a tela de nome
            iniciar_nivel1(nome_usuario)  # Inicia o jogo no nível 1 com o nome inserido
        else:
            # Se o nome estiver vazio, exibe um erro
            tk.messagebox.showerror("Erro", "Por favor, insira seu nome.")

    botao_iniciar = tk.Button(tela_inicial, text="Iniciar Jogo", command=iniciar_jogo, font=("Arial", 12), bg="#fbd11b", fg="#2d3e50")
    botao_iniciar.pack(pady=20)

    tela_inicial.mainloop()

# Inicia o jogo a partir da tela inicial
if __name__ == "__main__":
    tela_inicial()  # Chama a função para exibir a tela inicial
