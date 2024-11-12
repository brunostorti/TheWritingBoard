import tkinter as tk
from tkinter import messagebox, simpledialog
import json

# Configuração inicial da pontuação e lista de perguntas para o Nível 3
pontos = 0
questions_nivel3 = [
    {
        "question": "O que é uma tese em um texto dissertativo?",
        "options": ["1. Um exemplo", "2. Uma citação", "3. A principal ideia do autor", "4. Um argumento secundário"],
        "answer": 3
    },
    # Adicione as demais perguntas específicas do nível 3 aqui
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

# Função para iniciar o Nível 3
def iniciar_nivel3():
    global pontos
    pontos = 0  # Resetar pontos no início do nível

    # Configuração da janela
    tela_nivel3 = tk.Tk()
    tela_nivel3.title("Nível 3 - Noções Avançadas de Estrutura Textual")
    tela_nivel3.geometry("600x600")
    tela_nivel3.configure(bg="#2d3e50")  # Cor de fundo azul-escuro

    # Tela de introdução
    introducao_frame = tk.Frame(tela_nivel3, bg="#2d3e50")
    introducao_frame.pack(fill="both", expand=True)

    introducao_label = tk.Label(
        introducao_frame,
        text="Bem-vindo ao Nível 3: Noções Avançadas de Estrutura Textual!\n\nVocê responderá perguntas mais desafiadoras sobre estrutura de textos dissertativos.\nA cada resposta correta, você ganhará 30 pontos!\n\nBoa sorte!",
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
        text="Iniciar Nível 3",
        command=iniciar_jogo,
        font=("Arial", 12, "bold"),
        bg="#f9d342",
        fg="#2d3e50",
        cursor="hand2",
        relief="groove"
    )
    start_button.pack(pady=20)

    # Frame para o jogo (perguntas)
    jogo_frame = tk.Frame(tela_nivel3, bg="#2d3e50")

    # Exibir visor de pontos com design aprimorado
    score_label = tk.Label(jogo_frame, text=f"Pontos: {pontos}", font=("Arial", 16, "bold"), bg="#2d3e50", fg="#f9d342")
    score_label.pack(pady=10)

    pergunta_atual = 0

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
            pontos += 30
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
        tela_nivel3.destroy()
        import modulos
        modulos.iniciar_modulos()

    botao_voltar = tk.Button(jogo_frame, text="Voltar", command=voltar_modulos, font=("Arial", 12, "bold"), bg="#f9d342", fg="#2d3e50", relief="flat", cursor="hand2")
    botao_voltar.pack(side=tk.BOTTOM, pady=20)

    # Função para finalizar o nível
    def finalizar_nivel():
        global pontos
        nome_jogador = simpledialog.askstring("Registro no Ranking", "Digite seu nome para registrar no ranking:")
        if nome_jogador:
            messagebox.showinfo("Nível 3 Concluído", f"Você finalizou o Nível 3 com {pontos} pontos!")
            atualizar_ranking(nome_jogador, pontos)

    tela_nivel3.mainloop()

# Chamada para iniciar o nível 3
iniciar_nivel3()
