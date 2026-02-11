from modulos.aluno import Aluno
from modulos.mysql import MySQL

banco = MySQL()

banco.connect()


aluno = Aluno (
    "José Maria",
    "josemaria@gmail.com",
    "12345678912",
    "031998920888",
    "Rua jose gomes ferreira,183"
    )

query = aluno.cadastrar()
#print(query)

banco.execute_query(query)

banco.disconnect()