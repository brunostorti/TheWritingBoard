import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFrame
from PyQt5.QtCore import Qt

# Função para redirecionar o jogador para a tela de login
def abrir_tela_login():
    tela_inicio.close()  # Fecha a tela de início
    import login  # Importa o módulo de login
    login.tela_login()  # Chama a função que inicia a tela de login

# Configurações da tela de início
app = QApplication(sys.argv)
tela_inicio = QWidget()
tela_inicio.setWindowTitle("The Writing Board - Tela de Início")
tela_inicio.setGeometry(100, 100, 600, 600)  # Tamanho fixo para todas as telas
tela_inicio.setStyleSheet("background-color: #2C2F33; color: white; font-family: Arial;")

# Layout principal
layout = QVBoxLayout()

# Título do Jogo
titulo = QLabel("The Writing Board")
titulo.setAlignment(Qt.AlignCenter)
titulo.setStyleSheet("font-size: 32px; font-weight: bold; color: #7289DA;")
layout.addWidget(titulo)

# Seção do Botão Iniciar
secao_botao = QFrame()
secao_botao.setFrameShape(QFrame.StyledPanel)
secao_botao.setStyleSheet("background-color: #23272A; border-radius: 10px; padding: 20px;")

botao_login = QPushButton("Iniciar")
botao_login.setStyleSheet("background-color: #7289DA; color: white; border-radius: 8px; padding: 10px;")
botao_login.clicked.connect(abrir_tela_login)  # Conecta o botão à função de redirecionamento
secao_botao_layout = QVBoxLayout()
secao_botao_layout.addWidget(botao_login)
secao_botao.setLayout(secao_botao_layout)
layout.addWidget(secao_botao)

# Ajusta o layout
tela_inicio.setLayout(layout)
tela_inicio.show()

sys.exit(app.exec_())
