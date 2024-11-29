import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient

# Função para conectar ao MongoDB
def conectar_mongodb():
    try:
        client = MongoClient("mongodb+srv://seu_usuario:senha@cluster.mongodb.net/?retryWrites=true&w=majority")
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
        if db:
            usuarios_collection = db['usuarios']
            if usuarios_collection.find_one({"nome": nome}):
                messagebox.showerror("Erro", "Esse nome já está cadastrado.")
            else:
                usuarios_collection.insert_one({"nome": nome, "senha": senha})
                messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
                entrada_nome.delete(0, tk.END)
                entrada_senha.delete(0, tk.END)

# Função de login
def realizar_login():
    nome = entrada_login_nome.get()
    senha = entrada_login_senha.get()

    db = conectar_mongodb()
    if db:
        usuarios_collection = db['usuarios']
        usuario = usuarios_collection.find_one({"nome": nome})
        if usuario and usuario['senha'] == senha:
            messagebox.showinfo("Sucesso", f"Bem-vindo, {nome}!")
            tela_login.destroy()
            abrir_interface(nome)
        else:
            messagebox.showerror("Erro", "Nome ou senha incorretos.")

# Função para abrir a interface após login
def abrir_interface(nome):
    # Importar e abrir a interface principal
    import interface
    interface.iniciar_interface(nome)

# Função principal para exibir a tela de login/cadastro
def tela_login():
    global entrada_nome, entrada_senha, entrada_login_nome, entrada_login_senha
    tela_login = tk.Tk()
    tela_login.title("The Writing Board - Tela de Login")
    tela_login.state("zoomed")  # Configuração para tela cheia
    tela_login.configure(bg="#1c2533")  # Fundo azul-acinzentado

    # Frame centralizado
    frame_principal = tk.Frame(tela_login, bg="#1c2533")
    frame_principal.place(relx=0.5, rely=0.5, anchor="center")

    # Título e subtítulo
    tk.Label(frame_principal, text="The Writing Board", font=("Arial", 40, "bold"), fg="#ffd700", bg="#1c2533").pack(pady=20)
    tk.Label(frame_principal, text="Entre ou Cadastre-se para começar sua jornada", font=("Arial", 16), fg="#eeeeee", bg="#1c2533").pack(pady=10)

    # Seção de cadastro
    secao_cadastro = tk.LabelFrame(frame_principal, text="Cadastro", bg="#1c2533", fg="#ffd700", font=("Arial", 18, "bold"), padx=30, pady=30, bd=5, relief="solid")
    secao_cadastro.pack(fill="both", expand=True, padx=20, pady=10)
    tk.Label(secao_cadastro, text="Nome:", font=("Arial", 14), fg="#eeeeee", bg="#1c2533").grid(row=0, column=0, sticky="e", padx=10, pady=10)
    entrada_nome = tk.Entry(secao_cadastro, width=30, font=("Arial", 14))
    entrada_nome.grid(row=0, column=1, padx=10, pady=10)
    tk.Label(secao_cadastro, text="Senha:", font=("Arial", 14), fg="#eeeeee", bg="#1c2533").grid(row=1, column=0, sticky="e", padx=10, pady=10)
    entrada_senha = tk.Entry(secao_cadastro, show="*", width=30, font=("Arial", 14))
    entrada_senha.grid(row=1, column=1, padx=10, pady=10)
    tk.Button(secao_cadastro, text="Cadastrar", font=("Arial", 14, "bold"), bg="#ffd700", fg="#1c2533", command=cadastrar_usuario).grid(row=2, column=0, columnspan=2, pady=20)

    # Seção de login
    secao_login = tk.LabelFrame(frame_principal, text="Login", bg="#1c2533", fg="#ffd700", font=("Arial", 18, "bold"), padx=30, pady=30, bd=5, relief="solid")
    secao_login.pack(fill="both", expand=True, padx=20, pady=10)
    tk.Label(secao_login, text="Nome:", font=("Arial", 14), fg="#eeeeee", bg="#1c2533").grid(row=0, column=0, sticky="e", padx=10, pady=10)
    entrada_login_nome = tk.Entry(secao_login, width=30, font=("Arial", 14))
    entrada_login_nome.grid(row=0, column=1, padx=10, pady=10)
    tk.Label(secao_login, text="Senha:", font=("Arial", 14), fg="#eeeeee", bg="#1c2533").grid(row=1, column=0, sticky="e", padx=10, pady=10)
    entrada_login_senha = tk.Entry(secao_login, show="*", width=30, font=("Arial", 14))
    entrada_login_senha.grid(row=1, column=1, padx=10, pady=10)
    tk.Button(secao_login, text="Login", font=("Arial", 14, "bold"), bg="#ffd700", fg="#1c2533", command=realizar_login).grid(row=2, column=0, columnspan=2, pady=20)

    tela_login.mainloop()

if __name__ == "__main__":
    tela_login()
