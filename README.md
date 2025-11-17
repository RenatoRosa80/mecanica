# mecanica
Car maintenance managment

fixing git problems:

# 1. Certifique-se de que tem todos os arquivos adicionados
git add .

# 2. Faça um commit
git commit -m "Final project version"

# 3. Force o push (se você tem certeza que quer substituir o remoto)
git push -u origin main --force


for Render:

gunicorn

Build Command: (mantenha como está)

bash
pip install gunicorn && pip install -r requirements.txt
Start Command: (ALTERE PARA)

bash
python -m gunicorn mecanica.wsgi:application --bind 0.0.0.0:$PORT

ALLOWED HOST: 'mecanica-qbou.onrender.com',
    'localhost',
    '127.0.0.1',
