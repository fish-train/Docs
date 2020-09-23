***********
Сборка DOCX
***********

.. _docx-preparation-label:

Подготовка к работе
===================

#. Установите `Расширение Docxbuilder <https://github.com/amedama41/docxbuilder>`_.
#. В файле conf.py добавьте:

   .. code-block:: bash

       extensions = ['docxbuilder']
#. В файле conf.py добавьте настройки документа:

   .. code-block:: python

       docx_documents = [
       ('index', 'docxbuilder.docx', {
            'title': project,
            'creator': author,
            'subject': 'A manual of docxbuilder',
        }, True),
       ]
       docx_style = 'path/to/custom_style.docx'
       docx_pagebreak_before_section = 1

   Подробнее см. статью `Usage <https://docxbuilder.readthedocs.io/en/latest/docxbuilder.html#usage>`_.

Создание DOCX-файлов
====================

.. code-block:: bash

    make docx

Выходные файлы размещаются в папке build/docx/.

Ссылки на дополнительные материалы
==================================

* `Docxbuilder Documentation <https://docxbuilder.readthedocs.io/en/latest/index.html>`_ 