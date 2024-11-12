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
        "question": "Qual a função dos argumentos em um texto dissertativo?",
        "options": ["1. Apresentar dados", "2. Defender a tese", "3. Fornecer exemplos", "4. Contradizer a tese"],
        "answer": 2
    },
    {
        "question": "Qual é o objetivo da conclusão de um texto dissertativo?",
        "options": ["1. Introduzir novas ideias", "2. Resumir os argumentos", "3. Criticar a tese", "4. Apresentar a tese"],
        "answer": 2
    },
    {
        "question": "O que caracteriza uma introdução eficiente?",
        "options": ["1. Ser longa", "2. Ser vaga", "3. Contextualizar a tese", "4. Repetir a conclusão"],
        "answer": 3
    },
    {
        "question": "Como um argumento deve ser estruturado?",
        "options": ["1. Baseado em opinião", "2. Sem dados", "3. De forma lógica e fundamentada", "4. Sem relação com a tese"],
        "answer": 3
    },
    {
        "question": "O que significa ser objetivo em um texto?",
        "options": ["1. Usar opiniões pessoais", "2. Usar dados e fatos", "3. Fazer perguntas", "4. Usar linguagem poética"],
        "answer": 2
    },
    {
        "question": "Qual o papel dos conectivos em um texto?",
        "options": ["1. Separar ideias", "2. Conectar parágrafos", "3. Dar opinião", "4. Enfeitar o texto"],
        "answer": 2
    },
    {
        "question": "Como um texto deve ser concluído?",
        "options": ["1. Apresentando novas ideias", "2. Resumindo e reforçando a tese", "3. Com perguntas", "4. Com citações"],
        "answer": 2
    },
    {
        "question": "Qual é a importância de um bom vocabulário?",
        "options": ["1. Enfeitar o texto", "2. Tornar a leitura complexa", "3. Comunicar de forma clara", "4. Apresentar opiniões"],
        "answer": 3
    },
    # Adicione outras perguntas aqui, mantendo o formato e sem repetir nenhuma
]


# Função para atualizar o ranking
def atualizar_ranking(nome_jogador, pontos):
    try:
        with open('ranking.json', 'r') as file:
            ranking = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        ranking = []


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
    tela_nivel1.geometry("600x600")
    tela_nivel1.configure(bg="#2d3e50")  # Cor de fundo azul-escuro


    # Tela de introdução
    introducao_frame = tk.Frame(tela_nivel1, bg="#2d3e50")
    introducao_frame.pack(fill="both", expand=True)


    introducao_label = tk.Label(
        introducao_frame,
        text="Bem-vindo ao Nível 1: Noções de Estrutura Textual!\n\nVocê responderá perguntas sobre estrutura de textos dissertativos.\nA cada resposta correta, você ganhará pontos!\n\nBoa sorte!",
        font=("Arial", 14),
        bg="#2d3e50",
        fg="#f9d342",
        wraplength=500,
        justify="center"
    )
    introducao_label.pack(pady=40)


    # Botão para começar o nível após a introdução
    def iniciar_jogo():
        introducao_frame.pack_forget()  # Esconde o frame de introdução
        jogo_frame.pack(fill="both", expand=True)  # Mostra o frame de perguntas
        show_question()


    start_button = tk.Button(
        introducao_frame,
        text="Iniciar Nível 1",
        command=iniciar_jogo,
        font=("Arial", 12, "bold"),
        bg="#f9d342",
        fg="#2d3e50",
        cursor="hand2",
        relief="groove"
    )
    start_button.pack(pady=20)


    # Frame para o jogo (perguntas)
    jogo_frame = tk.Frame(tela_nivel1, bg="#2d3e50")


    # Exibir visor de pontos com design aprimorado
    score_label = tk.Label(jogo_frame, text=f"Pontos: {pontos}", font=("Arial", 16, "bold"), bg="#2d3e50", fg="#f9d342")
    score_label.pack(pady=10)


    pergunta_atual = 0


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


            # Atualizar as opções em 2x2
            for i, option in enumerate(options):
                option_buttons[i].config(text=option, command=lambda ans=i+1: check_answer(ans, answer))
        else:
            finalizar_nivel()


    # Verificar resposta e atualizar pontuação
    def check_answer(selected_answer, correct_answer):
        nonlocal pergunta_atual
        global pontos
        if selected_answer == correct_answer:
            pontos += 5
            update_score()
        pergunta_atual += 1
        show_question()


    # Layout da pergunta
    question_label = tk.Label(jogo_frame, text="", wraplength=500, font=("Arial", 14, "bold"), bg="#2d3e50", fg="#f9d342")
    question_label.pack(pady=20)


    # Frame para botões de opções com layout 2x2
    options_frame = tk.Frame(jogo_frame, bg="#2d3e50")
    options_frame.pack(pady=20)


    # Botões para opções com design aprimorado
    option_buttons = []
    for i in range(4):
        btn = tk.Button(options_frame, text="", font=("Arial", 12), width=20, height=2, bg="#5c80bc", fg="white", relief="raised", activebackground="#4a6fa5", cursor="hand2")
        option_buttons.append(btn)


    # Organizando botões em 2x2
    option_buttons[0].grid(row=0, column=0, padx=10, pady=5)
    option_buttons[1].grid(row=0, column=1, padx=10, pady=5)
    option_buttons[2].grid(row=1, column=0, padx=10, pady=5)
    option_buttons[3].grid(row=1, column=1, padx=10, pady=5)


    # Botão "Voltar" para retornar ao módulo
    def voltar_modulos():
        tela_nivel1.destroy()
        import modulos
        modulos.iniciar_modulos()


    botao_voltar = tk.Button(jogo_frame, text="Voltar", command=voltar_modulos, font=("Arial", 12, "bold"), bg="#f9d342", fg="#2d3e50", relief="flat", cursor="hand2")
    botao_voltar.pack(side=tk.BOTTOM, pady=20)


    # Função para finalizar o nível
    def finalizar_nivel():
        global pontos
        nome_jogador = simpledialog.askstring("Registro no Ranking", "Digite seu nome para registrar no ranking:")
        if nome_jogador:
            messagebox.showinfo("Nível 1 Concluído", f"Você finalizou o Nível 1 com {pontos} pontos!")
            atualizar_ranking(nome_jogador, pontos)


            tela_nivel1.destroy()
            import ranking
            ranking
