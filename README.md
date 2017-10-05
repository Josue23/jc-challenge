# Cadastro de uma agência de empregos
## Considere dois usuários. Requerer cadastro com email e senha.
Empresa deve criar uma (ou várias) vagas.

Candidato deve se candidatar a uma (ou mais) vagas.

A vaga que a empresa vai criar deve ter:

Nome da vaga

Faixa salarial - valor mínimo e máximo

Experiência: exemplo, 3 anos de experiência

Escolaridade

Distância máxima entre casa e trabalho

O candidato deve informar:

Pretensão salarial

Experiência

Escolaridade

Distância

# jc-challenge
## Como rodar a aplicação

git clone https://github.com/Josue23/jc-challenge.git

cd jc-challenge

virtualenv .venv -p python2

source .venv/bin/activate

pip install -r requirements.txt

./manage.py makemigrations

./manage.py migrate

./manage.py createsuperuser --username="admin"

./manage.py runserver
