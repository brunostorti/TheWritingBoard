import tkinter as tk
from PIL import Image, ImageTk  # Para trabalhar com imagens
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
        client = MongoClient(
            "mongodb+srv://joaoalvarez:PjOwQniGDQGSJzvo@cluster0.tguge.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        )

        # Acessa o banco de dados desejado
        db = client["Projeto_PI"]  # Substitua 'nome_do_seu_banco' pelo nome do seu banco

        # Exemplo de acesso a uma coleção dentro do banco de dados
        colecao = db["user"]  # Substitua 'nome_da_sua_colecao' pelo nome da sua coleção

        # Apenas um exemplo de operação: contar o número de documentos na coleção
        numero_de_documentos = colecao.count_documents({})
        print(f"Número de documentos na coleção: {numero_de_documentos}")

    except Exception as e:
        print("Erro ao conectar ao MongoDB:", e)


# Configurações da tela de início
tela_inicio = tk.Tk()
tela_inicio.title("The Writing Board - Tela de Início")
tela_inicio.configure(bg="#1c2533")  # Fundo azul-acinzentado sofisticado

# Habilitar tela cheia
tela_inicio.attributes("-fullscreen", True)

# Frame principal para centralizar conteúdo
main_frame = tk.Frame(tela_inicio, bg="#1c2533", padx=20, pady=20)
main_frame.pack(expand=True, fill="both")

# Adicionando o layout com a imagem 'images.png' e o título
titulo_frame = tk.Frame(main_frame, bg="#1c2533")
titulo_frame.pack(pady=(50, 30), anchor="center")

try:
    # Imagem 'images.png' à esquerda
    img_esquerda = Image.open("imagens/images.png")  # Substitua pelo caminho correto
    img_esquerda = img_esquerda.resize((150, 150))  # Redimensionar a imagem
    esquerda_img = ImageTk.PhotoImage(img_esquerda)
    esquerda_label = tk.Label(titulo_frame, image=esquerda_img, bg="#1c2533")
    esquerda_label.image = esquerda_img
    esquerda_label.pack(side="left", padx=20)

    # Imagem 'titulo.png' ao lado direito
    img_titulo = Image.open("imagens/titulo.png")  # Substitua pelo caminho correto
    img_titulo = img_titulo.resize((600, 250))  # Ajuste do tamanho
    titulo_img = ImageTk.PhotoImage(img_titulo)
    titulo_label = tk.Label(titulo_frame, image=titulo_img, bg="#1c2533")
    titulo_label.image = titulo_img
    titulo_label.pack(side="left", padx=20)
except Exception as e:
    print(f"Erro ao carregar a imagem: {e}")

# Linha decorativa abaixo das imagens
linha = tk.Frame(main_frame, bg="#ffd700", height=3, width=700)
linha.pack(pady=(5, 15), fill="x")

# Seção do botão Iniciar com mais espaçamento acima e abaixo
secao_botao = tk.Frame(main_frame, bg="#1c2533")
secao_botao.pack(pady=(40, 60))  # Aumentando o espaçamento inferior

botao_iniciar = tk.Button(
    secao_botao,
    text="Iniciar",
    font=("Arial", 20, "bold"),
    bg="#ffd700",  # Botão dourado
    fg="#1c2533",  # Texto azul-acinzentado
    activebackground="#e6c300",  # Amarelo mais intenso ao clicar
    activeforeground="white",
    width=15,
    height=2,
    relief="groove",
    bd=5,
    cursor="hand2",
    command=lambda: [abrir_tela_login(), conectar_mongodb()]
)
botao_iniciar.pack()

# Rodapé com estilo premium
rodape = tk.Frame(tela_inicio, bg="#ffd700", height=40)
rodape.pack(side="bottom", fill="x")
texto_rodape = tk.Label(
    rodape,
    text="© 2024 The Writing Board - Feito com paixão e criatividade",
    font=("Arial", 11, "italic"),
    bg="#ffd700",
    fg="#1c2533"
)
texto_rodape.pack()

# Inicia a tela
tela_inicio.mainloop()