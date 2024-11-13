import tkinter as tk
import json

def iniciar_ranking(nome_usuario):
    tela_ranking = tk.Tk()
    tela_ranking.title("The Writing Board - Ranking")
    tela_ranking.geometry("500x500")
    tela_ranking.configure(bg="#2d3e50")  # Fundo da tela em azul escuro

    # Carregar as pontuações do arquivo JSON
    try:
        with open("pontuacoes.json", "r") as arquivo:
            pontuacoes = json.load(arquivo)
    except FileNotFoundError:
        pontuacoes = {}

    # Texto informativo com o nome do usuário logado
    texto_informativo = tk.Label(
        tela_ranking,
        text=f"Aqui, {nome_usuario}, ficarão suas últimas pontuações das tentativas de níveis.",
        font=("Arial", 12),
        bg="#2d3e50",
        fg="#fbd11b",
        wraplength=450,
        justify="center"
    )
    texto_informativo.pack(pady=20)

    # Criar uma string para exibir as pontuações de forma limpa
    pontuacoes_texto = "Pontuações:\n"
    if pontuacoes:
        for nivel, pontos_lista in pontuacoes.items():
            for item in pontos_lista:
                usuario = item["usuario"]
                pontos = item["pontuacao"]
                pontuacoes_texto += f"{nivel.capitalize()}: {usuario} - {pontos} pontos\n"
    else:
        pontuacoes_texto += "Nenhuma pontuação registrada.\n"

    # Exibir as pontuações na tela de forma limpa
    label_pontuacoes = tk.Label(
        tela_ranking,
        text=pontuacoes_texto,
        font=("Arial", 12),
        bg="#2d3e50",
        fg="white",
        justify="left"
    )
    label_pontuacoes.pack(pady=20)

    # Função para voltar à tela de módulos
    def voltar_modulos():
        tela_ranking.quit()  # Em vez de destruir, usamos quit() para encerrar o loop da tela de ranking
        tela_ranking.destroy()  # E agora, podemos destruir a tela de ranking para liberar recursos
        import modulos  # Redireciona para a tela de módulos
        modulos.iniciar_modulos()  # Chama a função de modulos.py para abrir a tela de módulos

    # Botão "Voltar" para retornar à tela de módulos
    botao_voltar = tk.Button(
        tela_ranking,
        text="Voltar",
        command=voltar_modulos,
        font=("Arial", 10, "bold"),
        bg="#fbd11b",
        fg="#2d3e50",
        activebackground="#fbd11b",
        activeforeground="#2d3e50",
        relief="raised",
        cursor="hand2",
        padx=10,
        pady=5
    )
    botao_voltar.pack(side=tk.BOTTOM, pady=20)

    tela_ranking.mainloop()

if __name__ == "__main__":
    iniciar_ranking("Usuário Exemplo")
