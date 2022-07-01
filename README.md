# next20221-t11-envio-automatizado-mensagem
Envio automatizado de mensagens por e-mail


Contexto

Em um sistema de gerenciamento de projetos existe a necessidade de envio de mensagens por e-mail para finalidades diversas, tais como informe de agendamento de reuniões, notificação aproximação de prazos e possivelmente validação de endereços de e-mail por parte de usuários. Os usuários deste sistema podem não fazer parte de uma mesma instituição.


Objetivo

Implementar uma API REST que possibilite cadastrar usuários e gerenciar usuários (CRUD) e o envio de mensagens pré-formatadas (notificações de prazos e validação de endereço de e-mail) ou não para usuários cadastrados no sistema.

Referências

https://spring.io/guides/tutorials/rest/
https://flask.palletsprojects.com
https://www.mailgun.com/

### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
[Git](https://git-scm.com)

É bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/).

Qualquer banco de dados com compatibilidade com o [SQLAchelmy](https://sqlalchemy.org/) pode ser utilizado.

### Rodando o Back End (servidor)

- Clone esse repositório:

  ```$ git clone <https://github.com/next-cesar-school/next20221-t11-envio-automatizado-mensagem.git>```

- Crie uma variável de ambiente para criação do Banco de Dados: 

  ```DATABASE_URL = mysql://login:senha@localhost:3306/nomeDoBancoDeDados (Exemplo com MySQL)```

- Instale as dependências:

  ```$ pip install -r requirements.txt```

- Execute a aplicação:
 
  ```$ python3 app.py```


### Rotas da API


- Rota ```/user``` (método ```GET```): Retorna todos usários cadastrados na API

- Rota ```/user/id``` (método ```GET```): Retorna um usário cadastrado na API baseado no ```id```

- Rota ```/user``` (método ```POST```): Cria um cadastro de usuário na API

- Rota ```/user/id``` (método ```PUT```): Atualiza um cadastro de usuário na API baseado no ```id```

- Rota ```/user/id``` (método ```DELETE```): Deleta um cadastro de usuário na API baseado no ```id```
  
- Rota ```/sendmail``` (método ```POST```): Envia um email ```pré-definido``` para os usuários cadastrados na API
  
- Rota ```/sendcustommail``` (método ```POST```): Envia um email ```personalizado (subject/message)``` para os usuários cadastrados na API
