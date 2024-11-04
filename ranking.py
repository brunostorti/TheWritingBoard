import tkinter as tk
from datetime import datetime
import json

# Função para carregar dados do ranking do arquivo JSON
def carregar_ranking():
    try:
        with open('ranking.json', 'r') as arquivo:
            dados = json.load(arquivo)
            return dados["ranking"]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Função para salvar dados do ranking no arquivo JSON
def salvar_ranking(dados_ranking):
    with open('ranking.json', 'w') as arquivo:
        json.dump({"ranking": dados_ranking}, arquivo, indent=4)

# Inicializando os dados de ranking
dados_ranking = carregar_ranking()

# Função para adicionar resultados ao ranking
def adicionar_resultado(modulo, pontos):
    resultado = {
        "modulo": modulo,
        "pontos": pontos,
        "data": datetime.now().strftime("%d/%m/%Y")
    }
    dados_ranking.append(resultado)
    salvar_ranking(dados_ranking)  # Salva o ranking atualizado no arquivo JSON

# Função para iniciar a tela de ranking
def iniciar_ranking():
    tela_ranking = tk.Tk()
    tela_ranking.title("The Writing Board - Ranking")
    tela_ranking.geometry("500x500")

    # Introdução ao jogador
    introducao = tk.Label(
        tela_ranking, 
        text="Aqui estão seus últimos resultados! Seus pontos ficarão registrados \n"
             "junto com o módulo no qual você jogou. Continue se superando!",
        font=("Arial", 14),
        justify="center"
    )
    introducao.pack(pady=20)

    # Exibição dos últimos resultados
    resultados_frame = tk.Frame(tela_ranking)
    resultados_frame.pack(pady=20)

    for i, resultado in enumerate(dados_ranking, start=1):
        resultado_texto = f"{i}. Módulo: {resultado['modulo']} - Pontos: {resultado['pontos']} - Data: {resultado['data']}"
        resultado_label = tk.Label(resultados_frame, text=resultado_texto, font=("Arial", 12))
        resultado_label.pack(anchor="w", pady=5)

    # Função para voltar para a tela anterior (interface.py)
    def voltar_interface():
        tela_ranking.destroy()
        import interface
        interface.iniciar_interface()

    # Botão Voltar
    botao_voltar = tk.Button(tela_ranking, text="Voltar", command=voltar_interface)
    botao_voltar.pack(side=tk.BOTTOM, pady=20)

    tela_ranking.mainloop()

# Exemplo de uso da função de adicionar resultado
# Aqui você deve substituir pela lógica real do seu jogo
# Adicione esta chamada após o jogador completar um nível
# Por exemplo
