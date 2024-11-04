import tkinter as tk
from tkinter import messagebox
import json

# Configuração inicial da pontuação e lista de perguntas do Nível 3
pontos = 0
questions_nivel3 = [
    {
        "question": "Qual é o papel do repertório sociocultural em uma redação argumentativa?",
        "options": ["1. Distrair o leitor", "2. Enriquecer a argumentação", "3. Fornecer conclusões", "4. Descrever o tema"],
        "answer": 2
    },
    {
        "question": "O que é uma citação direta?",
        "options": ["1. Uma ideia própria do autor", "2. Uma reprodução exata das palavras de outra pessoa", "3. Uma paráfrase", "4. Um resumo"],
        "answer": 2
    },
    {
        "question": "Por que é importante ter clareza na escrita?",
        "options": ["1. Para aumentar o número de palavras", "2. Para garantir que o leitor compreenda a mensagem", "3. Para impressionar o leitor", "4. Para confundir o leitor"],
        "answer": 2
    },
    {
        "question": "Qual é a função da tese em uma redação?",
        "options": ["1. Introduzir novos argumentos", "2. Defender a posição do autor", "3. Fazer perguntas", "4. Concluir o texto"],
        "answer": 2
    },
    {
        "question": "Como o uso de dados estatísticos pode fortalecer um argumento?",
        "options": ["1. Tornando o texto mais longo", "2. Fornecendo embasamento factual", "3. Distraindo o leitor", "4. Confundindo o leitor"],
        "answer": 2
    },
    {
        "question": "O que significa a palavra 'concisão' em uma redação?",
        "options": ["1. Uso excessivo de palavras", "2. Objetividade e clareza", "3. Uso de termos complexos", "4. Extensão desnecessária"],
        "answer": 2
    },
    {
        "question": "Em qual parte da redação é ideal introduzir o contra-argumento?",
        "options": ["1. Introdução", "2. Desenvolvimento", "3. Conclusão", "4. Título"],
        "answer": 2
    },
    {
        "question": "Por que o uso de conectivos é importante em uma argumentação?",
        "options": ["1. Para organizar e encadear ideias", "2. Para deixar o texto confuso", "3. Para alongar o texto", "4. Para omitir argumentos"],
        "answer": 1
    },
    {
        "question": "Qual o papel da linguagem formal em uma redação argumentativa?",
        "options": ["1. Dar credibilidade ao texto", "2. Tornar o texto mais leve", "3. Encurtar a redação", "4. Aumentar a dificuldade de compreensão"],
        "answer": 1
    },
    {
        "question": "Como uma boa conclusão impacta o leitor?",
        "options": ["1. Reafirma a posição do autor", "2. Adiciona novas ideias", "3. Introduz novos argumentos", "4. Diminui o impacto do texto"],
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

# Função para iniciar o Nível 3
def iniciar_nivel3():
    global pontos
    pontos = 0  # Resetar pontos no início do nível

    # Configuração da janela
    tela_nivel3 = tk.Tk()
    tela_nivel3.title("Nível 3 - Argumentação Avançada")
    tela_nivel3.geometry("500x500")

    # Exibir visor de pontos
    score_label = tk.Label(tela_nivel3, text=f"Pontos: {pontos}", font=("Arial", 16))
    score_label.pack(pady=10)

    # Variável para controlar a pergunta atual
    pergunta_atual = 0

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
            pontos += 30  # Acrescentar 30 pontos para resposta correta
            score_label.config(text=f"Pontos: {pontos}")  # Atualiza o visor de pontos

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
    start_button = tk.Button(tela_nivel3, text="Iniciar Perguntas do Nível 3", command=show_question)
    start_button.pack(pady=20)

    # Botão "Voltar" para retornar ao módulo
    def voltar_modulos():
        tela_nivel3.destroy()
        import modulos
        modulos.iniciar_modulos()

    botao_voltar = tk.Button(tela_nivel3, text="Voltar", command=voltar_modulos)
    botao_voltar.pack(side=tk.BOTTOM, pady=20)

    def finalizar_nivel():
        messagebox.showinfo("Nível 3 Concluído", f"Você finalizou o Nível 3 com {pontos} pontos!")
        atualizar_ranking(pontos)  # Atualizar ranking com a pontuação final
        tela_nivel3.destroy()

    tela_nivel3.mainloop()

if __name__ == "__main__":
    iniciar_nivel3()
