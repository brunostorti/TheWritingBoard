# login.py

import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient
import bcrypt  # Importa o módulo bcrypt para hashing de senhas

usuario_logado = ""  # Variável global para armazenar o nome do usuário logado

def conectar_mongodb():
    try:
        client = MongoClient("mongodb+srv://joaoalvarez:PjOwQniGDQGSJzvo@cluster0.tguge.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        db = client['ProjetoPI']
        return db
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao conectar ao banco de dados: {e}")
        return None

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
            usuarios_collection = db['usuarios']
            
            if usuarios_collection.find_one({"nome": nome}):
                messagebox.showerror("Erro", "Esse nome já está cadastrado.")
            else:
                hashed_senha = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())
                usuarios_collection.insert_one({"nome": nome, "senha": hashed_senha})
                messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
                entrada_nome.delete(0, tk.END)
                entrada_senha.delete(0, tk.END)

def realizar_login():
    global usuario_logado  # Tornando a variável global
    nome = entrada_login_nome.get()
    senha = entrada_login_senha.get()

    db = conectar_mongodb()
    if db is not None:
        usuarios_collection = db['usuarios']
        usuario = usuarios_collection.find_one({"nome": nome})
        if usuario:
            if bcrypt.checkpw(senha.encode('utf-8'), usuario['senha']):
                usuario_logado = nome  # Aqui o nome do usuário logado é atribuído
                messagebox.showinfo("Sucesso", f"Bem-vindo, {nome}!")
                tela_login.destroy()
                abrir_interface()
            else:
                messagebox.showerror("Erro", "Nome ou senha incorretos.")
        else:
            messagebox.showerror("Erro", "Nome não encontrado.")

def abrir_interface():
    import interface
    interface.iniciar_interface(usuario_logado)

def iniciar_login():
    # Função que reinicia a tela de login
    global entrada_nome, entrada_senha, entrada_login_nome, entrada_login_senha
    global tela_login
    tela_login = tk.Tk()
    tela_login.title("The Writing Board - Tela de Login")
    tela_login.state("zoomed")  # Habilita tela cheia
    tela_login.configure(bg="#222831")

    titulo = tk.Label(
        tela_login, 
        text="Bem-vindo, jogador!", 
        font=("Arial", 28, "bold"), 
        fg="#ffd369", 
        bg="#222831"
    )
    titulo.pack(pady=40)

    # Seção de cadastro
    secao_cadastro = tk.Frame(tela_login, bg="#2d3e50", bd=5, relief="solid", padx=30, pady=30)
    secao_cadastro.place(relx=0.5, rely=0.35, anchor="center")

    tk.Label(secao_cadastro, text="Faça seu cadastro", font=("Arial", 18, "bold"), fg="#ffd369", bg="#2d3e50").grid(row=0, column=0, columnspan=2, pady=15)
    
    tk.Label(secao_cadastro, text="Nome:", font=("Arial", 16), fg="#fff", bg="#2d3e50").grid(row=1, column=0, sticky="e", padx=15, pady=10)
    entrada_nome = tk.Entry(secao_cadastro, width=30, font=("Arial", 16), relief="solid", bd=2)
    entrada_nome.grid(row=1, column=1, padx=15, pady=10)

    tk.Label(secao_cadastro, text="Senha:", font=("Arial", 16), fg="#fff", bg="#2d3e50").grid(row=2, column=0, sticky="e", padx=15, pady=10)
    entrada_senha = tk.Entry(secao_cadastro, show="*", width=30, font=("Arial", 16), relief="solid", bd=2)
    entrada_senha.grid(row=2, column=1, padx=15, pady=10)

    botao_cadastrar = tk.Button(
        secao_cadastro, 
        text="Cadastrar", 
        font=("Arial", 16, "bold"), 
        bg="#ffd700", 
        fg="#222831", 
        relief="raised", 
        bd=4, 
        width=20, 
        height=2, 
        command=cadastrar_usuario
    )
    botao_cadastrar.grid(row=3, column=0, columnspan=2, pady=20)

    # Seção de login
    secao_login = tk.Frame(tela_login, bg="#2d3e50", bd=5, relief="solid", padx=30, pady=30)
    secao_login.place(relx=0.5, rely=0.65, anchor="center")

    tk.Label(secao_login, text="Caso já tenha uma conta, faça seu login", font=("Arial", 18, "bold"), fg="#ffd369", bg="#2d3e50").grid(row=0, column=0, columnspan=2, pady=15)

    tk.Label(secao_login, text="Nome:", font=("Arial", 16), fg="#fff", bg="#2d3e50").grid(row=1, column=0, sticky="e", padx=15, pady=10)
    entrada_login_nome = tk.Entry(secao_login, width=30, font=("Arial", 16), relief="solid", bd=2)
    entrada_login_nome.grid(row=1, column=1, padx=15, pady=10)

    tk.Label(secao_login, text="Senha:", font=("Arial", 16), fg="#fff", bg="#2d3e50").grid(row=2, column=0, sticky="e", padx=15, pady=10)
    entrada_login_senha = tk.Entry(secao_login, show="*", width=30, font=("Arial", 16), relief="solid", bd=2)
    entrada_login_senha.grid(row=2, column=1, padx=15, pady=10)

    botao_login = tk.Button(
        secao_login, 
        text="Login", 
        font=("Arial", 16, "bold"), 
        bg="#ffd700", 
        fg="#222831", 
        relief="raised", 
        bd=4, 
        width=20, 
        height=2, 
        command=realizar_login
    )
    botao_login.grid(row=3, column=0, columnspan=2, pady=20)

    tela_login.mainloop()

if __name__ == "__main__":
    iniciar_login()
