import tkinter as tk
from tkinter import messagebox
import json

# Configuração inicial da pontuação e lista de perguntas do Nível 2
pontos = 0
questions_nivel2 = [
    {
        "question": "Qual é o objetivo de um texto argumentativo?",
        "options": ["1. Informar o leitor", "2. Convencer o leitor", "3. Entreter o leitor", "4. Descrever uma situação"],
        "answer": 2
    },
    {
        "question": "O que deve ser considerado ao escrever uma conclusão?",
        "options": ["1. Introduzir novas ideias", "2. Repetir argumentos", "3. Reforçar a tese", "4. Fazer uma pergunta"],
        "answer": 3
    },
    {
        "question": "Qual é a função de um exemplo em um texto argumentativo?",
        "options": ["1. Distrair o leitor", "2. Ilustrar e apoiar a tese", "3. Aumentar a confusão", "4. Fazer piadas"],
        "answer": 2
    },
    {
        "question": "O que é um contra-argumento?",
        "options": ["1. Um argumento que apoia a tese", "2. Um argumento contrário à tese", "3. Uma pergunta retórica", "4. Um exemplo"],
        "answer": 2
    },
    {
        "question": "Por que é importante usar conectivos em um texto?",
        "options": ["1. Para deixar o texto mais confuso", "2. Para ligar ideias e facilitar a leitura", "3. Para aumentar o número de palavras", "4. Para escrever mais rápido"],
        "answer": 2
    },
    {
        "question": "Qual é a estrutura básica de um texto argumentativo?",
        "options": ["1. Introdução, desenvolvimento, conclusão", "2. Apenas conclusão", "3. Tese, antítese, síntese", "4. Parágrafo único"],
        "answer": 1
    },
    {
        "question": "O que caracteriza uma boa argumentação?",
        "options": ["1. Clareza e coerência", "2. Complicação", "3. Uso excessivo de jargões", "4. Subjetividade"],
        "answer": 1
    },
    {
        "question": "Qual a importância da pesquisa ao escrever um texto argumentativo?",
        "options": ["1. Não é importante", "2. Fornece embasamento para os argumentos", "3. Para encher o texto", "4. Para complicar o texto"],
        "answer": 2
    },
    {
        "question": "O que é uma tese?",
        "options": ["1. A ideia central do texto", "2. Um argumento", "3. Um exemplo", "4. Uma conclusão"],
        "answer": 1
    },
    {
        "question": "Qual é a importância da revisão do texto?",
        "options": ["1. Para corrigir erros", "2. Para aumentar o número de palavras", "3. Para desorganizar o texto", "4. Para diminuir a qualidade"],
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

# Função para iniciar o Nível 2
def iniciar_nivel2():
    global pontos
    pontos = 0  # Resetar pontos no início do nível

    # Configuração da janela
    tela_nivel2 = tk.Tk()
    tela_nivel2.title("Nível 2 - Repertório")
    tela_nivel2.geometry("500x500")

    # Exibir visor de pontos
    score_label = tk.Label(tela_nivel2, text=f"Pontos: {pontos}", font=("Arial", 16))
    score_label.pack(pady=10)

    # Variável para controlar a pergunta atual
    pergunta_atual = 0

    # Função para mostrar a próxima pergunta
    def show_question():
        nonlocal pergunta_atual
        if pergunta_atual < len(questions_nivel2):
            question = questions_nivel2[pergunta_atual]
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
            pontos += 10  # Acrescentar 10 pontos para resposta correta
            score_label.config(text=f"Pontos: {pontos}")  # Atualiza o visor de pontos

        pergunta_atual += 1
        show_question()  # Avança para a próxima pergunta diretamente

    # Layout da pergunta
    question_label = tk.Label(tela_nivel2, text="", wraplength=400, font=("Arial", 12))
    question_label.pack(pady=20)

    # Botões para opções
    option_buttons = [tk.Button(tela_nivel2, text="", font=("Arial", 12)) for _ in range(4)]
    for btn in option_buttons:
        btn.pack(pady=5)

    # Botão para iniciar perguntas do Nível 2
    start_button = tk.Button(tela_nivel2, text="Iniciar Perguntas do Nível 2", command=show_question)
    start_button.pack(pady=20)

    # Botão "Voltar" para retornar ao módulo
    def voltar_modulos():
        tela_nivel2.destroy()
        import modulos
        modulos.iniciar_modulos()

    botao_voltar = tk.Button(tela_nivel2, text="Voltar", command=voltar_modulos)
    botao_voltar.pack(side=tk.BOTTOM, pady=20)

    def finalizar_nivel():
        messagebox.showinfo("Nível 2 Concluído", f"Você finalizou o Nível 2 com {pontos} pontos!")
        atualizar_ranking(pontos)  # Atualizar ranking com a pontuação final
        tela_nivel2.destroy()

    tela_nivel2.mainloop()

if __name__ == "__main__":
    iniciar_nivel2()
