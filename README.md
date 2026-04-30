# NT_Sabados1_VaxMinder

Proyecto integrador de nuevas tecnologías para simular, transformar y limpiar datos de vacunación.

## Requisitos

- Python 3.11 o superior
- Entorno virtual recomendado

## Instalación

Desde la raíz del proyecto:

```powershell
python -m venv env
env\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

> Si usas `bash` o `zsh` en Windows con WSL, reemplaza `env\Scripts\Activate.ps1` por `source env/bin/activate`.

## Ejecución

```powershell
python main.py
```

## Archivos importantes

- `main.py` - punto de entrada principal del proyecto
- `requirements.txt` - dependencias necesarias
- `.gitignore` - excluye el entorno virtual `env/`

## Notas

Este repositorio ya excluye el entorno virtual local, por lo que solo debes subir el código fuente y `requirements.txt` a GitHub.
