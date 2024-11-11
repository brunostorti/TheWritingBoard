import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QFrame, QDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QFont

# Funções para carregar e salvar usuários
def carregar_usuarios():
    try:
        with open("usuarios.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def salvar_usuarios():
    with open("usuarios.json", "w") as f:
        json.dump(usuarios, f)

usuarios = carregar_usuarios()

def cadastrar_usuario():
    nome = entrada_nome.text()
    senha = entrada_senha.text()

    if len(nome) < 1:
        show_error("Por favor, insira um nome.")
    elif len(senha) < 4:
        show_error("A senha deve ter pelo menos 4 caracteres.")
    elif nome in usuarios:
        show_error("Esse nome já está cadastrado.")
    else:
        usuarios[nome] = senha
        salvar_usuarios()
        show_success("Cadastro realizado com sucesso!")
        entrada_nome.clear()
        entrada_senha.clear()

def realizar_login():
    nome = entrada_login_nome.text()
    senha = entrada_login_senha.text()

    if nome in usuarios and usuarios[nome] == senha:
        show_success(f"Bem-vindo, {nome}!")
        login_window.hide()  # Oculta a janela de login
        abrir_interface(nome)
    else:
        show_error("Nome ou senha incorretos.")

def show_error(message):
    error_dialog = QDialog()
    error_dialog.setWindowTitle("Erro")
    error_label = QLabel(message)
    error_label.setAlignment(Qt.AlignCenter)
    layout = QVBoxLayout()
    layout.addWidget(error_label)
    error_dialog.setLayout(layout)
    error_dialog.exec_()

def show_success(message):
    success_dialog = QDialog()
    success_dialog.setWindowTitle("Sucesso")
    success_label = QLabel(message)
    success_label.setAlignment(Qt.AlignCenter)
    layout = QVBoxLayout()
    layout.addWidget(success_label)
    success_dialog.setLayout(layout)
    success_dialog.exec_()

def abrir_interface(nome):
    interface_window = QWidget()
    interface_window.setWindowTitle(f"Bem-vindo, {nome}!")
    interface_window.setGeometry(100, 100, 600, 600)
    interface_layout = QVBoxLayout()

    # Adicionar mais elementos da interface principal aqui
    welcome_label = QLabel(f"Seja bem-vindo, {nome}!")
    interface_layout.addWidget(welcome_label)

    botao_logout = QPushButton("Sair")
    botao_logout.setStyleSheet("background-color: #7289DA; color: white; border-radius: 8px; padding: 12px; font-size: 18px;")
    botao_logout.clicked.connect(lambda: sair(interface_window))
    interface_layout.addWidget(botao_logout)

    interface_window.setLayout(interface_layout)
    interface_window.show()

def sair(window):
    window.close()
    login_window.show()  # Mostra a janela de login novamente

def tela_login():
    global entrada_nome, entrada_senha, entrada_login_nome, entrada_login_senha, login_window

    app = QApplication(sys.argv)
    login_window = QWidget()
    login_window.setWindowTitle("The Writing Board - Tela de Login")
    login_window.setGeometry(100, 100, 600, 600)  # Tamanho fixo para todas as telas
    login_window.setStyleSheet("background-color: #2C2F33; color: white; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;")

    # Definir uma fonte mais sofisticada
    font = QFont("Segoe UI", 12)
    app.setFont(font)

    # Layout principal
    layout = QVBoxLayout()

    # Título
    titulo = QLabel("Bem-vindo, jogador!")
    titulo.setAlignment(Qt.AlignCenter)
    titulo.setStyleSheet("font-size: 28px; font-weight: bold; color: #7289DA;")
    layout.addWidget(titulo)

    # Seção de Cadastro
    secao_cadastro = QFrame()
    secao_cadastro.setFrameShape(QFrame.StyledPanel)
    secao_cadastro.setStyleSheet("background-color: #23272A; border-radius: 10px; padding: 20px;")
    
    cadastro_layout = QVBoxLayout()
    cadastro_titulo = QLabel("Cadastro")
    cadastro_titulo.setStyleSheet("font-size: 20px; color: #7289DA; font-weight: bold;")
    cadastro_layout.addWidget(cadastro_titulo)

    cadastro_layout.addWidget(QLabel("Nome:"))
    entrada_nome = QLineEdit()
    entrada_nome.setStyleSheet("background-color: #99AAB5; border-radius: 8px; padding: 10px; font-size: 16px;")
    cadastro_layout.addWidget(entrada_nome)

    cadastro_layout.addWidget(QLabel("Senha:"))
    entrada_senha = QLineEdit()
    entrada_senha.setStyleSheet("background-color: #99AAB5; border-radius: 8px; padding: 10px; font-size: 16px;")
    entrada_senha.setEchoMode(QLineEdit.Password)
    cadastro_layout.addWidget(entrada_senha)

    botao_cadastrar = QPushButton("Cadastrar")
    botao_cadastrar.setStyleSheet("background-color: #7289DA; color: white; border-radius: 8px; padding: 12px; font-size: 18px;")
    botao_cadastrar.clicked.connect(cadastrar_usuario)
    cadastro_layout.addWidget(botao_cadastrar)

    secao_cadastro.setLayout(cadastro_layout)
    layout.addWidget(secao_cadastro)

    # Seção de Login
    secao_login = QFrame()
    secao_login.setFrameShape(QFrame.StyledPanel)
    secao_login.setStyleSheet("background-color: #23272A; border-radius: 10px; padding: 20px;")
    
    login_layout = QVBoxLayout()
    login_titulo = QLabel("Login")
    login_titulo.setStyleSheet("font-size: 20px; color: #7289DA; font-weight: bold;")
    login_layout.addWidget(login_titulo)

    login_layout.addWidget(QLabel("Nome:"))
    entrada_login_nome = QLineEdit()
    entrada_login_nome.setStyleSheet("background-color: #99AAB5; border-radius: 8px; padding: 10px; font-size: 16px;")
    login_layout.addWidget(entrada_login_nome)

    login_layout.addWidget(QLabel("Senha:"))
    entrada_login_senha = QLineEdit()
    entrada_login_senha.setStyleSheet("background-color: #99AAB5; border-radius: 8px; padding: 10px; font-size: 16px;")
    entrada_login_senha.setEchoMode(QLineEdit.Password)
    login_layout.addWidget(entrada_login_senha)

    botao_login = QPushButton("Login")
    botao_login.setStyleSheet("background-color: #7289DA; color: white; border-radius: 8px; padding: 12px; font-size: 18px;")
    botao_login.clicked.connect(realizar_login)
    login_layout.addWidget(botao_login)

    secao_login.setLayout(login_layout)
    layout.addWidget(secao_login)

    login_window.setLayout(layout)
    login_window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    tela_login()
