# mecanica
Car maintenance managment

fixing git problems:

# 1. Certifique-se de que tem todos os arquivos adicionados
git add .

# 2. Faça um commit
git commit -m "Final project version"

# 3. Force o push (se você tem certeza que quer substituir o remoto)
git push -u origin main --force


git log --oneline -3

for Render:

git commit -m "FIX: Configure ALLOWED_HOSTS and update requirements"

gunicorn

Build Command: (mantenha como está)

bash
pip install gunicorn && pip install -r requirements.txt
Start Command: (ALTERE PARA)

bash
python -m gunicorn mecanica.wsgi:application --bind 0.0.0.0:$PORT

# mecanica/settings.py
ALLOWED_HOSTS = [
    'mecanica-qbou.onrender.com',
    'localhost',
    '127.0.0.1',
    '.onrender.com',  # Permite todos subdomínios do Render
]


second option:

import os

ALLOWED_HOSTS = []


Mascara para cpf funcionar sem padrao:


// Máscara para CPF
document.addEventListener('DOMContentLoaded', function() {
    const cpfField = document.querySelector('#id_cpf');
    if (cpfField) {
        cpfField.addEventListener('input', function(e) {
            let value = e.target.value.replace(/\D/g, '');
            if (value.length <= 11) {
                value = value.replace(/(\d{3})(\d)/, '$1.$2');
                value = value.replace(/(\d{3})(\d)/, '$1.$2');
                value = value.replace(/(\d{3})(\d{1,2})$/, '$1-$2');
                e.target.value = value;
            }
        });
    }
});
</script>

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

ALLOWED_HOSTS.extend(['localhost', '127.0.0.1'])
