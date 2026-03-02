from modulos.mysql import MySQL
from modulos.aluno import Aluno


from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox
)


class cadastrar():
    def __init__(self, app):
        self.app = app
        self.janela = QWidget()
        self.layout = QVBoxLayout()
        self.banco = MySQL()

        self.campos = {}

        self.configurar_janela()
        self.criar_componentes()

    def configurar_janela(self):
        self.janela.setWindowTitle("Cadastrar Aluno")

        # 🔹 Redimensionamento proporcional à tela
        screen = self.app.primaryScreen()
        tamanho_tela = screen.availableGeometry()

        largura = int(tamanho_tela.width() * 0.4)
        altura = int(tamanho_tela.height() * 0.6)

        self.janela.resize(largura, altura)
        self.janela.setMinimumSize(400, 300)

        self.janela.setLayout(self.layout)

    def criar_componentes(self):
        componentes = {
            "nome": "Digitar seu nome:",
            "email": "Digitar seu email:",
            "cpf": "Digitar seu cpf:",
            "telefone": "Digitar seu telefone:",
            "endereco": "Digitar seu endereco:"
        }

        for chave, texto in componentes.items():
            label = QLabel(texto)
            campo = QLineEdit()

            self.layout.addWidget(label)
            self.layout.addWidget(campo)

            self.campos[chave] = campo

        botao_cadastro = QPushButton("Cadastrar")
        self.layout.addWidget(botao_cadastro)

        botao_cadastro.clicked.connect(self.cadastrar)

    # 🔹 MÉTODO DE VALIDAÇÃO SEPARADO
    def validar_campos(self):
        nome = self.campos["nome"].text().strip()
        email = self.campos["email"].text().strip()
        cpf = self.campos["cpf"].text().strip()
        telefone = self.campos["telefone"].text().strip()
        endereco = self.campos["endereco"].text().strip()

        if not nome:
            QMessageBox.warning(self.janela, "Erro", "O nome é obrigatório.")
            return False

        if not email or "@" not in email:
            QMessageBox.warning(self.janela, "Erro", "Email inválido.")
            return False

        if not cpf or not cpf.isdigit() or len(cpf) != 11:
            QMessageBox.warning(self.janela, "Erro", "CPF deve conter 11 números.")
            return False

        if not telefone or not telefone.isdigit():
            QMessageBox.warning(self.janela, "Erro", "Telefone deve conter apenas números.")
            return False

        if not endereco:
            QMessageBox.warning(self.janela, "Erro", "Endereço é obrigatório.")
            return False

        return True

    def cadastrar(self):

        # 🔹 Valida antes de inserir no banco
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

            QMessageBox.information(
                self.janela,
                "Sucesso",
                "Aluno Cadastrado!"
            )

            self.limpar_campos()

        except Exception as e:
            QMessageBox.critical(
                self.janela,
                "Erro",
                f"Erro ao cadastrar: {e}"
            )

        finally:
            self.banco.disconnect()

    def limpar_campos(self):
        for campo in self.campos.values():
            campo.clear()


