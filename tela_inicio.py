import tkinter as tk
from login import tela_login  # Importa a função tela_login de login.py
from pymongo import MongoClient  # Importa o MongoClient para conectar ao MongoDB

# Função para redirecionar o jogador para a tela de login
def abrir_tela_login():
    tela_inicio.destroy()  # Fecha a tela de início do Tkinter
    tela_login()  # Chama a função tela_login para exibir a tela de login

# Função para conectar ao MongoDB
def conectar_mongodb():
    try:
        # Cria a conexão usando o URI do MongoDB
        client = MongoClient("mongodb+srv://joaoalvarez:PjOwQniGDQGSJzvo@cluster0.tguge.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        
        # Acessa o banco de dados desejado
        db = client['Projeto_PI']  # Substitua 'nome_do_seu_banco' pelo nome do seu banco
        
        # Exemplo de acesso a uma coleção dentro do banco de dados
        colecao = db['user']  # Substitua 'nome_da_sua_colecao' pelo nome da sua coleção
        
        # Apenas um exemplo de operação: contar o número de documentos na coleção
        numero_de_documentos = colecao.count_documents({})
        print(f"Número de documentos na coleção: {numero_de_documentos}")
        
    except Exception as e:
        print("Erro ao conectar ao MongoDB:", e)

# Configurações da tela de início
tela_inicio = tk.Tk()
tela_inicio.title("The Writing Board - Tela de Início")
tela_inicio.geometry("600x600")  # Tamanho fixo para todas as telas
tela_inicio.configure(bg="#222831")  # Cor de fundo como nas outras telas

# Título do Jogo
titulo = tk.Label(
    tela_inicio,
    text="The Writing Board",
    font=("Arial", 32, "bold"),
    fg="#ffd369",  # Cor do texto, amarelo claro como nas outras telas
    bg="#222831"  # Cor de fundo da tela
)
titulo.pack(pady=50)

# Seção do Botão Iniciar
secao_botao = tk.Frame(tela_inicio, bg="#2d3e50", bd=5, relief="solid", padx=20, pady=20)
secao_botao.pack(pady=30)

botao_iniciar = tk.Button(
    secao_botao,
    text="Iniciar",
    font=("Arial", 14, "bold"),
    bg="#fbd11b",  # Cor do botão como nas outras telas
    fg="#222831",  # Cor do texto do botão
    activebackground="#e8c16e",  # Cor de fundo ao clicar
    activeforeground="white",
    relief="raised",
    bd=4,
    width=20,
    height=2,
    command=lambda: [abrir_tela_login(), conectar_mongodb()]  # Conecta ao MongoDB ao iniciar
)
botao_iniciar.pack()

# Inicia a tela
tela_inicio.mainloop()
