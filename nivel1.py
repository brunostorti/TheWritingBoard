import tkinter as tk
from pymongo import MongoClient
from ranking import iniciar_ranking  # Importa a função de ranking

# Conectar ao MongoDB
client = MongoClient('mongodb+srv://joaoalvarez:PjOwQniGDQGSJzvo@cluster0.tguge.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['Projeto_PI']
pontuacoes_collection = db['pontuacoes']
usuarios_collection = db['nome']  # Nome da coleção de usuários

# Função para obter o nome do usuário logado
def obter_nome_usuario_logado():
    # Aqui você deve buscar o nome do usuário logado do seu sistema de autenticação
    # Como exemplo, vou pegar o primeiro nome da coleção de usuários, ajustando conforme seu sistema.
    usuario_logado = usuarios_collection.find_one()  # Modifique a consulta conforme necessário
    return usuario_logado["nome"] if usuario_logado else "Desconhecido"

def salvar_pontuacao(nivel, pontuacao, usuario):
    dados = {
        "nivel": nivel,
        "usuario": usuario,
        "pontuacao": pontuacao
    }
    pontuacoes_collection.insert_one(dados)

def buscar_perguntas():
    # Buscar todas as perguntas e opções da coleção 'perguntas1'
    perguntas_collection = db['perguntas1']  # Usar a coleção 'perguntas1' para este nível
    perguntas_cursor = perguntas_collection.find()
    perguntas = []
    for pergunta in perguntas_cursor:
        perguntas.append({
            "pergunta": pergunta["pergunta"],
            "opcoes": pergunta["opcoes"],
            "correta": pergunta["correta"]
        })
    return perguntas

def iniciar_nivel1():
    tela_nivel1 = tk.Tk()
    tela_nivel1.title("The Writing Board - Nível 1")
    tela_nivel1.geometry("500x500")
    tela_nivel1.configure(bg="#2d3e50")

    perguntas = buscar_perguntas()  # Busca as perguntas diretamente da coleção 'perguntas1'

    pontuacao = 0
    indice_pergunta = 0
    nome_usuario = obter_nome_usuario_logado()  # Pega o nome do usuário logado automaticamente

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
        salvar_pontuacao("nivel1", pontuacao, nome_usuario)  # Salva a pontuação com o nome do usuário logado
        tela_nivel1.destroy()  # Fecha a tela do nível
        iniciar_ranking(nome_usuario)  # Chama a função para exibir o ranking com o nome do usuário

    label_pergunta = tk.Label(tela_nivel1, text="", font=("Arial", 14), bg="#2d3e50", fg="#fbd11b", wraplength=450, justify="center")
    label_pergunta.pack(pady=20)

    label_pontuacao = tk.Label(tela_nivel1, text=f"Pontuação: {pontuacao}", font=("Arial", 12, "bold"), bg="#2d3e50", fg="#fbd11b")
    label_pontuacao.pack(pady=10)

    opcoes_botoes = []
    for i in range(4):
        botao = tk.Button(tela_nivel1, text="", command=lambda i=i: verificar_resposta(i), font=("Arial", 12, "bold"), bg="#fbd11b", fg="#2d3e50", activebackground="#fbd11b", activeforeground="#2d3e50", width=25, height=2, cursor="hand2")
        botao.pack(pady=5)
        opcoes_botoes.append(botao)

    exibir_pergunta()

    tela_nivel1.mainloop()

if __name__ == "__main__":
    iniciar_nivel1()  # Inicia o jogo no nível 1