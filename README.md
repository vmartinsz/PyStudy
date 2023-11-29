<h1 align="center">:file_cabinet: Exemplo de README.md</h1>

## :memo: Descrição
O PyStudy é uma plataforma inovadora projetada para simplificar e otimizar a gestão de atividades escolares, proporcionando aos alunos uma experiência eficiente e organizada. Desenvolvido com foco na praticidade e usabilidade, o PyStudy é a ferramenta perfeita para estudantes que desejam manter controle sobre suas tarefas acadêmicas.

## :books: Funcionalidades
* O PyStudy oferece uma interface intuitiva que permite aos alunos adicionar e visualizar todas as suas atividades escolares em um único local. Com categorias personalizáveis, os alunos podem organizar suas tarefas por disciplina.

## :wrench: Tecnologias utilizadas

- MySQL Connector Python:
  Biblioteca para conectar e interagir com um banco de dados MySQL. Utilizado para implementar as operações CRUD (Create, Read, Update, Delete) relacionadas ao armazenamento e recuperação de dados das atividades escolares

- Flask:
  Um framework web leve e poderoso para construção rápida de aplicativos web. O Flask foi utilizado para criar a estrutura do servidor web e gerenciar as rotas necessárias para o funcionamento do PyStudy.
  
- Flask-Session:
  Extensão do Flask para manipulação de sessões. Usado para gerenciar informações de sessão, permitindo que os usuários mantenham seu estado de autenticação durante a navegação na aplicação.

- smtplib e email:
  Bibliotecas padrão do Python para enviar e-mails. Essenciais para a implementação de funcionalidades relacionadas a notificações e lembretes, garantindo uma comunicação eficiente com os usuários.

- Render_template (Flask):
    Função do Flask que permite a renderização de templates HTML. Fundamental para a construção de páginas dinâmicas e interativas na aplicação web.
    
## :rocket: Rodando o projeto
Para rodar o repositório é necessário clonar o mesmo, dar o seguinte comando para iniciar o projeto:
```
pip install -r requirements
python3 app.py
```

## :soon: Implementação futura

O projeto está em constante evolução, e algumas melhorias e adições estão planejadas para o futuro. Aqui estão algumas áreas que serão abordadas:

### Dockerização

Atualmente, o projeto ainda não foi dockerizado. A dockerização facilitará a implantação e distribuição do aplicativo, garantindo ambientes consistentes. Em breve, adicionaremos instruções sobre como empacotar o aplicativo em contêineres Docker para uma implantação mais eficiente.

Para executar o aplicativo em um contêiner Docker, você pode seguir os seguintes passos:

1. Criar a imagem Docker.
2. Executar o contêiner.

### Melhorias no Front-End

O front-end do aplicativo está em um estágio inicial, e sabemos que há espaço para melhorias significativas. Se você é apaixonado por design de interface do usuário e experiência do usuário, sua contribuição seria muito bem-vinda!

Alguns pontos que planejamos abordar incluem:

- Aprimoramento da interface de usuário para uma experiência mais intuitiva.
- Adição de recursos visuais atraentes.
- Otimização para dispositivos móveis e tablets.

Se você possui habilidades em design de front-end, ficaríamos felizes em receber suas sugestões e colaborações!

Fique à vontade para abrir problemas ou enviar solicitações de recebimento para contribuir com essas melhorias ou discutir outras ideias para o projeto.

## :handshake: Colaboradores
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/vmartinsz">
        <img src="https://avatars.githubusercontent.com/u/116663034?v=4" width="100px;" alt="Foto de Vitor Martins no GitHub"/><br>
        <sub>
          <b>vmartinsz</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

## :dart: Status do projeto
- Em andamento
