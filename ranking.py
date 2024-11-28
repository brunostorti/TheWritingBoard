import tkinter as tk
from pymongo import MongoClient

# Conectar ao MongoDB
client = MongoClient('mongodb+srv://joaoalvarez:PjOwQniGDQGSJzvo@cluster0.tguge.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['Projeto_PI']
pontuacoes_collection = db['pontuacoes']

# Função para salvar a pontuação na coleção "pontuacoes"
def salvar_pontuacao(nivel, pontuacao, usuario):
    dados = {
        "nivel": nivel,
        "usuario": usuario,
        "pontuacao": pontuacao
    }
    pontuacoes_collection.insert_one(dados)

# Função para buscar e exibir o ranking
def iniciar_ranking(nome_usuario):
    tela_ranking = tk.Tk()
    tela_ranking.title("The Writing Board - Ranking")
    tela_ranking.geometry("500x500")
    tela_ranking.configure(bg="#2d3e50")

    # Buscar pontuações por nível no MongoDB
    nivel1_pontuacoes = pontuacoes_collection.find({"nivel": "nivel1"}).sort("pontuacao", -1).limit(10)
    nivel2_pontuacoes = pontuacoes_collection.find({"nivel": "nivel2"}).sort("pontuacao", -1).limit(10)
    nivel3_pontuacoes = pontuacoes_collection.find({"nivel": "nivel3"}).sort("pontuacao", -1).limit(10)

    # Texto informativo com o nome do usuário logado
    texto_informativo = tk.Label(
        tela_ranking,
        text=f"Aqui, {nome_usuario}, ficam suas últimas pontuações nos níveis.",
        font=("Arial", 12),
        bg="#2d3e50",
        fg="#fbd11b",
        wraplength=450,
        justify="center"
    )
    texto_informativo.pack(pady=20)

    # Função para formatar o ranking de um nível
    def formatar_ranking(nivel, pontuacoes):
        ranking_texto = f"Ranking Nível {nivel.capitalize()}:\n"
        if pontuacoes:
            for i, entry in enumerate(pontuacoes, start=1):
                ranking_texto += f"{i}. {entry['usuario']} - {entry['pontuacao']} pontos\n"
        else:
            ranking_texto += "Nenhuma pontuação registrada.\n"
        return ranking_texto

    # Exibir as pontuações na tela de forma limpa
    ranking_nivel1 = formatar_ranking("1", nivel1_pontuacoes)
    ranking_nivel2 = formatar_ranking("2", nivel2_pontuacoes)
    ranking_nivel3 = formatar_ranking("3", nivel3_pontuacoes)

    label_pontuacoes = tk.Label(
        tela_ranking,
        text=ranking_nivel1 + "\n" + ranking_nivel2 + "\n" + ranking_nivel3,
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

# Exemplo de como iniciar o ranking com um nome de usuário
if __name__ == "__main__":
    iniciar_ranking("Usuário Exemplo")