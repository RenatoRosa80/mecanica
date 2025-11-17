🛠️ Sistema Gerencial Mecânica San Louis
Sistema completo de gestão para oficina mecânica desenvolvido em Django, com interface moderna e responsiva.

✨ Funcionalidades
📋 Módulos Principais
Clientes - Cadastro completo com CPF, contato e endereço

Veículos - Gestão de frota e veículos dos clientes

Serviços - Controle de ordens de serviço e manutenções

Estoque - Gerenciamento de peças e produtos

Fornecedores - Cadastro de fornecedores e compras

Financeiro - Controle financeiro e fluxo de caixa

Relatórios - Relatórios gerenciais e analytics

🎯 Características Técnicas
Framework: Django 5.2.8

Frontend: Tailwind CSS + JavaScript

Database: SQLite (dev) / PostgreSQL (prod)

Deploy: Render.com

Arquivos Estáticos: WhiteNoise

Segurança: CSRF protection, XSS protection

🚀 Como Executar
Pré-requisitos
Python 3.11+

Django 5.2.8

Dependências do requirements.txt

🔧 Instalação Local
bash
# Clone o repositório
git clone https://github.com/RenatoRosa80/mecanica.git
cd mecanica

# Crie ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Instale dependências
pip install -r requirements.txt

# Execute migrações
python manage.py migrate

# Crie superusuário
python manage.py createsuperuser

# Execute o servidor
python manage.py runserver
🌐 Deploy em Produção
O sistema está configurado para deploy automático no Render.com:

Build Command:

bash
pip install -r requirements.txt && python manage.py collectstatic --noinput
Start Command:

bash
python -m gunicorn mecanica.wsgi:application --bind 0.0.0.0:$PORT
🏗️ Estrutura do Projeto
text
mecanica/
├── core/                 # App principal
├── clientes/            # Gestão de clientes
├── veiculos/            # Controle de veículos
├── servicos/            # Ordens de serviço
├── estoque/             # Gerenciamento de estoque
├── fornecedores/        # Cadastro de fornecedores
├── financeiro/          # Controle financeiro
├── relatorios/          # Relatórios gerenciais
├── static/
│   ├── css/            # Estilos customizados
│   └── js/             # Scripts JavaScript
├── templates/           # Templates base
└── mecanica/
    ├── settings.py      # Configurações Django
    └── urls.py         # URLs principais
🔐 Segurança
✅ CSRF Protection

✅ XSS Protection

✅ HTTPS em produção

✅ Validação de formulários

✅ Autenticação de usuários

✅ Permissões por grupo

📊 Tecnologias Utilizadas
Backend
Django 5.2.8 - Framework web

Django REST Framework - APIs (futuro)

WhiteNoise - Servir arquivos estáticos

Gunicorn - Servidor WSGI

dj-database-url - Configuração de banco

Frontend
Tailwind CSS - Framework CSS utility-first

JavaScript Vanilla - Interatividade

HTML5 - Estrutura semântica

Banco de Dados
SQLite - Desenvolvimento

PostgreSQL - Produção (Render.com)

Deploy & DevOps
Render.com - Plataforma de deploy

Git - Controle de versão

GitHub - Repositório

🎨 Interface
Design System
Cores: Verde corporativo (#16a34a)

Tipografia: Sistema de fontes nativo

Layout: Dashboard responsivo

Componentes: Cards, tabelas, formulários

Responsividade
📱 Mobile-first approach

💻 Tablets e desktops

🖥️ Telas grandes

🔄 Fluxo de Trabalho
Cadastro de Cliente → Dados completos com validação de CPF

Registro de Veículo → Vinculação com cliente

Ordem de Serviço → Serviços e peças utilizadas

Controle Financeiro → Pagamentos e fluxo de caixa

Relatórios → Análise e tomada de decisão

📈 Próximas Funcionalidades
API REST para integração

App mobile companion

Notificações por email

Integração com pagamentos

Dashboard analytics avançado

Sistema de agendamento

🤝 Contribuição
Fork o projeto

Crie uma branch para sua feature (git checkout -b feature/AmazingFeature)

Commit suas mudanças (git commit -m 'Add some AmazingFeature')

Push para a branch (git push origin feature/AmazingFeature)

Abra um Pull Request

📝 Licença
Este projeto está sob licença MIT. Veja o arquivo LICENSE para mais detalhes.

👨‍💻 Desenvolvedor
Renato Rosa

GitHub: @RenatoRosa80

Email: renatto.rfilho@yahoo.com

🔗 Links Úteis
🌐 Aplicação Online

📁 Repositório GitHub

🐛 Reportar Bug

Mecânica San Louis © 2025 - Sistema de Gestão Completo para Oficinas Mecânicas
























___________________________________________________________________________________--
Fixed Problems
__________________________________________________________________________________-_
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
