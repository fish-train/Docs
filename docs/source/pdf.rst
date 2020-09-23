**********
Сборка PDF
**********

Подготовка к работе
===================

#. Установите `MikTex <https://docs.miktex.org/>`_.
#. Установите `ActiveState Perl <https://www.activestate.com/products/perl/downloads/>`_.
#. Установите пакет latexmk.
#. Установите пакеты, которые предлагает MikTex.
#. В файле conf.py раскомментируйте параметр latex_documents:

.. code-block:: python

    latex_documents = [
   ('index', 'sphinx-test.tex', u'Sphinx и reStructuredText. Учебный проект',
    u'fish-train', 'manual'),]

Создание PDF-файлов
===================

.. code-block:: bash

    make latexpdf

Выходные файлы размещаются в папке build/latex/.

..
	Создание PDF-файлов. 2 способ
	=============================

	#. Перейдите в папку docs.
	#. Сгенирируйте TEX-файл:

	   .. code-block:: bash

	      sphinx-build -b latex source build/latex

	#. Перейдите в папку build/latex.
	#. Сгенирируйте PDF-файл:

	   .. code-block:: bash

	      pdflatex sphinx-test.tex

	#. Сгенирируйте оглавление:

	   .. code-block:: bash

	      makeindex sphinx-test.idx

	#. Повторно сгенирируйте PDF-файл:

	   .. code-block:: bash

	      pdflatex sphinx-test.tex

Ссылки на дополнительные материалы
==================================

* `Options for LaTeX output <https://www.sphinx-doc.org/en/master/usage/configuration.html#latex-options>`_ 
* `LaTeX customization <https://www.sphinx-doc.org/en/master/latex.html>`_ 
* `Генерация в формат LaTeX <https://sphinx-ru.readthedocs.io/ru/latest/sphinx.html#latex>`_ 
* `LaTeX Templates <https://www.latextemplates.com/>`_
* `Gallery — Technical Manual <https://ru.overleaf.com/gallery/tagged/manual>`_
* `MiKTeX Manual <https://docs.miktex.org/manual/>`_
* `Как сделать генерацию LaTeX и PDF в Sphinx <https://habr.com/ru/post/328182/>`_
