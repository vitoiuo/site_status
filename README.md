# Site Status Checker

Um app que podemos cadastrar outros sites que temos publicado, dai teremos um serviço que a cada 5 ou 10min irá verificar se nossos sites cadastrados estão retornando código de sucesso (Exemplo 200), em caso de um dos nossos sites ficar fora do ar (404, 500), devemos receber uma notificação ou email

## Setup inicial

- Clone este repositório
- Crie uma virtualenv com o Python na versão 3.8.10
- Se estiver contribuindo com o projeto, instale as dependências existentes em dev-requirements.txt, se não, execute o processo com requirements.txt:
  pip install -r <arquivo-de-dependencias>

## Rodando o projeto na sua máquina

- Crie uma .env na raiz do seu porjeto com usuário e senha para o banco
- Suba um conatiner postgres com 'docker compose up'
- Bota esse bixo pra rodar, com '/.manage.py runserver' ou 'python3 manage.py runserver'
