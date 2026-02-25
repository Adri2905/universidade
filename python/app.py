from modulos.mysql import MySQL
from modulos.aluno import Aluno


import sys

from PySide6.QtWidgets import(
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox
)
class TelaCadastro():
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.janela = QWidget()
        self.layout = QVBoxLayout()
        self.banco = MySQL()
        
        self.campos = {}
        self.configurar_janela ()
        self.criar_componentes()
    
    def configurar_janela(self): 
        
        self.janela.setWindowTitle("Cadastrar Aluno")
        # Adaptar redimensionamento para tamanho dinamico
        self.janela.resize(1200, 600)
        self.janela.setLayout(self.layout)
        
    def criar_componentes(self):
        componentes = {
            "nome":"Digitar seu nome:",
            "email": "Digitar seu email:",
            "cpf":"Digitar seu cpf:",
            "telefone":"Digitar seu telefone:",
            "endereco":"Digitar seu endereco:"
               
        }
        for chave, texto  in componentes.items():
            label = QLabel(texto)
            campo = QLineEdit()
            
            self.layout.addWidget(label)
            self.layout.addWidget(campo)
            
            self.campos[chave] = campo
            
        botao_cadastro = QPushButton("Cadatrar")
        self.layout.addWidget(botao_cadastro)
        
        botao_cadastro.clicked.connect(self.cadastrar)
        
    def cadastrar(self):
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
                "sucesso",
                "Aluno Cadastrado!"
            )
            self.limpar_campos()
            
        except Exception as e:
            QMessageBox.critical(
                self.janela,
                "Erro",
                f"Erro ao castrar: {e}"
            )
            
        finally:
            self.banco.disconnect()
    
    def limpar_campos(self):
        for campo in self.campos.values():
            campo.clear()


if __name__=="__main__":
    tela = TelaCadastro()
    tela.janela.show()
    
    sys.exit(tela.app.exec())
