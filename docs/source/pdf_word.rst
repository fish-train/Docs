*****************************
Сборка PDF с помощью docx2pdf
*****************************

Библиотека docx2pdf конвертирует DOCX-файлы в формат PDF с помощью Microsoft Word.

Подготовка к работе
===================

#. Выполните настройки для сборки DOCX. Подробнее см. :ref:`docx-preparation-label`.
#. Установите Microsoft Word.
#. Установите конвертер `docx2pdf <https://github.com/AlJohri/docx2pdf>`_:
   
   .. code-block:: bash
   
       pip install docx2pdf

Создание PDF-файлов
===================

#. В консоли перейдите в папку с DOCX-файлом:

   .. code-block:: bash
   
       cd build/docx

#. Выполните команду:

   .. code-block:: bash
   
       docx2pdf myfile.docx

Скрипт для создания PDF-файлов
==============================

.. literalinclude:: make_pdf.py
  :language: python
  :linenos:
