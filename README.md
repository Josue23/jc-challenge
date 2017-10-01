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
