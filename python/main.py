from modulos.aluno import Aluno
from modulos.mysql import MySQL

banco = MySQL(
    '127.0.0.1',
    'root',
    '',
    'universidade'
)


banco.connect()


aluno = Aluno (
    "José Maria",
    "josemaria@gmail.com",
    "12345678912",
    "031998920888",
    "Rua jose gomes ferreira,183"
    )

query = aluno.cadastrar(banco)

banco.disconnect()