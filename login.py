import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient

# Função para conectar ao MongoDB
def conectar_mongodb():
    try:
        client = MongoClient("mongodb+srv://joaoalvarez:PjOwQniGDQGSJzvo@cluster0.tguge.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        db = client['Projeto_PI']
        return db
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao conectar ao banco de dados: {e}")
        return None

# Função de cadastro de usuário
def cadastrar_usuario():
    nome = entrada_nome.get()
    senha = entrada_senha.get()

    if len(nome) < 1:
        messagebox.showerror("Erro", "Por favor, insira um nome.")
    elif len(senha) < 4:
        messagebox.showerror("Erro", "A senha deve ter pelo menos 4 caracteres.")
    else:
        db = conectar_mongodb()
        if db is not None:
            usuarios_collection = db['nome']
            senha_collection = db['senha']
            
            if usuarios_collection.find_one({"nome": nome}):
                messagebox.showerror("Erro", "Esse nome já está cadastrado.")
            else:
                usuarios_collection.insert_one({"nome": nome})
                senha_collection.insert_one({"nome": nome, "senha": senha})
                
                messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
                entrada_nome.delete(0, tk.END)
                entrada_senha.delete(0, tk.END)

# Função de login
def realizar_login():
    nome = entrada_login_nome.get()
    senha = entrada_login_senha.get()

    db = conectar_mongodb()
    if db is not None:
        usuarios_collection = db['nome']
        senha_collection = db['senha']
        
        usuario = usuarios_collection.find_one({"nome": nome})
        if usuario:
            senha_db = senha_collection.find_one({"nome": nome})
            if senha_db and senha_db['senha'] == senha:
                messagebox.showinfo("Sucesso", f"Bem-vindo, {nome}!")
                tela_login.destroy()
                abrir_interface(nome)
            else:
                messagebox.showerror("Erro", "Nome ou senha incorretos.")
        else:
            messagebox.showerror("Erro", "Nome não encontrado.")

# Função para abrir a interface após login
def abrir_interface(nome):
    import interface
    interface.iniciar_interface(nome)

# Função para criar a tela de login
def tela_login():
    global entrada_nome, entrada_senha, entrada_login_nome, entrada_login_senha
    global tela_login
    tela_login = tk.Tk()
    tela_login.title("The Writing Board - Tela de Login")
    tela_login.state("zoomed")  # Tela cheia
    tela_login.configure(bg="#1c2533")  # Fundo azul-acinzentado

    # Frame principal para centralizar os elementos
    frame_principal = tk.Frame(tela_login, bg="#1c2533")
    frame_principal.place(relx=0.5, rely=0.5, anchor="center")  # Centralizado na tela

    # Título da tela
    titulo = tk.Label(frame_principal, text="The Writing Board", font=("Arial", 40, "bold"), fg="#ffd700", bg="#1c2533")
    titulo.pack(pady=20)

    subtitulo = tk.Label(frame_principal, text="Entre ou Cadastre-se para começar sua jornada", font=("Arial", 16), fg="#eeeeee", bg="#1c2533")
    subtitulo.pack(pady=10)

    # Seção de Cadastro
    secao_cadastro = tk.LabelFrame(frame_principal, text="Cadastro", bg="#1c2533", fg="#ffd700", font=("Arial", 18, "bold"), padx=30, pady=30, bd=5, relief="solid")
    secao_cadastro.pack(fill="both", expand=True, padx=20, pady=10)

    tk.Label(secao_cadastro, text="Nome:", font=("Arial", 14), fg="#eeeeee", bg="#1c2533").grid(row=0, column=0, sticky="e", padx=10, pady=10)
    entrada_nome = tk.Entry(secao_cadastro, width=30, font=("Arial", 14))
    entrada_nome.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(secao_cadastro, text="Senha:", font=("Arial", 14), fg="#eeeeee", bg="#1c2533").grid(row=1, column=0, sticky="e", padx=10, pady=10)
    entrada_senha = tk.Entry(secao_cadastro, show="*", width=30, font=("Arial", 14))
    entrada_senha.grid(row=1, column=1, padx=10, pady=10)

    botao_cadastrar = tk.Button(secao_cadastro, text="Cadastrar", font=("Arial", 14, "bold"), bg="#ffd700", fg="#1c2533", command=cadastrar_usuario)
    botao_cadastrar.grid(row=2, column=0, columnspan=2, pady=20)

    # Seção de Login
    secao_login = tk.LabelFrame(frame_principal, text="Login", bg="#1c2533", fg="#ffd700", font=("Arial", 18, "bold"), padx=30, pady=30, bd=5, relief="solid")
    secao_login.pack(fill="both", expand=True, padx=20, pady=10)

    tk.Label(secao_login, text="Nome:", font=("Arial", 14), fg="#eeeeee", bg="#1c2533").grid(row=0, column=0, sticky="e", padx=10, pady=10)
    entrada_login_nome = tk.Entry(secao_login, width=30, font=("Arial", 14))
    entrada_login_nome.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(secao_login, text="Senha:", font=("Arial", 14), fg="#eeeeee", bg="#1c2533").grid(row=1, column=0, sticky="e", padx=10, pady=10)
    entrada_login_senha = tk.Entry(secao_login, show="*", width=30, font=("Arial", 14))
    entrada_login_senha.grid(row=1, column=1, padx=10, pady=10)

    botao_login = tk.Button(secao_login, text="Login", font=("Arial", 14, "bold"), bg="#ffd700", fg="#1c2533", command=realizar_login)
    botao_login.grid(row=2, column=0, columnspan=2, pady=20)

    tela_login.mainloop()

if __name__ == "__main__":
    tela_login()