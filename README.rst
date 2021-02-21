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

    pip install -r requirements.txt
    sassc _static/theme.scss _static/theme.css
    make revealjs
    wget https://files.pythonhosted.org/packages/18/b2/ed4468b5a6e2ef423cddd9ad018e28daf9992df26dd96517e40a10949ed8/sphinx-revealjs-1.0.1.tar.gz
    tar -zxvf sphinx-revealjs-1.0.1.tar.gz
    mv sphinx-revealjs-1.0.1/sphinx_revealjs/themes/sphinx_revealjs/static/revealjs4 _build/revealjs/_static/

Tras la compilación puede verse los ficheros resultantes en el directorio ``_build``.

