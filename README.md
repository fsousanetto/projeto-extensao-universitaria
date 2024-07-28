## Projeto de Extensão Universitária
### Gerenciament de Cadastro de Alunos

Bem-vindo ao repositório do Projeto de Extensão Universitária. Este projeto visa desenvolver um sistema de gerenciamento de cadastro de alunos em cursos, aulas de dança, artes marciais, cursinho pré-vestibular, dentre outras atividades para uma instituição local.

#### Sumário

- [Contexto](#contexto)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Uso](#uso)
- [Estrutura do Banco de Dados](#estrutura-do-banco-de-dados)
- [Contribuição](#contribuição)
- [Licença](#licença)

#### Contexto

Este projeto foi desenvolvido como parte de uma atividade de extensão universitária. O objetivo é proporcionar um sistema que auxilie uma instituição na organização e gerenciamento de seus alunos, cursos, matrículas, aulas e professores.

#### Estrutura do Projeto

O projeto está estruturado nas seguintes etapas:

1. **Planejamento**: Reunião inicial, análise de requisitos e definição do escopo.
2. **Modelagem Conceitual**: Identificação das entidades e relacionamentos, criação do Diagrama Entidade-Relacionamento (DER).
3. **Modelagem Lógica**: Conversão do DER para o modelo relacional, revisão com a equipe.
4. **Implementação Física**: Configuração do ambiente, criação das tabelas no banco de dados, inserção de dados de teste.
5. **Desenvolvimento de Mecanismos de Manipulação de Dados**: Criação de scripts SQL para inserção e consultas de dados.
6. **Testes e Validação**: Testes de integração e ajustes.
7. **Documentação e Treinamento**: Criação da documentação do sistema, treinamento para usuários finais.
8. **Implantação**: Migração para o ambiente de produção, monitoramento inicial.
9. **Encerramento**: Entrega da documentação final.

#### Requisitos

- PostgreSQL
- Ferramentas de modelagem (Draw.io, dbdiagram.io)
- Python (opcional, para prototipação)

#### Instalação

1. Clone o repositório:
   ```sh
   git clone https://github.com/fsousanetto/projeto-extensao-banco-de-dados.git
   cd projeto-extensao-banco-de-dados
   ```

2. Configure o PostgreSQL e crie o banco de dados conforme o script SQL fornecido no arquivo `db.sql`.

3. Execute os comandos SQL no PostgreSQL para criar as tabelas e inserir dados de teste.

4. Execute o comando `python3 app/controller.py` para rodar a interface.

#### Uso

O projeto pode ser usado para gerenciar:
- Cadastro de alunos
- Cursos oferecidos
- Matrículas de alunos nos cursos
- Aulas relacionadas aos cursos
- Professores e suas turmas

#### Estrutura do Banco de Dados

- **Student**: ID, Name, Date of Birth, CPF (Tax ID), Address, Phone, Email.
- **Course**: ID, Course Name, Description, Duration, Type (Dance, Martial Arts, Preparatory).
- **Enrollment**: ID, Student ID, Course ID, Enrollment Date.
- **Class**: ID, Course ID, Class Date, Start Time, End Time, Location.
- **Instructor**: ID, Name, Specialty, Phone, Email.
- **Class Group**: ID, Course ID, Instructor ID, Group Name, Schedule.

#### Contribuição

Contribuições são bem-vindas! Para contribuir:
1. Faça um fork do repositório.
2. Crie uma nova branch (`git checkout -b feature/nova-funcionalidade`).
3. Commit suas alterações (`git commit -m 'Adiciona nova funcionalidade'`).
4. Faça o push para a branch (`git push origin feature/nova-funcionalidade`).
5. Abra um Pull Request.

#### Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---
