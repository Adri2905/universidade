# Projeto Universidade

Modelagem em Orientação á Objetos das entidades alunos, cursos e tumar

## Casos de usos
```mermaid
flowchart LR
    Usuario([Secretaria])

    UC1((Cadastrar Alunos))
    UC2((Editar Alunos))
    UC3((Transferir Alunos))

    Usuario --> UC1
    Usuario --> UC2
    Usuario --> UC3
```

## Diagrama de Classes
```mermaid
classDiagram
    class Aluno{
        -nome
        -email
        -cpf
        -telefone
        -endereço
        -matricula
        + cadastrar()
        + editar()
        + trasferir()
    }
```

## Dependências
- **VsCode**: IDE (Interface de Desenvolvimento)
- **Mermaid**:Lingagem para confecção em documentos MD (Mark Down)

- **Material Icon Theme**: Tema para colorir as pastas.
- **Git Lens**: Interface grafica para o versionamento git integrado ao VsCode.