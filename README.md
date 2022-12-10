# Django Rest Framework (DRF)

Es un framework de desarrollo web para Django que permite construir APIs RESTful de forma rápida y sencilla.

## Pasos para crear un proyecto con DRF

- Crear un entorno virtual con Python

```bash
virtualenv env
```

- Activar el entorno virtual

MacOS/Linux

```bash
source env/bin/activate
```

Windows

```bash
env\Scripts\activate
```

- Instalar Django

```bash
pip install django
```

- Crear un proyecto con Django

```bash
django-admin startproject todoapi .
```

- Instalar Django Rest Framework

```bash
pip install djangorestframework
```

- Creamos una aplicación

```bash
python manage.py startapp tasks
```

- Agregamos la aplicación a nuestro proyecto y tambien agregamos el framework de DRF

|- *settings.py*

```python
INSTALLED_APPS = [
    ...,
    'rest_framework',
    'tasks.apps.TasksConfig',
]
```
