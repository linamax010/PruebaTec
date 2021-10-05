Dependencies
------------
- Python 3.8.x
- Django 3.2.x
- django-cors-headers 3.9.x
- django-markdown
- Markdown 3.3.x
- SQLite

Steps
-----------
1.  Create virtual environment::

        python3 -m venv ./venv
        source ./venv/bin/activate

2.  Install requirements::

        make requirements

3.  Run project::

        make run

4.  Run web site

        open /website/index.html