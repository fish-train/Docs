************************
Хостинг на Read The Docs
************************

`Read the Docs <https://readthedocs.org>`_ – сервис для хранения и публикации документации.На Read The Docs можно импортировать проект документации из сервисов: GitHub, Bitbucket and GitLab.

Чтобы импортировать проект из GitHub:

#. Подготовьте проект:

     #) Убедитесь, что файлы проекта находятся в папке ``docs``:

        .. image:: _static/docs_folder.png
           :align: center

     #) В файл ``conf.py`` добавьте настройку: ``master_doc = 'index'``.

#. Зарегистрируйтесь на сайте `Read the Docs <https://readthedocs.org>`_.
#. Свяжите свой аккаунт GitHub с Read the Docs. Подробнее см. `Connecting Your Account <https://docs.readthedocs.io/en/stable/connected-accounts.html>`_ 

#. Откройте раздел **Мои проекты** на Read the Docs.

   .. image:: _static/my_projects.png
      :align: center

#. Нажмите на кнопку **Импортировать проект**. Подробнее см. `Importing Your Documentation <https://docs.readthedocs.io/en/stable/intro/import-guide.html>`_ 
#. Выберите репозиторий с проектом.
#. Проверьте детали проекта и нажмите на кнопку **Вперед**:

   .. image:: _static/details.png
      :align: center

#. Укажите дополнительные настройки и нажмите на кнопку **Завершить**:

   .. image:: _static/extra.png
      :align: center

#. Автоматически запустится сборка проекта:
   
   .. image:: _static/building.png
      :align: center

При следующем изменении проекта в репозитории автоматически запустится сборка сайта на Read The Docs. 

.. note:: 

   Если в проекте используются расширения:

   #. Добавьте в папку ``docs`` файл requirements.txt и укажите в нем список зависимостей. Подробнее см. `Requirements Files <https://pip.pypa.io/en/stable/user_guide/#requirements-files>`_ и `Requirements File Format <https://pip.pypa.io/en/latest/reference/pip_install/#requirements-file-format>`_ .
   #. На странице проекта нажмте на кнопку **Админ** и перейдите в **Расширенные настройки**.
   #. Укажите путь к файлу requirements.txt и нажмите на кнопку **Сохранить**:

   .. image:: _static/requirements.png
      :align: center

.. seealso::
   
   `Работа с Read The Docs <https://sphinx-ru.readthedocs.io/ru/latest/rtd-gh.html#read-the-docs>`_ 

   `GETTING STARTED <https://docs.readthedocs.io/en/stable/features.html>`_ 