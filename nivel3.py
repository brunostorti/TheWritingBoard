import tkinter as tk
from tkinter import messagebox, simpledialog
import json

# Configuração inicial da pontuação e listas de perguntas
pontos = 0

# Perguntas do Nível 1 (já definidas anteriormente)
questions_nivel1 = [
    {
        "question": "O que é uma tese em um texto dissertativo?",
        "options": ["1. Um exemplo", "2. Uma citação", "3. A principal ideia do autor", "4. Um argumento secundário"],
        "answer": 3
    },
    {
        "question": "Para que serve o parágrafo de introdução?",
        "options": ["1. Apresentar a conclusão", "2. Apresentar a tese", "3. Fornecer argumentos", "4. Criticar a tese"],
        "answer": 2
    },
    # ... (demais perguntas do Nível 1)
]

# Perguntas do Nível 3
questions_nivel3 = [
    {
        "question": "Qual é o objetivo principal de uma proposta de intervenção?",
        "options": ["1. Finalizar o texto", "2. Apresentar soluções para o problema", "3. Criticar o tema", "4. Explicar a tese"],
        "answer": 2
    },
    {
        "question": "O que é uma proposta de solução viável?",
        "options": ["1. Uma solução utópica", "2. Uma solução possível e exequível", "3. Uma crítica ao problema", "4. Um resumo do texto"],
        "answer": 2
    },
    {
        "question": "Qual é a importância do agente na proposta de intervenção?",
        "options": ["1. Apontar responsabilidades específicas", "2. Aumentar a conclusão", "3. Desenvolver o argumento", "4. Reforçar a introdução"],
        "answer": 1
    },
    {
        "question": "O que se entende por detalhamento na proposta de intervenção?",
        "options": ["1. Descrever a estrutura do texto", "2. Especificar as ações a serem tomadas", "3. Introduzir a tese", "4. Apresentar dados"],
        "answer": 2
    },
    {
        "question": "Por que a proposta de intervenção deve ser articulada com os argumentos?",
        "options": ["1. Para ampliar o desenvolvimento", "2. Para sustentar a tese com dados", "3. Para oferecer soluções conectadas aos problemas", "4. Para criticar o texto"],
        "answer": 3
    },
    {
        "question": "Em qual parte da redação a proposta de intervenção é inserida?",
        "options": ["1. Na introdução", "2. No desenvolvimento", "3. Na conclusão", "4. Em qualquer parágrafo"],
        "answer": 3
    },
    {
        "question": "Quais elementos devem constar em uma proposta de intervenção?",
        "options": ["1. Agente, ação, detalhamento, meio, e finalidade", "2. Tese, argumentos, exemplo", "3. Introdução, desenvolvimento e conclusão", "4. Narrador, personagem e enredo"],
        "answer": 1
    },
    {
        "question": "Qual é a finalidade na proposta de intervenção?",
        "options": ["1. Reforçar a conclusão", "2. Apontar o problema", "3. Indicar o objetivo final da ação", "4. Introduzir o agente"],
        "answer": 3
    },
    {
        "question": "Em que situação a proposta de intervenção pode ser penalizada?",
        "options": ["1. Quando está clara e viável", "2. Quando está incompleta ou incoerente", "3. Quando é detalhada", "4. Quando inclui dados e citações"],
        "answer": 2
    },
    {
        "question": "A proposta de intervenção é um elemento obrigatório na redação do ENEM?",
        "options": ["1. Sim, é obrigatória", "2. Não, é opcional", "3. Apenas se o tema for social", "4. Apenas se o tema for cultural"],
        "answer": 1
    }
]

# Função para atualizar o ranking
def atualizar_ranking(nome_jogador, pontos):
    try:
        with open('ranking.json', 'r') as file:
            ranking = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        ranking = []

    # Adiciona a pontuação do jogador ao ranking
    ranking.append({"nome": nome_jogador, "pontos": pontos})

    with open('ranking.json', 'w') as file:
        json.dump(ranking, file)

# Função para iniciar o Nível 3
def iniciar_nivel3():
    global pontos
    pontos = 0  # Resetar pontos no início do nível

    # Configuração da janela
    tela_nivel3 = tk.Tk()
    tela_nivel3.title("Nível 3 - Proposta de Intervenção")
    tela_nivel3.geometry("500x500")

    # Exibir visor de pontos
    score_label = tk.Label(tela_nivel3, text=f"Pontos: {pontos}", font=("Arial", 16))
    score_label.pack(pady=10)

    # Variável para controlar a pergunta atual
    pergunta_atual = 0

    # Função para atualizar o visor de pontos
    def update_score():
        score_label.config(text=f"Pontos: {pontos}")

    # Função para mostrar a próxima pergunta
    def show_question():
        nonlocal pergunta_atual
        if pergunta_atual < len(questions_nivel3):
            question = questions_nivel3[pergunta_atual]
            question_text = question["question"]
            options = question["options"]
            answer = question["answer"]

            question_label.config(text=question_text)

            # Atualizar as opções
            for i, option in enumerate(options):
                option_buttons[i].config(text=option, command=lambda ans=i+1: check_answer(ans, answer))

        else:
            # Final do nível e pontuação total
            finalizar_nivel()

    # Verificar resposta e atualizar pontuação
    def check_answer(selected_answer, correct_answer):
        nonlocal pergunta_atual
        global pontos
        if selected_answer == correct_answer:
            pontos += 30  # Acrescentar pontos para resposta correta
            update_score()  # Atualiza o visor de pontos

        pergunta_atual += 1
        show_question()  # Avança para a próxima pergunta diretamente

    # Layout da pergunta
    question_label = tk.Label(tela_nivel3, text="", wraplength=400, font=("Arial", 12))
    question_label.pack(pady=20)

    # Botões para opções
    option_buttons = [tk.Button(tela_nivel3, text="", font=("Arial", 12)) for _ in range(4)]
    for btn in option_buttons:
        btn.pack(pady=5)

    # Botão para iniciar perguntas do Nível 3
    start_button = tk.Button(tela_nivel3, text="Iniciar Perguntas do Nível 3", command=lambda: [show_question(), start_button.config(state="disabled")])
    start_button.pack(pady=20)

    # Botão "Voltar" para retornar ao módulo
    def voltar_modulos():
        tela_nivel3.destroy()
        import modulos
        modulos.iniciar_modulos()

    botao_voltar = tk.Button(tela_nivel3, text="Voltar", command=voltar_modulos)
    botao_voltar.pack(side=tk.BOTTOM, pady=20)

    def finalizar_nivel():
        global pontos
        nome_jogador = simpledialog.askstring("Registro no Ranking", "Digite seu nome para registrar no ranking:")
        if nome_jogador:
            messagebox.showinfo("Nível 3 Concluído", f"Você finalizou o Nível 3 com {pontos} pontos!")
            atualizar_ranking(nome_jogador, pontos)  # Atualizar ranking com a pontuação final

            # Aqui chamamos a tela de ranking
            tela_nivel3.destroy()
            import ranking  # Importa a tela de ranking
            ranking.exibir_ranking()  # Chama a função para exibir o ranking
        else:
            messagebox.showwarning("Nível 3 Concluído", "Nome não registrado no ranking.")
            tela_nivel3.destroy()  # Fechar a tela do nível mesmo que não tenha registrado o nome

    tela_nivel3.mainloop()

if __name__ == "__main__":
    iniciar_nivel3()
