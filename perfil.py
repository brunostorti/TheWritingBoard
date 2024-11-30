import bcrypt
import tkinter as tk
from tkinter import messagebox
import subprocess
from pymongo import MongoClient

# Conectar ao MongoDB
db = MongoClient("mongodb+srv://joaoalvarez:PjOwQniGDQGSJzvo@cluster0.tguge.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")["ProjetoPI"]
usuarios_collection = db["usuarios"]  # Coleção onde nome e senha estão armazenados

# Função para atualizar o perfil no MongoDB
def atualizar_perfil():
    nome_atual = entrada_nome_atual.get()
    senha_atual = entrada_senha_atual.get()
    novo_nome = entrada_novo_nome.get()
    nova_senha = entrada_nova_senha.get()

    # Verificar se o nome e a senha atual estão corretos na coleção 'usuarios'
    usuario = usuarios_collection.find_one({"nome": nome_atual})

    if usuario:
        # Verificar se a senha fornecida corresponde à senha criptografada
        if bcrypt.checkpw(senha_atual.encode('utf-8'), usuario['senha']):  # Sem o .encode() na senha do banco
            if len(novo_nome) < 1:
                messagebox.showerror("Erro", "Por favor, insira um novo nome.")
            elif len(nova_senha) < 4:
                messagebox.showerror("Erro", "A nova senha deve ter pelo menos 4 caracteres.")
            else:
                # Verificar se já existe um usuário com o novo nome
                if usuarios_collection.find_one({"nome": novo_nome}):
                    messagebox.showerror("Erro", "Já existe um usuário com este nome.")
                    return
                else:
                    # Criptografar a nova senha antes de salvar
                    nova_senha_criptografada = bcrypt.hashpw(nova_senha.encode('utf-8'), bcrypt.gensalt())

                    # Atualizar o nome e a senha na coleção 'usuarios'
                    usuarios_collection.update_one(
                        {"nome": nome_atual},
                        {"$set": {"nome": novo_nome, "senha": nova_senha_criptografada}}
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
    tela_perfil.state("zoomed")  # Tela cheia
    tela_perfil.configure(bg="#1c2533")  # Fundo azul-acinzentado

    # Título da tela de perfil
    titulo = tk.Label(tela_perfil, text="Editar Perfil", font=("Arial", 40, "bold"), fg="#ffd700", bg="#1c2533")
    titulo.pack(pady=20)

    # Seção de edição do perfil
    secao_perfil = tk.Frame(tela_perfil, bg="#2d3e50", bd=5, relief="solid", padx=30, pady=30)
    secao_perfil.place(relx=0.5, rely=0.4, anchor="center")  # Centralizando a seção de perfil um pouco acima do centro

    # Campo para Nome Atual
    tk.Label(secao_perfil, text="Nome Atual:", font=("Arial", 16), fg="#fff", bg="#2d3e50").grid(row=0, column=0, sticky="e", padx=15, pady=15)
    entrada_nome_atual = tk.Entry(secao_perfil, width=40, font=("Arial", 16), relief="solid", bd=2)
    entrada_nome_atual.grid(row=0, column=1, padx=15, pady=15)

    # Campo para Senha Atual
    tk.Label(secao_perfil, text="Senha Atual:", font=("Arial", 16), fg="#fff", bg="#2d3e50").grid(row=1, column=0, sticky="e", padx=15, pady=15)
    entrada_senha_atual = tk.Entry(secao_perfil, show="*", width=40, font=("Arial", 16), relief="solid", bd=2)
    entrada_senha_atual.grid(row=1, column=1, padx=15, pady=15)

    # Campo para Novo Nome
    tk.Label(secao_perfil, text="Novo Nome:", font=("Arial", 16), fg="#fff", bg="#2d3e50").grid(row=2, column=0, sticky="e", padx=15, pady=15)
    entrada_novo_nome = tk.Entry(secao_perfil, width=40, font=("Arial", 16), relief="solid", bd=2)
    entrada_novo_nome.grid(row=2, column=1, padx=15, pady=15)

    # Campo para Nova Senha
    tk.Label(secao_perfil, text="Nova Senha:", font=("Arial", 16), fg="#fff", bg="#2d3e50").grid(row=3, column=0, sticky="e", padx=15, pady=15)
    entrada_nova_senha = tk.Entry(secao_perfil, show="*", width=40, font=("Arial", 16), relief="solid", bd=2)
    entrada_nova_senha.grid(row=3, column=1, padx=15, pady=15)

    # Botão "Salvar Alterações"
    botao_salvar = tk.Button(
        secao_perfil, 
        text="Salvar Alterações", 
        font=("Arial", 16, "bold"), 
        bg="#ffd700", 
        fg="#1c2533", 
        relief="raised", 
        bd=4, 
        width=25, 
        height=2, 
        command=atualizar_perfil
    )
    botao_salvar.grid(row=4, column=0, columnspan=2, pady=20)

    # Botão "Voltar" (Agora na parte inferior da tela)
    botao_voltar = tk.Button(
        tela_perfil, 
        text="Voltar", 
        font=("Arial", 16, "bold"), 
        bg="#ffd700", 
        fg="#1c2533", 
        relief="raised", 
        bd=4, 
        width=20, 
        height=2, 
        command=voltar_interface
    )
    botao_voltar.pack(side="bottom", pady=20)  # Posicionando o botão de voltar na parte inferior

    tela_perfil.mainloop()

if __name__ == "__main__":
    iniciar_perfil()