.. Construyendo APIs con Django Rest Framework documentation master file, created by
   sphinx-quickstart on Wed Feb 17 01:02:49 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. This toctree is only to link examples.

.. toctree::
   :glob:
   :hidden:

   *

.. _intro:

===============================================
Construyendo APIs con **Django Rest Framework**
===============================================

Sobre mí
========

.. Buenas, soy Juan José Oyague, más conocido en las redes como Nekmo; y llevo media vida programando en Python,
   usando Django ya desde su versión 1.1. Así que no os puedo engañar...

**Nekmo**

*Django desde versión 1.1 (2009)*

.. image:: images/cara.svg
   :width: 200px

Django + Django Rest Framework
==============================

.. ... Me gusta Django, y Django Rest Framework (diapositiva corazón). Y espero conseguir haceros llegar un poco de mi
   pasión por estos dos frameworks, y de los motivos por los que llevo usándolos tanto tiempo. Vale, pero
   antes de llegar a mí Django Rest Framework, llego...

Django
======

.. Django. ¿Y qué es exactamente este framework?

Qué es
------

* Framework web
* Desarrollo rápido en Python
* Miles de módulos
* Muy escalable
* Gran soporte

.. Aquí no me puedo parar mucho, pero en resumen, Django es un framework web para el rápido desarrollo en Python, con
   miles de módulos, muy estable y con gran soporte. Seguramente, el más conocido y usado en Python.


Baterías incluidas
------------------

.. Y al igual que Python, tiene baterías incluidas para todo.

.. image:: images/batteries-included.*
   :width: 100%

Qué incluye
-----------

* ORM para base de datos
* Administración de sesiones
* Control de permisos
* Gestión de urls
* Middleware
* Caché
* envío de correos...
* Pero claro, no API Rest.

Django Rest Framework
=====================

.. ¿Recordáis que hemos dicho que tiene módulos para todo? Pues Django Rest Framework es uno de esos módulos.
   Se instala en prácticamente en 3 o 4 pasos, y listo para funcionar.

Framework para desarrollar APIs REST
------------------------------------

.. Pero espera... Django Rest Framework es un framework... ¿Y Django también es un framework?


Meta framework
--------------

(diapositiva meme meta).

.. Sí, Django Rest Framework es un framework dentro de otro framework web. Pero aún no saquéis las antorchas.


Antorchas
---------

(diapositiva antorchas Simpsons).

Django Rest Framework complementa
---------------------------------

.. Django Rest Framework aprovecha todo lo bueno de Django, y lo complementa. Si Django es un pastel

Pastel 1
--------
(diapositiva pastel)


.. Django Rest Framework es su guinda

Pastel 2
--------
(diapositiva pastel con guida).

.. ¿Y nadie quiere una guinda sin pastel, verdad?

Ejemplo web
===========

.. Además, nos construye una API REST muy vistosa y navegable y que nos mostrará el JSON resaltado de nuestros objetos
   de la base de datos.

Formulario
----------

.. No sólo eso, sino que nos construtye formularios para crear nuevos objetos. ¿Pero cómo funciona todo esto?


Estructura
==========
(diapositiva: serializers, viewsets, routers).

.. Si Django Rest Framework me gusta, no es sólo por sus opciones o su modo web, sino porque a diferencia de otros
   módulos que hacen lo mismo, entiende perfectamente la filosofía de Django, y ello se ve en su estructura base.

Serializers
===========

**¿Qué son?**

.. Vale, empecemos por los serializers. ¿Y qué hacen los serializers?

Los serializers, serializan
---------------------------

*J. Oyague, 2021.*

.. Los serializers, serializan. Juan José Oyague, 2021. Vale, ahora en serio.

Convertir la entrada
--------------------

.. Los serializers, son los responsables de convertir la entrada de datos, vamos, lo que mete el usuario a través de la
   API, en un objeto en Python, que normalmente servirá para crear o actualizar un objeto en la base de datos

Convertir la salida
-------------------

.. También hacen lo mismo pero a la inversa: convierten el objeto a una salida compatible, para que nos entendamos, un
   diccionario, y devolverlo al usuario.


Convert sections from reStructuredText directly
===============================================

Adjust section structure
------------------------

From:

.. code-block:: rest

    Title
    =====

    First section
    -------------

        Content 1
        ^^^^^^^^^

        Content 2
        ^^^^^^^^^

To:

.. code-block:: html

    <section>
        <h1>Title</h1>
    </section>
    <section>
        <section>
            <h2>First section</h2>
        </section>
        <section>
            <h3>Content 1</h3>
        </section>
        <section>
            <h3>Content 2</h3>
        </section>
    </section>


