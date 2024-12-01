import tkinter as tk
from pymongo import MongoClient

client = MongoClient('mongodb+srv://joaoalvarez:PjOwQniGDQGSJzvo@cluster0.tguge.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['ProjetoPI']
pontuacoes_collection = db['pontuacoes']

def iniciar_ranking(nome_usuario):
    tela_ranking = tk.Tk()
    tela_ranking.title("The Writing Board - Ranking")
    tela_ranking.configure(bg="#2d3e50")

    tela_ranking.attributes("-fullscreen", True)

    texto_informativo = tk.Label(
        tela_ranking,
        text=f"Aqui, {nome_usuario}, ficam suas melhores pontuações.",
        font=("Arial", 16, "bold"),
        bg="#2d3e50",
        fg="#fbd11b",
        wraplength=800,
        justify="center"
    )
    texto_informativo.pack(pady=20)

    frame_ranking = tk.Frame(tela_ranking, bg="#2d3e50")
    frame_ranking.pack(pady=20, fill=tk.BOTH, expand=True)

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
                texto_ranking += f"{i}. {entry['nome']} - {entry['pontuacao']} pontos ({entry['nivel']})\n"
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

    ranking_geral = pontuacoes_collection.find().sort("pontuacao", -1).limit(10)

    criar_coluna_ranking(frame_ranking, "Ranking Geral", ranking_geral)

    def voltar_interface():
        tela_ranking.quit()
        tela_ranking.destroy()
        import interface
        interface.iniciar_interface()

    botao_voltar = tk.Button(
        tela_ranking,
        text="Voltar",
        command=voltar_interface,
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

if __name__ == "__main__":
    iniciar_ranking("Usuário Exemplo") 
