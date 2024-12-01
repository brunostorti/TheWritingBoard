import tkinter as tk
from PIL import Image, ImageTk 
from login import iniciar_login 
from pymongo import MongoClient 



def abrir_tela_login():
    tela_inicio.destroy() 
    iniciar_login() 


def conectar_mongodb():
    try:
       
        client = MongoClient(
            "mongodb+srv://joaoalvarez:PjOwQniGDQGSJzvo@cluster0.tguge.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        )

        
        db = client["ProjetoPI"]  

        colecao_usuarios = db["usuarios"]  

        
        numero_de_documentos = colecao_usuarios.count_documents({})
        print(f"Número de documentos na coleção de usuários: {numero_de_documentos}")

    except Exception as e:
        print("Erro ao conectar ao MongoDB:", e)



tela_inicio = tk.Tk()
tela_inicio.title("The Writing Board - Tela de Início")
tela_inicio.configure(bg="#1c2533") 


tela_inicio.attributes("-fullscreen", True)


main_frame = tk.Frame(tela_inicio, bg="#1c2533", padx=20, pady=20)
main_frame.pack(expand=True, fill="both")


titulo_frame = tk.Frame(main_frame, bg="#1c2533")
titulo_frame.pack(pady=(50, 30), anchor="center")

try:
   
    img_esquerda = Image.open("imagens/images.png")  
    img_esquerda = img_esquerda.resize((150, 150)) 
    esquerda_img = ImageTk.PhotoImage(img_esquerda)
    esquerda_label = tk.Label(titulo_frame, image=esquerda_img, bg="#1c2533")
    esquerda_label.image = esquerda_img
    esquerda_label.pack(side="left", padx=20)

    img_titulo = Image.open("imagens/titulo.png")  
    img_titulo = img_titulo.resize((800, 320)) 
    titulo_img = ImageTk.PhotoImage(img_titulo)
    titulo_label = tk.Label(titulo_frame, image=titulo_img, bg="#1c2533")
    titulo_label.image = titulo_img
    titulo_label.pack(side="left", padx=20)
except Exception as e:
    print(f"Erro ao carregar a imagem: {e}")

linha = tk.Frame(main_frame, bg="#ffd700", height=3, width=700)
linha.pack(pady=(5, 15), fill="x")

secao_botao = tk.Frame(main_frame, bg="#1c2533")
secao_botao.pack(pady=(40, 60)) 

botao_iniciar = tk.Button(
    secao_botao,
    text="Iniciar",
    font=("Arial", 20, "bold"),
    bg="#ffd700",  
    fg="#1c2533",  
    activebackground="#e6c300",  
    activeforeground="white",
    width=15,
    height=2,
    relief="groove",
    bd=5,
    cursor="hand2",
    command=lambda: [abrir_tela_login(), conectar_mongodb()]
)
botao_iniciar.pack()

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

tela_inicio.mainloop()