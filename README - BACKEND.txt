=======================================================================================
AIII CALICA, segue ai o que você tem que fazer pra rodar os projetinhos do backend
=======================================================================================

BACKEND:

*Depois que você baixou o projeto na pasta backend abre o CMD pelo caminho do explorer

*Com o CMD aberto digita os comandos: 
"cd venv"
"cd scripts"
"activate"
Pressiona o enter

*Com a venv ativada digita os comandos:
"cd.."
"cd.."
"pip install -r requirements.txt"

_______________________________________________________
Depois disso processo começa as configurações no código

Nomes importantes: backend -> nome do projeto / api -> nome da aplicação

Faz esses passos que não tem erro:

--- Cria as suas tabelas, no git dentro de models.py que esta na pasta da aplicação, exemplo
de models no git.

--- Cria agora um arquivo chamado "serializers.py" dentro da aplicação: depois disso
so ver no git o exemplo de como ajustar este arquivo

--- Dentro de views.py dentro da aplicação, configure o código de exemplo que tem no git
obs: leia as linhas 9 a 11 do código no git

--- Dentro da aplicação cria um arquivo chamado "urls.py", configure de acordo com o git
obs: leia a linha 6 do código no git

--- Agora no arquivo de "admin.py" na pasta da aplicação, configure os objetos para aparecerem
no admin do django
obs: leia a linha 4 do código no git

--- Nas "urls.py" da pasta do PROJETO, insira a linha 24 do código no git, mas lembre-se do nome
da sua aplicação.

_______________________________________________________
Feito essas configurações, utilize:

"py manage.py makemigrations"
"py manage.py migrate"

Se tudo ocorreu bem, as tabelas foram criadas com sucesso

Para criar um superuser utilize:
"py manage.py createsuperuser"

Depois disso tudo: "py manage.py runserver"

Para testar a parte da api, utilize na url do navegador:

"localhost:8000/nome_da_url_que_você_definiu"

****************** Qualquer coisa da um berrão na sala =) ******************



