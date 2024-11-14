import tkinter as tk
import json
from modulos import iniciar_modulos  # Importa a função iniciar_modulos de modulos.py

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
        json.dump(dados, arquivo, indent=4)


def iniciar_nivel3():
    tela_nivel3 = tk.Tk()
    tela_nivel3.title("The Writing Board - Nível 3")
    tela_nivel3.geometry("500x500")
    tela_nivel3.configure(bg="#2d3e50")

    perguntas = [
        {"pergunta": "O que caracteriza uma tese sofisticada em um texto dissertativo-argumentativo?", 
         "opcoes": ["Apresenta uma opinião pessoal", "É genérica e aplicável a vários contextos", "É clara e complexa, abordando nuances", "Evita controvérsias"], 
         "correta": 2},
        {"pergunta": "Qual é o papel dos conectivos em parágrafos de argumentação complexa?", 
         "opcoes": ["Introduzir novas ideias", "Estabelecer relações lógicas entre ideias", "Enfeitar o texto", "Aumentar o número de palavras"], 
         "correta": 1},
        {"pergunta": "Como a conclusão de um texto dissertativo deve ser estruturada para reforçar a tese?", 
         "opcoes": ["Reafirma a tese e propõe uma reflexão final", "Introduz novos argumentos", "Repete a introdução", "Apresenta opiniões"], 
         "correta": 0},
        {"pergunta": "Qual é o benefício de usar dados e citações em uma redação argumentativa?", 
         "opcoes": ["Evitar discussões", "Provar a veracidade da tese", "Fortalecer argumentos com autoridade", "Reduzir o texto"], 
         "correta": 2},
        {"pergunta": "O que define uma proposta de intervenção adequada em uma redação no estilo ENEM?", 
         "opcoes": ["Sugere um novo tema", "Apresenta uma solução vaga", "É detalhada e respeita os direitos humanos", "Evita detalhamentos"], 
         "correta": 2},
        {"pergunta": "Como a coesão lexical contribui para a clareza do texto?", 
         "opcoes": ["Evita repetições", "Diminui a precisão", "Torna o texto mais informal", "Exclui sinônimos"], 
         "correta": 0},
        {"pergunta": "Qual a importância de um repertório sociocultural em uma argumentação sólida?", 
         "opcoes": ["Torna a tese mais complexa", "Comprova a opinião pessoal", "Enriquece os argumentos com contexto", "Simplifica o texto"], 
         "correta": 2},
        {"pergunta": "Por que é importante variar a estrutura das frases em uma redação dissertativa?", 
         "opcoes": ["Para enfeitar o texto", "Para evitar monotonia e enriquecer o estilo", "Para manter a simplicidade", "Para garantir objetividade"], 
         "correta": 1},
        {"pergunta": "O que torna uma introdução impactante em uma redação dissertativa?", 
         "opcoes": ["Começa com um exemplo direto", "É vaga e genérica", "Contextualiza o tema e antecipa a tese", "Evita informações contextuais"], 
         "correta": 2},
        {"pergunta": "Como uma análise crítica pode enriquecer um argumento?", 
         "opcoes": ["Refuta a tese", "Adiciona complexidade e mostra diferentes perspectivas", "Simplifica o argumento", "Elimina detalhes"], 
         "correta": 1},
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
            pontuacao += 30
            label_pontuacao.config(text=f"Pontuação: {pontuacao}")
        indice_pergunta += 1
        exibir_pergunta()

    def finalizar_quiz():
        tela_nome = tk.Toplevel(tela_nivel3)
        tela_nome.title("Informe seu nome")
        tela_nome.geometry("300x150")
        label_nome = tk.Label(tela_nome, text="Digite seu nome:", font=("Arial", 12), bg="#2d3e50", fg="#fbd11b")
        label_nome.pack(pady=10)

        entrada_nome = tk.Entry(tela_nome, font=("Arial", 12), bg="#fbd11b", fg="#2d3e50")
        entrada_nome.pack(pady=10)

        def salvar_e_fechar():
            nome_usuario = entrada_nome.get()
            if nome_usuario:
                salvar_pontuacao("nivel3", pontuacao, nome_usuario)
                tela_nome.destroy()
                tela_nivel3.destroy()
                iniciar_ranking()  # Atualiza o ranking com o novo nome e pontuação
            else:
                label_nome.config(text="Por favor, digite um nome!", fg="red")

        botao_salvar = tk.Button(tela_nome, text="Salvar", command=salvar_e_fechar, font=("Arial", 12), bg="#fbd11b", fg="#2d3e50")
        botao_salvar.pack(pady=10)

    label_pergunta = tk.Label(tela_nivel3, text="", font=("Arial", 14), bg="#2d3e50", fg="#fbd11b", wraplength=450, justify="center")
    label_pergunta.pack(pady=20)

    label_pontuacao = tk.Label(tela_nivel3, text=f"Pontuação: {pontuacao}", font=("Arial", 12, "bold"), bg="#2d3e50", fg="#fbd11b")
    label_pontuacao.pack(pady=10)

    opcoes_botoes = []
    for i in range(4):
        botao = tk.Button(tela_nivel3, text="", command=lambda i=i: verificar_resposta(i), font=("Arial", 12, "bold"), bg="#fbd11b", fg="#2d3e50", activebackground="#fbd11b", activeforeground="#2d3e50", width=25, height=2, cursor="hand2")
        botao.pack(pady=5)
        opcoes_botoes.append(botao)

    exibir_pergunta()

    tela_nivel3.mainloop()


def iniciar_ranking():
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

    voltar_button = tk.Button(tela_ranking, text="Voltar", command=lambda: [tela_ranking.destroy(), iniciar_modulos()], font=("Arial", 12), bg="#fbd11b", fg="#2d3e50")
    voltar_button.pack(pady=10)

    tela_ranking.mainloop()


if __name__ == "__main__":
    iniciar_nivel3()
