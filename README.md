# ERP Funilaria (Django)

Este repositório contém a base de um ERP para funilaria automotiva feito em **Python + Django**.
Ele já vem com módulos essenciais para cadastro de clientes, veículos, ordens de serviço,
estoque e financeiro.

## Módulos criados

- **Clientes**: cadastro de pessoas físicas/jurídicas.
- **Veículos**: vínculo do veículo ao cliente.
- **Serviços**: ordens de serviço e status do trabalho.
- **Estoque**: peças, entradas e saídas.
- **Financeiro**: faturas e pagamentos.

## Como rodar localmente

1. Crie e ative um ambiente virtual.
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Rode as migrações (a partir da pasta do projeto, onde está o `manage.py`):
   ```bash
   python manage.py migrate
   ```
4. Crie um superusuário:
   ```bash
   python manage.py createsuperuser
   ```
5. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```

Acesse o admin em `http://127.0.0.1:8000/admin/`.

## Importação automática de orçamentos aprovados (PDF)

1. Crie uma pasta chamada `Orçamentos` na raiz do projeto.
2. Coloque os PDFs aprovados nessa pasta.
3. Execute o comando abaixo para importar:
   ```bash
   python manage.py import_orcamentos --path "Orçamentos"
   ```

O importador soma todos os valores encontrados com o texto **"Total Aprovado"** (ex.: quando houver complemento),
captura **placa**, **veículo**, **CNPJ** e cria a OS com o **valor total aprovado**.

## Passo a passo no Windows (cmd)

1. Entre na pasta do projeto (onde está o `manage.py`):
   ```bat
   cd C:\ERPfunilaria
   ```
2. Crie o ambiente virtual:
   ```bat
   py -m venv venv
   ```
3. Ative o ambiente virtual:
   ```bat
   venv\Scripts\activate
   ```
4. Instale o Django e dependências:
   ```bat
   pip install -r requirements.txt
   ```
5. Rode as migrações:
   ```bat
   python manage.py migrate
   ```
6. Inicie o servidor:
   ```bat
   python manage.py runserver
   ```

## Estrutura esperada do projeto

Na pasta do projeto você deve ter algo parecido com:

```
ERPfunilaria/
├─ manage.py
├─ requirements.txt
├─ README.md
├─ apps/
└─ erpfunilaria/
   ├─ __init__.py
   ├─ settings.py
   ├─ urls.py
   ├─ wsgi.py
   └─ asgi.py
```

Se **`settings.py`, `urls.py`, `wsgi.py` ou `__init__.py` estiverem fora da pasta `erpfunilaria/`**, o Django não consegue importar o módulo e vai aparecer o erro:
`ModuleNotFoundError: No module named 'erpfunilaria'`.

Para corrigir, crie a pasta `erpfunilaria` e mova esses arquivos para dentro dela, garantindo que o caminho fique `erpfunilaria/settings.py`, `erpfunilaria/urls.py`, etc.

## Solução de problemas

- **Erro `ModuleNotFoundError: No module named 'erpfunilaria'`**: verifique se você está executando o comando dentro da pasta do projeto (onde está o `manage.py`). O `manage.py` já adiciona a pasta atual ao `PYTHONPATH` para evitar esse problema.
- **Erro `ModuleNotFoundError: No module named 'django'`**: seu ambiente virtual não está ativo ou o Django não foi instalado. Ative o `venv` e execute `pip install -r requirements.txt`.
- **Erro `ModuleNotFoundError: No module named 'apps.services'`**: confirme que existe o arquivo `apps/__init__.py` e que a pasta `apps/` fica no mesmo nível do `manage.py`.
