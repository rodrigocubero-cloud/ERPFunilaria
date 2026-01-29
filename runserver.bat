@echo off
setlocal

if not exist venv\Scripts\activate (
    echo Ambiente virtual nao encontrado. Execute: py -m venv venv
    exit /b 1
)

call venv\Scripts\activate
python manage.py runserver
