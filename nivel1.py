import tkinter as tk
import json

def salvar_pontuacao(nivel, pontuacao, usuario):
    try:
        with open("pontuacoes.json", "r") as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        dados = {}

    if nivel not in dados:
        dados[nivel] = []
    dados[nivel].append({"usuario": usuario, "pontuacao": pontuacao})

    with open("pontuacoes.json", "w") as arquivo:
        json.dump(dados, arquivo)

def iniciar_nivel1(nome_usuario):
    tela_nivel1 = tk.Tk()
    tela_nivel1.title("The Writing Board - Nível 1")
    tela_nivel1.geometry("500x500")
    tela_nivel1.configure(bg="#2d3e50")

    perguntas = [
        {"pergunta": "O que é uma tese em um texto dissertativo?", "opcoes": ["Um exemplo", "Uma citação", "A principal ideia do autor", "Um argumento secundário"], "correta": 2},
        {"pergunta": "Para que serve o parágrafo de introdução?", "opcoes": ["Apresentar a conclusão", "Apresentar a tese", "Fornecer argumentos", "Criticar a tese"], "correta": 1},
        {"pergunta": "Qual a função dos argumentos em um texto dissertativo?", "opcoes": ["Apresentar dados", "Defender a tese", "Fornecer exemplos", "Contradizer a tese"], "correta": 1},
        {"pergunta": "Qual é o objetivo da conclusão de um texto dissertativo?", "opcoes": ["Introduzir novas ideias", "Resumir os argumentos", "Criticar a tese", "Apresentar a tese"], "correta": 1},
        {"pergunta": "O que caracteriza uma introdução eficiente?", "opcoes": ["Ser longa", "Ser vaga", "Contextualizar a tese", "Repetir a conclusão"], "correta": 2},
        {"pergunta": "Como um argumento deve ser estruturado?", "opcoes": ["Baseado em opinião", "Sem dados", "De forma lógica e fundamentada", "Sem relação com a tese"], "correta": 2},
        {"pergunta": "O que significa ser objetivo em um texto?", "opcoes": ["Usar opiniões pessoais", "Usar dados e fatos", "Fazer perguntas", "Usar linguagem poética"], "correta": 1},
        {"pergunta": "Qual o papel dos conectivos em um texto?", "opcoes": ["Separar ideias", "Conectar parágrafos", "Dar opinião", "Enfeitar o texto"], "correta": 1},
        {"pergunta": "Como um texto deve ser concluído?", "opcoes": ["Apresentando novas ideias", "Resumindo e reforçando a tese", "Com perguntas", "Com citações"], "correta": 1},
        {"pergunta": "Qual é a importância de um bom vocabulário?", "opcoes": ["Enfeitar o texto", "Tornar a leitura complexa", "Comunicar de forma clara", "Apresentar opiniões"], "correta": 2},
    ]

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
        salvar_pontuacao("nivel1", pontuacao, nome_usuario)
        tela_nivel1.destroy()
        iniciar_ranking(nome_usuario)

    label_pergunta = tk.Label(tela_nivel1, text="", font=("Arial", 14), bg="#2d3e50", fg="#fbd11b", wraplength=450, justify="center")
    label_pergunta.pack(pady=20)

    # Visor de pontuação
    label_pontuacao = tk.Label(tela_nivel1, text=f"Pontuação: {pontuacao}", font=("Arial", 12, "bold"), bg="#2d3e50", fg="#fbd11b")
    label_pontuacao.pack(pady=10)

    opcoes_botoes = []
    for i in range(4):
        botao = tk.Button(tela_nivel1, text="", command=lambda i=i: verificar_resposta(i), font=("Arial", 12, "bold"), bg="#fbd11b", fg="#2d3e50", activebackground="#fbd11b", activeforeground="#2d3e50", width=25, height=2, cursor="hand2")
        botao.pack(pady=5)
        opcoes_botoes.append(botao)

    exibir_pergunta()

    tela_nivel1.mainloop()

def iniciar_ranking(nome_usuario):
    tela_ranking = tk.Tk()
    tela_ranking.title("Ranking")
    tela_ranking.geometry("500x500")
    tela_ranking.configure(bg="#2d3e50")

    try:
        with open("pontuacoes.json", "r") as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        dados = {}

    ranking_texto = "Ranking\n\n"
    for nivel, pontuacoes in dados.items():
        ranking_texto += f"Nível {nivel}:\n"
        for entry in pontuacoes:
            ranking_texto += f"{entry['usuario']} - {entry['pontuacao']} pontos\n"

    label_ranking = tk.Label(tela_ranking, text=ranking_texto, font=("Arial", 12), bg="#2d3e50", fg="#fbd11b", justify="left")
    label_ranking.pack(pady=20)

    voltar_button = tk.Button(tela_ranking, text="Voltar", command=tela_ranking.destroy, font=("Arial", 12), bg="#fbd11b", fg="#2d3e50")
    voltar_button.pack(pady=10)

    tela_ranking.mainloop()

if __name__ == "__main__":
    iniciar_nivel1("Usuário Exemplo")
