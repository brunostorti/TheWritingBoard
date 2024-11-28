import tkinter as tk
from tkinter import messagebox
import subprocess
from pymongo import MongoClient

# Reutilizando a conexão já existente ao MongoDB
db = MongoClient("mongodb+srv://joaoalvarez:PjOwQniGDQGSJzvo@cluster0.tguge.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")["Projeto_PI"]
senha_collection = db["senha"]  # Coleção onde nome e senha estão armazenados
nome_collection = db["nome"]  # Coleção onde o nome do usuário está armazenado

# Função para atualizar o perfil no MongoDB
def atualizar_perfil():
    nome_atual = entrada_nome_atual.get()
    senha_atual = entrada_senha_atual.get()
    novo_nome = entrada_novo_nome.get()
    nova_senha = entrada_nova_senha.get()

    # Verificar se o nome e a senha atual estão corretos na coleção 'senha'
    usuario = senha_collection.find_one({"nome": nome_atual})

    if usuario:
        if usuario['senha'] == senha_atual:
            if len(novo_nome) < 1:
                messagebox.showerror("Erro", "Por favor, insira um novo nome.")
            elif len(nova_senha) < 4:
                messagebox.showerror("Erro", "A nova senha deve ter pelo menos 4 caracteres.")
            else:
                # Verificar se já existe um usuário com o novo nome na coleção 'nome'
                if nome_collection.find_one({"nome": novo_nome}):
                    messagebox.showerror("Erro", "Já existe um usuário com este nome.")
                    return
                else:
                    # Atualizar o nome na coleção 'nome'
                    nome_collection.delete_one({"nome": nome_atual})  # Remove o nome antigo
                    nome_collection.insert_one({"nome": novo_nome})  # Adiciona o novo nome

                    # Atualizar o nome e a senha na coleção 'senha'
                    senha_collection.update_one(
                        {"nome": nome_atual},
                        {"$set": {"nome": novo_nome, "senha": nova_senha}}
                    )
                    messagebox.showinfo("Sucesso", "Perfil atualizado com sucesso!")
                    voltar_interface()
        else:
            messagebox.showerror("Erro", "Senha atual incorreta.")
    else:
        messagebox.showerror("Erro", "Nome atual não encontrado.")

# Função para voltar à interface anterior
def voltar_interface():
    tela_perfil.destroy()
    subprocess.Popen(["python", "interface.py"])

# Função para iniciar a tela de perfil
def iniciar_perfil():
    global tela_perfil, entrada_nome_atual, entrada_senha_atual, entrada_novo_nome, entrada_nova_senha
    tela_perfil = tk.Tk()
    tela_perfil.title("The Writing Board - Perfil")
    tela_perfil.geometry("500x500")
    tela_perfil.configure(bg="#222831")  # Cor de fundo da tela

    # Título da tela de perfil
    titulo = tk.Label(tela_perfil, text="Editar Perfil", font=("Arial", 18, "bold"), fg="#ffd369", bg="#222831")
    titulo.pack(pady=20)

    # Seção de edição do perfil
    secao_perfil = tk.Frame(tela_perfil, bg="#2d3e50", bd=5, relief="solid", padx=20, pady=20)
    secao_perfil.pack(fill="both", expand=True, padx=20, pady=10)

    # Campo para Nome Atual
    tk.Label(secao_perfil, text="Nome Atual:", font=("Arial", 12), fg="#fff", bg="#2d3e50").grid(row=0, column=0, sticky="e", padx=5, pady=5)
    entrada_nome_atual = tk.Entry(secao_perfil, width=30, font=("Arial", 12))
    entrada_nome_atual.grid(row=0, column=1, padx=5, pady=5)

    # Campo para Senha Atual
    tk.Label(secao_perfil, text="Senha Atual:", font=("Arial", 12), fg="#fff", bg="#2d3e50").grid(row=1, column=0, sticky="e", padx=5, pady=5)
    entrada_senha_atual = tk.Entry(secao_perfil, show="*", width=30, font=("Arial", 12))
    entrada_senha_atual.grid(row=1, column=1, padx=5, pady=5)

    # Campo para Novo Nome
    tk.Label(secao_perfil, text="Novo Nome:", font=("Arial", 12), fg="#fff", bg="#2d3e50").grid(row=2, column=0, sticky="e", padx=5, pady=5)
    entrada_novo_nome = tk.Entry(secao_perfil, width=30, font=("Arial", 12))
    entrada_novo_nome.grid(row=2, column=1, padx=5, pady=5)

    # Campo para Nova Senha
    tk.Label(secao_perfil, text="Nova Senha:", font=("Arial", 12), fg="#fff", bg="#2d3e50").grid(row=3, column=0, sticky="e", padx=5, pady=5)
    entrada_nova_senha = tk.Entry(secao_perfil, show="*", width=30, font=("Arial", 12))
    entrada_nova_senha.grid(row=3, column=1, padx=5, pady=5)

    # Botão "Salvar Alterações"
    botao_salvar = tk.Button(
        secao_perfil, 
        text="Salvar Alterações", 
        font=("Arial", 14, "bold"), 
        bg="#fbd11b", 
        fg="#222831", 
        relief="raised", 
        bd=4, 
        width=20, 
        height=2, 
        command=atualizar_perfil
    )
    botao_salvar.grid(row=4, column=0, columnspan=2, pady=10)

    # Botão "Voltar"
    botao_voltar = tk.Button(
        tela_perfil, 
        text="Voltar", 
        font=("Arial", 14, "bold"), 
        bg="#fbd11b", 
        fg="#222831", 
        relief="raised", 
        bd=4, 
        width=20, 
        height=2, 
        command=voltar_interface
    )
    botao_voltar.pack(side=tk.BOTTOM, pady=20)

    tela_perfil.mainloop()

if __name__ == "__main__":
    iniciar_perfil()
