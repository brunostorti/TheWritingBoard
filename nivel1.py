import tkinter as tk
from tkinter import messagebox, simpledialog
import json

# Configuração inicial da pontuação e lista de perguntas
pontos = 0
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
    {
        "question": "O que deve ser feito no parágrafo de desenvolvimento?",
        "options": ["1. Apresentar ideias novas", "2. Reafirmar a introdução", "3. Desenvolver e argumentar a tese", "4. Concluir o texto"],
        "answer": 3
    },
    {
        "question": "Qual a função principal de um texto dissertativo?",
        "options": ["1. Narrar uma história", "2. Expressar sentimentos", "3. Argumentar sobre um tema", "4. Divertir o leitor"],
        "answer": 3
    },
    {
        "question": "O que deve ser evitado em um texto dissertativo-argumentativo?",
        "options": ["1. Argumentos baseados em dados", "2. Opiniões pessoais sem embasamento", "3. Estrutura clara e organizada", "4. Exemplos reais"],
        "answer": 2
    },
    {
        "question": "Qual é a característica de uma boa conclusão?",
        "options": ["1. Repetir a tese exatamente igual", "2. Trazer novos argumentos", "3. Síntese das ideias e solução para o problema", "4. Criticar o tema"],
        "answer": 3
    },
    {
        "question": "Como os argumentos devem ser apresentados?",
        "options": ["1. Em uma sequência lógica e estruturada", "2. De forma aleatória", "3. Somente no parágrafo de conclusão", "4. Em tópicos separados"],
        "answer": 1
    },
    {
        "question": "Em um texto dissertativo-argumentativo, a estrutura básica é formada por:",
        "options": ["1. Introdução, meio e fim", "2. Tese, desenvolvimento e conclusão", "3. Título e parágrafos", "4. Desenvolvimento e finalização"],
        "answer": 2
    },
    {
        "question": "Qual das alternativas é mais adequada para iniciar um parágrafo de desenvolvimento?",
        "options": ["1. Primeiramente", "2. Em conclusão", "3. Em contrapartida", "4. No entanto"],
        "answer": 1
    },
    {
        "question": "Qual o objetivo da tese na introdução?",
        "options": ["1. Explicar todos os detalhes do tema", "2. Posicionar a opinião do autor sobre o tema", "3. Descrever um exemplo prático", "4. Concluir o texto"],
        "answer": 2
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

# Função para iniciar o Nível 1
def iniciar_nivel1():
    global pontos
    pontos = 0  # Resetar pontos no início do nível

    # Configuração da janela
    tela_nivel1 = tk.Tk()
    tela_nivel1.title("Nível 1 - Noções de Estrutura Textual")
    tela_nivel1.geometry("500x500")

    # Exibir visor de pontos
    score_label = tk.Label(tela_nivel1, text=f"Pontos: {pontos}", font=("Arial", 16))
    score_label.pack(pady=10)

    # Variável para controlar a pergunta atual
    pergunta_atual = 0

    # Função para atualizar o visor de pontos
    def update_score():
        score_label.config(text=f"Pontos: {pontos}")

    # Função para mostrar a próxima pergunta
    def show_question():
        nonlocal pergunta_atual
        if pergunta_atual < len(questions_nivel1):
            question = questions_nivel1[pergunta_atual]
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
            pontos += 5  # Acrescentar pontos para resposta correta
            update_score()  # Atualiza o visor de pontos

        pergunta_atual += 1
        show_question()  # Avança para a próxima pergunta diretamente

    # Layout da pergunta
    question_label = tk.Label(tela_nivel1, text="", wraplength=400, font=("Arial", 12))
    question_label.pack(pady=20)

    # Botões para opções
    option_buttons = [tk.Button(tela_nivel1, text="", font=("Arial", 12)) for _ in range(4)]
    for btn in option_buttons:
        btn.pack(pady=5)

    # Botão para iniciar perguntas do Nível 1
    start_button = tk.Button(tela_nivel1, text="Iniciar Perguntas do Nível 1", command=lambda: [show_question(), start_button.config(state="disabled")])
    start_button.pack(pady=20)

    # Botão "Voltar" para retornar ao módulo
    def voltar_modulos():
        tela_nivel1.destroy()
        import modulos
        modulos.iniciar_modulos()

    botao_voltar = tk.Button(tela_nivel1, text="Voltar", command=voltar_modulos)
    botao_voltar.pack(side=tk.BOTTOM, pady=20)

    def finalizar_nivel():
        global pontos
        nome_jogador = simpledialog.askstring("Registro no Ranking", "Digite seu nome para registrar no ranking:")
        if nome_jogador:
            messagebox.showinfo("Nível 1 Concluído", f"Você finalizou o Nível 1 com {pontos} pontos!")
            atualizar_ranking(nome_jogador, pontos)  # Atualizar ranking com a pontuação final

            # Aqui chamamos a tela de ranking
            tela_nivel1.destroy()
            import ranking  # Importa a tela de ranking
            ranking.exibir_ranking()  # Chama a função para exibir o ranking
        else:
            messagebox.showwarning("Nível 1 Concluído", "Nome não registrado no ranking.")
            tela_nivel1.destroy()  # Fechar a tela do nível mesmo que não tenha registrado o nome

    tela_nivel1.mainloop()

if __name__ == "__main__":
    iniciar_nivel1()
