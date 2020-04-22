***********
Сборка HTML
***********

Сайт с несколькими страницами
=============================

.. code-block:: bash

    make html

Выходные файлы размещаются в папке ``build/html/``.

Скрипт для локальной публикации сайта
-------------------------------------

.. literalinclude:: make_site.py
  :language: python
  :linenos:

Одностраничный сайт
===================

.. code-block:: bash

    make singlehtml

Выходные файлы размещаются в папке ``build/singlehtml/``.

Скрипт для локальной публикации одностраничного сайта
-----------------------------------------------------

.. literalinclude:: make_spage.py
  :language: python
  :linenos:

Ссылки о настройке сборки в HTML
================================

* `Генерация в формат HTML <https://sphinx-ru.readthedocs.io/ru/latest/sphinx.html#html>`_ 
* `HTML <https://www.sphinx-doc.org/en/master/usage/theming.html>`_ 
* `Options for HTML output <https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output>`_ 
* `Options for Single HTML output <https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-single-html-output>`_ 
* `HTML theming support <https://www.sphinx-doc.org/en/master/theming.html>`_ 
* `Sphinx Themes <https://sphinx-themes.org/>`_ 
