from modulos.mysql import MySQL
from modulos.aluno import Aluno


import sys

from PySide6.QtWidgets import(

    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton
)

def cadastro():
    aluno = Aluno(
        campo_nome.text(),
        campo_email.text(),
        campo_cpf.text(),
        campo_telefone.text(),
        campo_endereco.text(),
    )
    
    banco = MySQL()
    banco.connect()
    
    aluno.cadastrar(banco)
    banco.disconnect()

app = QApplication(sys.argv)

janela = QWidget()
janela.setWindowTitle("Primeiro Janela")
janela.resize(1200, 600)


layout = QVBoxLayout()

#Componentes
lebal_nome= QLabel("Digite seu nome:")
campo_nome=QLineEdit()

lebal_email= QLabel("Digite seu email:")
campo_email= QLineEdit()

lebal_cpf= QLabel("Digite seu cpf:")
campo_cpf= QLineEdit()

lebal_telefone= QLabel("Digite seu telefone:")
campo_telefone= QLineEdit()

lebal_endereco= QLabel("Digite seu endereço:")
campo_endereco= QLineEdit()

botao= QPushButton("Cadastrar")

# Adicionar componentes à janela 
layout.addWidget(lebal_nome)
layout.addWidget(campo_nome)

layout.addWidget(lebal_cpf)
layout.addWidget(campo_cpf)

layout.addWidget(lebal_email)
layout.addWidget(campo_email)

layout.addWidget(lebal_telefone)
layout.addWidget(campo_telefone)

layout.addWidget(lebal_endereco)
layout.addWidget(campo_endereco)


layout.addWidget(botao)

janela.setLayout(layout)

botao.clicked.connect(cadastro)


janela.show()
sys.exit(app.exec())