import tkinter as tk
from tkinter import messagebox, simpledialog
import json

# Configuração inicial da pontuação e lista de perguntas do Nível 2
pontos = 0
questions_nivel2 = [
    {
        "question": "O que é repertório sociocultural em um texto dissertativo?",
        "options": ["1. Uma opinião pessoal", "2. Informações sem fontes", "3. Argumento baseado em dados", "4. Ideia fora do contexto"],
        "answer": 3
    },
    {
        "question": "Como o repertório pode fortalecer a argumentação?",
        "options": ["1. Desviando o tema", "2. Aumentando a empatia", "3. Conectando com dados confiáveis", "4. Contrariando a tese"],
        "answer": 3
    },
    {
        "question": "Qual das opções a seguir é uma fonte de repertório sociocultural?",
        "options": ["1. Uma pesquisa científica", "2. Um boato", "3. Um meme", "4. Uma opinião sem fonte"],
        "answer": 1
    },
    {
        "question": "Como o repertório pode contribuir para a construção da proposta de intervenção?",
        "options": ["1. Introduzindo uma nova tese", "2. Validando soluções", "3. Desviando o foco", "4. Confundindo o leitor"],
        "answer": 2
    },
    {
        "question": "Citar uma lei em um texto dissertativo é um exemplo de:",
        "options": ["1. Opinião pessoal", "2. Repertório sociocultural", "3. Introdução", "4. Conclusão"],
        "answer": 2
    },
    {
        "question": "Qual dessas afirmações é um exemplo de repertório sociocultural adequado?",
        "options": ["1. Ouvi dizer que é assim", "2. Estatísticas do IBGE", "3. Algo que todos sabem", "4. Opinião do autor"],
        "answer": 2
    },
    {
        "question": "Qual das alternativas é considerada uma evidência confiável em uma dissertação?",
        "options": ["1. Fatos históricos", "2. Rumores", "3. Suposições", "4. Experiência pessoal"],
        "answer": 1
    },
    {
        "question": "O que NÃO é um exemplo de repertório sociocultural?",
        "options": ["1. Referência à Constituição", "2. Pesquisa de uma universidade", "3. Opinião pessoal", "4. Dado do IBGE"],
        "answer": 3
    },
    {
        "question": "Ao usar uma citação, o autor está empregando qual recurso argumentativo?",
        "options": ["1. Argumento de autoridade", "2. Contra-argumento", "3. Exemplo pessoal", "4. Opinião"],
        "answer": 1
    },
    {
        "question": "Qual das alternativas abaixo é uma boa prática ao usar repertório sociocultural?",
        "options": ["1. Inventar dados", "2. Usar fontes confiáveis", "3. Evitar referências", "4. Usar apenas a opinião"],
        "answer": 2
    },
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

# Função para iniciar o Nível 2
def iniciar_nivel2():
    global pontos
    pontos = 0  # Resetar pontos no início do nível

    # Configuração da janela
    tela_nivel2 = tk.Tk()
    tela_nivel2.title("Nível 2 - Repertório Sociocultural")
    tela_nivel2.geometry("500x500")

    # Exibir visor de pontos
    score_label = tk.Label(tela_nivel2, text=f"Pontos: {pontos}", font=("Arial", 16))
    score_label.pack(pady=10)

    # Variável para controlar a pergunta atual
    pergunta_atual = 0

    # Função para atualizar o visor de pontos
    def update_score():
        score_label.config(text=f"Pontos: {pontos}")

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
            update_score()  # Atualiza o visor de pontos

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
    start_button = tk.Button(tela_nivel2, text="Iniciar Perguntas do Nível 2", command=lambda: [show_question(), start_button.config(state="disabled")])
    start_button.pack(pady=20)

    # Botão "Voltar" para retornar ao módulo
    def voltar_modulos():
        tela_nivel2.destroy()
        import modulos
        modulos.iniciar_modulos()

    botao_voltar = tk.Button(tela_nivel2, text="Voltar", command=voltar_modulos)
    botao_voltar.pack(side=tk.BOTTOM, pady=20)

    def finalizar_nivel():
        global pontos
        nome_jogador = simpledialog.askstring("Registro no Ranking", "Digite seu nome para registrar no ranking:")
        if nome_jogador:
            messagebox.showinfo("Nível 2 Concluído", f"Você finalizou o Nível 2 com {pontos} pontos!")
            atualizar_ranking(nome_jogador, pontos)  # Atualizar ranking com a pontuação final

            # Aqui chamamos a tela de ranking
            tela_nivel2.destroy()
            import ranking  # Importa a tela de ranking
            ranking.exibir_ranking()  # Chama a função para exibir o ranking
        else:
            messagebox.showwarning("Nível 2 Concluído", "Nome não registrado no ranking.")
            tela_nivel2.destroy()  # Fechar a tela do nível mesmo que não tenha registrado o nome

    tela_nivel2.mainloop()

if __name__ == "__main__":
    iniciar_nivel2()
