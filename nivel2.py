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


def iniciar_nivel2():
    tela_nivel2 = tk.Tk()
    tela_nivel2.title("The Writing Board - Nível 2")
    tela_nivel2.geometry("500x500")
    tela_nivel2.configure(bg="#2d3e50")

    perguntas = [
        {"pergunta": "Em um texto argumentativo, qual é a função de um exemplo?", "opcoes": ["Reforçar a tese", "Introduzir novas ideias", "Discutir a conclusão", "Apresentar uma opinião pessoal"], "correta": 0},
        {"pergunta": "Como um argumento pode ser falho em um texto dissertativo?", "opcoes": ["Quando é repetido", "Quando não é fundamentado", "Quando não é claro", "Quando não é estruturado"], "correta": 1},
        {"pergunta": "Quais dos seguintes termos são usados para estruturar uma introdução eficaz?", "opcoes": ["Citações e exemplos", "Frases impactantes e dados", "Frases vagas e opiniões", "Reflexões sem fontes"], "correta": 1},
        {"pergunta": "Em um texto argumentativo, o que é necessário para reforçar a argumentação?", "opcoes": ["Exemplos e dados", "Opiniões pessoais", "Estilo literário", "Discussões sem fontes"], "correta": 0},
        {"pergunta": "Qual é a principal diferença entre uma dissertação e uma redação argumentativa?", "opcoes": ["A dissertação não requer argumentação", "A redação argumentativa defende um ponto de vista", "Ambas possuem a mesma estrutura", "A dissertação não apresenta conclusão"], "correta": 1},
        {"pergunta": "Ao elaborar um argumento, qual a importância de usar fontes confiáveis?", "opcoes": ["Aumentar a credibilidade", "Enfeitar o texto", "Impulsionar as opiniões pessoais", "Deixar o texto mais longo"], "correta": 0},
        {"pergunta": "Em qual das opções abaixo os conectivos têm maior relevância?", "opcoes": ["Para expressar opinião", "Para conectar argumentos de forma lógica", "Para tornar o texto mais informal", "Para separar ideias sem explicação"], "correta": 1},
        {"pergunta": "Qual é a melhor forma de concluir um texto argumentativo?", "opcoes": ["Fazendo uma reflexão sobre o tema", "Colocando uma nova tese", "Iniciando uma nova argumentação", "Apresentando dados irrelevantes"], "correta": 0},
        {"pergunta": "A clareza na argumentação é importante porque?", "opcoes": ["Torna o texto mais difícil de entender", "Facilita a compreensão e reforça a lógica do texto", "Diminui o impacto do texto", "Faz com que o texto fique mais longo"], "correta": 1},
        {"pergunta": "Qual é a relação entre a tese e os argumentos em um texto?", "opcoes": ["Os argumentos reforçam a tese", "A tese é apenas uma opinião", "A tese não precisa de argumentos", "Os argumentos desmentem a tese"], "correta": 0},
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
            pontuacao += 10
            label_pontuacao.config(text=f"Pontuação: {pontuacao}")
        indice_pergunta += 1
        exibir_pergunta()

    def finalizar_quiz():
        tela_nome = tk.Toplevel(tela_nivel2)
        tela_nome.title("Informe seu nome")
        tela_nome.geometry("300x150")
        label_nome = tk.Label(tela_nome, text="Digite seu nome:", font=("Arial", 12), bg="#2d3e50", fg="#fbd11b")
        label_nome.pack(pady=10)

        entrada_nome = tk.Entry(tela_nome, font=("Arial", 12), bg="#fbd11b", fg="#2d3e50")
        entrada_nome.pack(pady=10)

        def salvar_e_fechar():
            nome_usuario = entrada_nome.get()
            if nome_usuario:
                salvar_pontuacao("nivel2", pontuacao, nome_usuario)
                tela_nome.destroy()
                tela_nivel2.destroy()
                iniciar_ranking()  # Atualiza o ranking com o novo nome e pontuação
            else:
                label_nome.config(text="Por favor, digite um nome!", fg="red")

        botao_salvar = tk.Button(tela_nome, text="Salvar", command=salvar_e_fechar, font=("Arial", 12), bg="#fbd11b", fg="#2d3e50")
        botao_salvar.pack(pady=10)

    label_pergunta = tk.Label(tela_nivel2, text="", font=("Arial", 14), bg="#2d3e50", fg="#fbd11b", wraplength=450, justify="center")
    label_pergunta.pack(pady=20)

    label_pontuacao = tk.Label(tela_nivel2, text=f"Pontuação: {pontuacao}", font=("Arial", 12, "bold"), bg="#2d3e50", fg="#fbd11b")
    label_pontuacao.pack(pady=10)

    opcoes_botoes = []
    for i in range(4):
        botao = tk.Button(tela_nivel2, text="", command=lambda i=i: verificar_resposta(i), font=("Arial", 12, "bold"), bg="#fbd11b", fg="#2d3e50", activebackground="#fbd11b", activeforeground="#2d3e50", width=25, height=2, cursor="hand2")
        botao.pack(pady=5)
        opcoes_botoes.append(botao)

    exibir_pergunta()

    tela_nivel2.mainloop()


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
    iniciar_nivel2()
