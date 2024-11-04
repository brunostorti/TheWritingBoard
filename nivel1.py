import tkinter as tk
from tkinter import messagebox
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
        "question": "Qual é a estrutura básica de um texto dissertativo?",
        "options": ["1. Introdução, desenvolvimento, conclusão", "2. Introdução, resumo, conclusão", "3. Tese, antítese, síntese", "4. Parágrafo, frase, palavra"],
        "answer": 1
    },
    {
        "question": "O que é um argumento em um texto dissertativo?",
        "options": ["1. Uma opinião sem provas", "2. Uma evidência que sustenta a tese", "3. Uma citação famosa", "4. Uma crítica à tese"],
        "answer": 2
    },
    {
        "question": "O que deve conter no parágrafo de conclusão?",
        "options": ["1. Novos argumentos", "2. Citações", "3. Síntese da discussão", "4. Introdução de ideias"],
        "answer": 3
    },
    {
        "question": "Qual é a função do desenvolvimento em um texto dissertativo?",
        "options": ["1. Apresentar a tese", "2. Fundamentar a tese com argumentos", "3. Concluir o texto", "4. Introduzir o tema"],
        "answer": 2
    },
    {
        "question": "O que caracteriza um bom argumento?",
        "options": ["1. Opinião pessoal", "2. Informação irrelevante", "3. Dados e exemplos concretos", "4. Palavras complexas"],
        "answer": 3
    },
    {
        "question": "Qual recurso pode reforçar um argumento em um texto?",
        "options": ["1. Dados estatísticos", "2. Um resumo", "3. Uma pergunta retórica", "4. Uma palavra de transição"],
        "answer": 1
    }
]

# Função para atualizar o ranking
def atualizar_ranking(pontos):
    try:
        with open('ranking.json', 'r') as file:
            ranking = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        ranking = []

    nome_jogador = input("Digite seu nome para registrar no ranking: ")
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
            score_label.config(text=f"Pontos: {pontos}")  # Atualiza o visor de pontos

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
    start_button = tk.Button(tela_nivel1, text="Iniciar Perguntas do Nível 1", command=show_question)
    start_button.pack(pady=20)

    # Botão "Voltar" para retornar ao módulo
    def voltar_modulos():
        tela_nivel1.destroy()
        import modulos
        modulos.iniciar_modulos()

    botao_voltar = tk.Button(tela_nivel1, text="Voltar", command=voltar_modulos)
    botao_voltar.pack(side=tk.BOTTOM, pady=20)

    def finalizar_nivel():
        messagebox.showinfo("Nível 1 Concluído", f"Você finalizou o Nível 1 com {pontos} pontos!")
        atualizar_ranking(pontos)  # Atualizar ranking com a pontuação final
        tela_nivel1.destroy()

    tela_nivel1.mainloop()

if __name__ == "__main__":
    iniciar_nivel1()