reStructuredText comments are used as speaker notes
---------------------------------------------------

From:

.. code-block:: rest

    .. This is comment in reStructuredText

To:

.. code-block:: html

    <section>
      <aside class="notes">
        This is comment in reStructuredText
      </aside>
    </section>

code-block as reveal.js code block
----------------------------------


Directive for meta of section
=============================

Inject background color
-----------------------

.. revealjs_section::
    :data-background-color: #009900

.. code-block:: rest

    .. revealjs_section::
        :data-background-color: #009900

Inject background image
-----------------------

.. revealjs_section::
    :data-background-image: _static/icon-attakei.jpg
    :data-background-size: contain

.. code-block:: rest

    .. revealjs_section::
        :data-background-image: _static/icon-attakei.jpg
        :data-background-size: contain

Inject background video
-----------------------

.. revealjs_section::
    :data-background-video: https://s3.amazonaws.com/static.slid.es/site/homepage/v1/homepage-video-editor.mp4,https://s3.amazonaws.com/static.slid.es/site/homepage/v1/homepage-video-editor.webm

.. code-block:: rest

    .. revealjs_section::
        :data-background-video: https://s3.amazonaws.com/static.slid.es/site/homepage/v1/homepage-video-editor.mp4,https://s3.amazonaws.com/static.slid.es/site/homepage/v1/homepage-video-editor.webm

Inject background iframe
------------------------

.. revealjs_section::
    :data-background-iframe: https://slides.com
    :data-background-interactive:

.. code-block:: rest

    .. revealjs_section::
        :data-background-iframe: https://slides.com
        :data-background-interactive:


Transition settings(before)
---------------------------

.. revealjs_section::
    :data-transition: none

.. code-block:: rest

    .. revealjs_section::
        :data-transition: none

Transition settings(after)
--------------------------

.. revealjs_section::
    :data-transition: fade

.. code-block:: rest

    .. revealjs_section::
        :data-transition: fade

Background image transition
---------------------------

.. revealjs_section::
    :data-background-image: _static/icon-attakei.jpg
    :data-background-size: contain
    :data-background-transition: zoom

.. code-block:: rest

    .. revealjs_section::
        :data-background-image: _static/icon-attakei.jpg
        :data-background-size: contain
        :data-background-transition: zoom


Keep title without duplicated written
-------------------------------------

First section

.. revealjs_break::

Second section

.. code-block:: rest

    .. revealjs_break::


.. revealjs_break::
    :notitle:

Third section.

You can hide section title

.. code-block:: rest

    .. revealjs_break::
        :notitle:

Support features
================

Fragments
---------

This is support fragment with groups.

.. revealjs_fragments::

   * First
   * Second
   * Third

Plugins
-------

bundled plugins can use just write ``conf.py``

.. code-block:: python

    revealjs_script_plugins = [
        {
            "name": "RevealNotes",
            "src": "revealjs4/plugin/notes/notes.js",
        },
    ]

This is used `RevealNotes` plugin, Please press `S` key to try it!

Usage
=====

Installation
------------

You can install from PyPI.

.. code-block:: bash

    $ pip install sphinx-revealjs

Configure
---------

Edit `conf.py` to use this extension

.. code-block:: python

    extensions = [
        "sphinx_revealjs",
    ]

Write source
------------

Write plain reStructuredText

.. code-block:: rest

    My Reveal.js presentation
    =========================

    Agenda
    ------

    * Author
    * Feature


    Author: Who am I
    ================

    Own self promotion

    Content
    =======

Build
-----

This extension has custom builder name ``revealjs`` .
If you make docs as Reveal.js presentation, you call ``make revealjs``.

.. code-block:: bash

    $ make revealjs

This presentation is made from `source <https://github.com/attakei/sphinx-revealjs/blob/master/demo/revealjs4/index.rst>`_.

Other examples
==============

Within this pages
-----------------

* :doc:`example-background-only-section`

Enjoy writing reST as presentation
==================================

Please star!

.. raw:: html

    <!-- Place this tag where you want the button to render. -->
    <a class="github-button" href="https://github.com/attakei/sphinx-revealjs" data-icon="octicon-star" data-size="large" data-show-count="true" aria-label="Star attakei/sphinx-revealjs on GitHub">Star</a>
    <!-- Place this tag in your head or just before your close body tag. -->
    <script async defer src="https://buttons.github.io/buttons.js"></script>
