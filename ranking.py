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
    tela_ranking.configure(bg="#2d3e50")

    # Ativar tela cheia
    tela_ranking.attributes("-fullscreen", True)

    # Texto informativo com o nome do usuário logado
    texto_informativo = tk.Label(
        tela_ranking,
        text=f"Aqui, {nome_usuario}, ficam suas últimas pontuações nos níveis.",
        font=("Arial", 16, "bold"),
        bg="#2d3e50",
        fg="#fbd11b",
        wraplength=800,
        justify="center"
    )
    texto_informativo.pack(pady=20)

    # Frame para organizar rankings em colunas
    frame_ranking = tk.Frame(tela_ranking, bg="#2d3e50")
    frame_ranking.pack(pady=20, fill=tk.BOTH, expand=True)

    # Função para formatar e exibir ranking de um nível
    def criar_coluna_ranking(parent, titulo, pontuacoes):
        frame_coluna = tk.Frame(parent, bg="#34495e", padx=10, pady=10)
        frame_coluna.pack(side=tk.LEFT, padx=20, pady=10, fill=tk.BOTH, expand=True)

        label_titulo = tk.Label(
            frame_coluna,
            text=titulo,
            font=("Arial", 18, "bold"),
            bg="#34495e",
            fg="#fbd11b"
        )
        label_titulo.pack(pady=10)

        texto_ranking = ""
        if pontuacoes:
            for i, entry in enumerate(pontuacoes, start=1):
                texto_ranking += f"{i}. {entry['usuario']} - {entry['pontuacao']} pontos\n"
        else:
            texto_ranking = "Nenhuma pontuação registrada.\n"

        label_pontuacoes = tk.Label(
            frame_coluna,
            text=texto_ranking,
            font=("Arial", 14),
            bg="#34495e",
            fg="white",
            justify="left"
        )
        label_pontuacoes.pack(pady=10)

    # Buscar pontuações por nível no MongoDB
    nivel1_pontuacoes = pontuacoes_collection.find({"nivel": "nivel1"}).sort("pontuacao", -1).limit(10)
    nivel2_pontuacoes = pontuacoes_collection.find({"nivel": "nivel2"}).sort("pontuacao", -1).limit(10)
    nivel3_pontuacoes = pontuacoes_collection.find({"nivel": "nivel3"}).sort("pontuacao", -1).limit(10)

    # Criar colunas para cada nível
    criar_coluna_ranking(frame_ranking, "Ranking Nível 1", nivel1_pontuacoes)
    criar_coluna_ranking(frame_ranking, "Ranking Nível 2", nivel2_pontuacoes)
    criar_coluna_ranking(frame_ranking, "Ranking Nível 3", nivel3_pontuacoes)

    # Função para voltar à tela de módulos
    def voltar_modulos():
        tela_ranking.quit()
        tela_ranking.destroy()
        import modulos
        modulos.iniciar_modulos()

    # Botão "Voltar" para retornar à tela de módulos
    botao_voltar = tk.Button(
        tela_ranking,
        text="Voltar",
        command=voltar_modulos,
        font=("Arial", 14, "bold"),
        bg="#fbd11b",
        fg="#2d3e50",
        activebackground="#fbd11b",
        activeforeground="#2d3e50",
        relief="raised",
        cursor="hand2",
        padx=20,
        pady=10
    )
    botao_voltar.pack(side=tk.BOTTOM, pady=20)

    tela_ranking.mainloop()

# Exemplo de como iniciar o ranking com um nome de usuário
if __name__ == "__main__":
    iniciar_ranking("Usuário Exemplo")
