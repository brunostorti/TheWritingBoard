import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient

# Função para conectar ao MongoDB
def conectar_mongodb():
    try:
        # Conectar ao MongoDB
        client = MongoClient("mongodb+srv://joaoalvarez:PjOwQniGDQGSJzvo@cluster0.tguge.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        db = client['Projeto_PI']  # Substitua pelo nome do seu banco de dados
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
        # Conectar ao MongoDB
        db = conectar_mongodb()
        if db is not None:  # Verificação correta para garantir que a conexão foi bem-sucedida
            # Verificar se o nome já está cadastrado
            usuarios_collection = db['nome']  # Coleção para os nomes de usuário
            senha_collection = db['senha']  # Coleção para as senhas
            
            if usuarios_collection.find_one({"nome": nome}):
                messagebox.showerror("Erro", "Esse nome já está cadastrado.")
            else:
                # Inserir o nome e a senha nas coleções apropriadas
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
    if db is not None:  # Verificação correta para garantir que a conexão foi bem-sucedida
        # Acessar as coleções de nome e senha
        usuarios_collection = db['nome']
        senha_collection = db['senha']
        
        # Verificar se o nome existe e a senha corresponde
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
            messagebox.showerror("Erro", "Nome não encontado.")

# Função para abrir a interface após login
def abrir_interface(nome):
    import interface  # Certifique-se de que o módulo interface.py existe
    interface.iniciar_interface(nome)

# Função para criar a tela de login
def tela_login():
    global entrada_nome, entrada_senha, entrada_login_nome, entrada_login_senha
    global tela_login
    tela_login = tk.Tk()
    tela_login.title("The Writing Board - Tela de Login")
    tela_login.geometry("500x500")
    tela_login.configure(bg="#222831")  # Cor de fundo da tela

    # Título da tela de login
    titulo = tk.Label(tela_login, text="Bem-vindo, jogador!", font=("Arial", 18, "bold"), fg="#ffd369", bg="#222831")
    titulo.pack(pady=20)

    # Seção de Cadastro
    secao_cadastro = tk.Frame(tela_login, bg="#2d3e50", bd=5, relief="solid", padx=20, pady=20)
    secao_cadastro.pack(fill="both", expand=True, padx=20, pady=10)

    tk.Label(secao_cadastro, text="Nome:", font=("Arial", 12), fg="#fff", bg="#2d3e50").grid(row=0, column=0, sticky="e", padx=5, pady=5)
    entrada_nome = tk.Entry(secao_cadastro, width=30, font=("Arial", 12))
    entrada_nome.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(secao_cadastro, text="Senha:", font=("Arial", 12), fg="#fff", bg="#2d3e50").grid(row=1, column=0, sticky="e", padx=5, pady=5)
    entrada_senha = tk.Entry(secao_cadastro, show="*", width=30, font=("Arial", 12))
    entrada_senha.grid(row=1, column=1, padx=5, pady=5)

    botao_cadastrar = tk.Button(secao_cadastro, text="Cadastrar", font=("Arial", 14, "bold"), bg="#fbd11b", fg="#222831", relief="raised", bd=4, width=20, height=2, command=cadastrar_usuario)
    botao_cadastrar.grid(row=2, column=0, columnspan=2, pady=10)

    # Seção de Login
    secao_login = tk.Frame(tela_login, bg="#2d3e50", bd=5, relief="solid", padx=20, pady=20)
    secao_login.pack(fill="both", expand=True, padx=20, pady=10)

    tk.Label(secao_login, text="Nome:", font=("Arial", 12), fg="#fff", bg="#2d3e50").grid(row=0, column=0, sticky="e", padx=5, pady=5)
    entrada_login_nome = tk.Entry(secao_login, width=30, font=("Arial", 12))
    entrada_login_nome.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(secao_login, text="Senha:", font=("Arial", 12), fg="#fff", bg="#2d3e50").grid(row=1, column=0, sticky="e", padx=5, pady=5)
    entrada_login_senha = tk.Entry(secao_login, show="*", width=30, font=("Arial", 12))
    entrada_login_senha.grid(row=1, column=1, padx=5, pady=5)

    botao_login = tk.Button(secao_login, text="Login", font=("Arial", 14, "bold"), bg="#fbd11b", fg="#222831", relief="raised", bd=4, width=20, height=2, command=realizar_login)
    botao_login.grid(row=2, column=0, columnspan=2, pady=10)

    tela_login.mainloop()

if __name__ == "__main__":
    tela_login()
