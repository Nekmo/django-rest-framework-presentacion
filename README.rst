.. image:: https://raw.githubusercontent.com/Nekmo/django-rest-framework-presentacion/master/logo.png
    :width: 100%

|

.. image:: https://img.shields.io/github/workflow/status/Nekmo/django-rest-framework-presentacion/Build.svg?style=flat-square&maxAge=2592000
  :target: https://github.com/Nekmo/django-rest-framework-presentacion/actions?query=workflow%3ABuild
  :alt: Latest CI build status


===============================================
Construyendo APIs con **Django Rest Framework**
===============================================

Presentación para `Python Málaga <https://www.meetup.com/es-ES/python_malaga/>`_ el día 25 de febrero 2021. Puedes
utilizar esta misma presentación, íntegra o con modificaciones para cualquiera de los usos descritos en la licencia
MIT adjunta en este proyecto.

La presentación está `disponible online <https://nekmo.github.io/django-rest-framework-presentacion/>`_ ya compilada
para su visualización.

Para compilar desde el código fuente se requiere Python 3 instalado, estando probado sólo bajo Python 3.9. Se
recomienda ejecutar los siguientes pasos en un
`virtualenv <https://nekmo.com/es/blog/python-virtualenvs-y-virtualenvwrapper/>`_::

    # Clonar proyecto
    git clone https://github.com/Nekmo/django-rest-framework-presentacion.git
    cd django-rest-framework-presentacion
    # Instalar dependencias
    pip install -r requirements.txt
    # Compilar ficheros de estilos
    sassc _static/theme.scss _static/theme.css
    # Compilar presentación
    make revealjs
    # Copiar ficheros faltantes de Revealjs (requerido por usar versión modificada)
    wget https://files.pythonhosted.org/packages/18/b2/ed4468b5a6e2ef423cddd9ad018e28daf9992df26dd96517e40a10949ed8/sphinx-revealjs-1.0.1.tar.gz
    tar -zxvf sphinx-revealjs-1.0.1.tar.gz
    mv sphinx-revealjs-1.0.1/sphinx_revealjs/themes/sphinx_revealjs/static/revealjs4 _build/revealjs/_static/

Tras la compilación puede verse los ficheros resultantes en el directorio ``_build``.

Proyecto demo
=============
Con esta presentación se incluye un proyecto de demostración, el cual puede ejecutarse de forma fácil usando Docker y
Docker-compose. Para ello, ejecutar::

    # Clonar proyecto
    git clone https://github.com/Nekmo/django-rest-framework-presentacion.git
    cd django-rest-framework-presentacion
    # Levantar servicios nginx y gunicorn del docker-compose. Escuchará en el puerto 80.
    docker-compose up -d

Si el puerto ``80`` esta disponible en la máquina, el proyecto estará disponible en `localhost <http://localhost/>`_.

También puede ejecutarse el proyecto en modo desarrollo en la máquina, recomendándose la instalación en un virtualenv.
Para ello::

    # Clonar proyecto
    git clone https://github.com/Nekmo/django-rest-framework-presentacion.git
    cd django-rest-framework-presentacion
    # Acceder al directorio de la demo
    cd demo_project
    # Instalar dependencias
    pip install -r requirements.txt
    # Crear y rellenar base de datos
    python manage.py migrate --no-input
    python manage.py import_pokedex
    # Inicializar el proyecto en modo desarrollo escuchando en puerto 8000
    python manage.py runserver 8000

Tras la instalación y configuración el proyecto pasará a estar disponible en
`localhost en el puerto 8000 <http://localhost:8000/>`_.

Copyright
=========
Licencia MIT. Ver fichero ``LICENSE.txt``.

Nekmo 2021.

