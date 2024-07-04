# To-Do-List Django
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/andersonrodrigues14/To-Do-List/blob/main/LICENSE) 

# Sobre o projeto

Este To-Do-List é uma aplicação full stack web, desenvolvida em Django e Ajax com o instuito de deixar a aplicação mais dinâmica evitando refreshes de tela a cada interação do usuário" .

A aplicação consiste em um sistema para cadastro de tarefas e alteração dos seus status.

## Demonstração do Sistema

https://github.com/andersonrodrigues14/To-Do-List/assets/39199377/706b6c43-1ca5-4397-9c4a-109a8f269f52


# Tecnologias utilizadas
## Back end
- Django
  
## Front end
- HTML / CSS / JS
- Ajax

# Como executar o projeto


Pré-requisitos: Python instalado na máquina

```bash
# clonar repositório
git clone https://github.com/andersonrodrigues14/To-Do-List.git

# entrar na pasta do projeto e criar ambiente virtual
python -m venv .venv

# ativar o ambiente virtual
No Windowns -> .\.venv\Scripts\activate
MacOs/linux -> source .venv/bin/activate

# Instalar dependência do projetos presentes no requirements.txt
 pip install -r requirements.txt

# Descomentar configurações de banco de dados local em core/settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'), 
    }
}

# Criar super usuário para cadastrar status das tarefaz no admin do Django
python3 manage.py createsuperuser

# executar o projeto
python manage.py runserver

```

# Clonar repositório
```
git clone https://github.com/andersonrodrigues14/To-Do-List.git
```


# Autor

Anderson Almeida Rodrigues

https://www.linkedin.com/in/anderson-almeida-rodrigues-b30842186/
