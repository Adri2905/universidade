from modulos.mysql import MySQL
from modulos.aluno import Aluno

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox,
    QFrame
)
from PySide6.QtCore import Qt


class Cadastrar:
    def __init__(self, app):
        self.app = app
        self.janela = QWidget()
        self.layout = QVBoxLayout()
        self.banco = MySQL()

        self.campos = {}

        self.configurar_janela()
        self.criar_componentes()

    def configurar_janela(self):
        self.janela.setWindowTitle("➕ Cadastrar Aluno")

        screen = self.app.primaryScreen()
        tamanho = screen.availableGeometry()

        largura = int(tamanho.width() * 0.4)
        altura = int(tamanho.height() * 0.6)

        self.janela.resize(largura, altura)
        self.janela.setMinimumSize(400, 450)

        self.janela.setLayout(self.layout)

        self.janela.setStyleSheet("""
            QWidget {
                background-color: #1e1e2f;
                color: white;
                font-family: Arial;
            }

            QLineEdit {
                background-color: #2c2f48;
                border-radius: 6px;
                padding: 8px;
                border: 1px solid #444;
            }

            QLineEdit:focus {
                border: 1px solid #4e73df;
            }

            QPushButton {
                background-color: #4e73df;
                border-radius: 8px;
                padding: 10px;
            }

            QPushButton:hover {
                background-color: #2e59d9;
            }
        """)

    def criar_componentes(self):
        titulo = QLabel("Cadastro de Novo Aluno")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-size:18px; font-weight:bold;")
        self.layout.addWidget(titulo)

        linha = QFrame()
        linha.setFrameShape(QFrame.HLine)
        linha.setStyleSheet("background-color:#4e73df; max-height:2px;")
        self.layout.addWidget(linha)

        campos_texto = {
            "nome": "Nome",
            "email": "Email",
            "cpf": "CPF",
            "telefone": "Telefone",
            "endereco": "Endereço"
        }

        for chave, texto in campos_texto.items():
            label = QLabel(texto)
            campo = QLineEdit()
            self.layout.addWidget(label)
            self.layout.addWidget(campo)
            self.campos[chave] = campo

        botao = QPushButton("💾 Cadastrar")
        botao.clicked.connect(self.cadastrar)
        self.layout.addWidget(botao)

    def validar_campos(self):
        for chave, campo in self.campos.items():
            if not campo.text().strip():
                QMessageBox.warning(self.janela, "Erro", f"O campo {chave} é obrigatório.")
                return False
        return True

    def cadastrar(self):
        if not self.validar_campos():
            return

        aluno = Aluno(
            self.campos["nome"].text(),
            self.campos["email"].text(),
            self.campos["cpf"].text(),
            self.campos["telefone"].text(),
            self.campos["endereco"].text(),
        )

        try:
            self.banco.connect()
            aluno.cadastrar(self.banco)
            QMessageBox.information(self.janela, "Sucesso", "Aluno cadastrado!")
            self.limpar_campos()
        except Exception as e:
            QMessageBox.critical(self.janela, "Erro", str(e))
        finally:
            self.banco.disconnect()

    def limpar_campos(self):
        for campo in self.campos.values():
            campo.clear()