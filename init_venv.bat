@echo off

set "pasta=ambiente-dev"

if not exist "%pasta%" (
    echo Criando ambiente virtual...
    python -m venv "%pasta%"
) 

call "%pasta%"\Scripts\activate

python -m pip install --upgrade pip

call pip install -r requirements.txt

cls

cmd



