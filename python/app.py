from PySide6.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QPushButton,
    QWidget,
    QLabel,
    QFrame
)
from PySide6.QtCore import Qt
from screen.cadastrar import Cadastrar
from screen.listar import Listar

import sys


class App:
    def __init__(self):
        self.app = QApplication(sys.argv)

        self.janela = QWidget()
        self.janela.setWindowTitle("🎓 Sistema Universidade")
        self.janela.resize(500, 350)

        self.janela.setStyleSheet("""
            QWidget {
                background-color: #1e1e2f;
                color: white;
                font-family: Arial;
            }

            QLabel {
                font-size: 22px;
                font-weight: bold;
                margin-bottom: 20px;
            }

            QPushButton {
                background-color: #4e73df;
                border-radius: 8px;
                padding: 12px;
                font-size: 16px;
            }

            QPushButton:hover {
                background-color: #2e59d9;
            }

            QPushButton:pressed {
                background-color: #224abe;
            }
        """)

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignCenter)
        self.layout.setSpacing(15)

        self.janela.setLayout(self.layout)

        self.criar_interface()
        self.janela.show()

    def criar_interface(self):
        titulo = QLabel("Sistema de Gerenciamento Acadêmico")
        titulo.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(titulo)

        linha = QFrame()
        linha.setFrameShape(QFrame.HLine)
        linha.setStyleSheet("background-color: #4e73df; max-height: 2px;")
        self.layout.addWidget(linha)

        botao_listar = QPushButton("📋 Listar Alunos")
        botao_listar.clicked.connect(self.abrir_listagem)
        self.layout.addWidget(botao_listar)

        botao_cadastrar = QPushButton("➕ Cadastrar Aluno")
        botao_cadastrar.clicked.connect(self.abrir_cadastro)
        self.layout.addWidget(botao_cadastrar)

    def abrir_listagem(self):
        self.tela_listagem = Listar(self.app)
        self.tela_listagem.janela.show()

    def abrir_cadastro(self):
        self.tela_cadastro = Cadastrar(self.app)
        self.tela_cadastro.janela.show()


if __name__ == "__main__":
    system = App()
    sys.exit(system.app.exec())