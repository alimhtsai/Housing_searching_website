## Housing Searching Website | Django Project

### Introduction
- Cleaned data with NumPy and Pandas and visualized data with Matplotlib and Seaborn in Jupyter Notebook
- Built a full-stack website with Django framework, which allowed users to search for housing under selected conditions, including housing age, budget, the distance to transport stations, etc. 
- See the Matplotlib and Seaborn project at [NumPy_Pandas_rent_or_buy](https://github.com/alimhtsai/NumPy_Pandas_rent_or_buy).

<img width="1512" alt="rent_or_buy_main_page" src="https://user-images.githubusercontent.com/48788292/218222689-63e376f5-e533-4188-97e1-2b395d6a10ef.png">

### Execution Steps for macOS
**0. [pip and venv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/): Creating and activating a virtual environment**

To create a virtual environment, go to your project’s directory and run venv. If you are using Python 2, replace venv with virtualenv in the below commands.

`python3 -m venv django`

The second argument is the location to create the virtual environment. Generally, you can just create this in your project and call it env.

Before you can start installing or using packages in your virtual environment you’ll need to *activate* it. 

Activating a virtual environment will put the virtual environment-specific `python` and `pip` executables into your shell’s `PATH`.

`source django/bin/activate`

You can confirm you’re in the virtual environment by checking the location of your Python interpreter:

`which python`

It should be in the `django` directory:

`.../django/bin/python`

As long as your virtual environment is activated pip will install packages into that specific environment and you’ll be able to import and use packages in your Python application.

**1. [Install Django](https://docs.Djangoproject.com/en/4.1/topics/install/)**

```bash
python -m pip install Django
```
**2. Check Django version**
```bash
python -m django --version
```

**3. The structure of the Django project**

```bash
README.md
rentorbuyv3/
    manage.py
    rentorbuyv3/
        __init__.py
        asgi.py
        settings.py
        urls.py
        wsgi.py
    catalog/
        __init__.py
        admin.py
        apps.py
        filters.py
        forms.py
        migrations/
            ...
        models.py
        static/
            css/
            images/
            js/
        templates/
            ...
        tests.py
        views.py
        templates/
            buydbAll.xlsx
            rentdbAll.xlsx
```

**4. Install Django module**

`pip install django-import_export`

`pip install django-filter`


**5. Create administrator (superuser) of the Django project**

under this directory: `./rentorbuyv3`

```bash
python manage.py createsuperuser
```

```bash
>py manage.py createsuperuser
Username (leave blank to use 'user'): 
Email address: 
Password:
Password (again):
Superuser created successfully.
```

**6. Execute local server**

```bash
python manage.py runserver
```
```bash
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
February 11, 2023 - 06:25:48
Django version 4.1.6, using settings 'rentorbuyv3.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

**7. Open browser and enter the following url**
[http://local:8000/admin](http://localhost:8000/admin)

Enter the superuser's account and password

**8. Import the xlsx files**
xlsx files are located at `./rentorbuyv3/catalog/xlsxFiles`.
Import the buydbAll.xlsx and rentdbAll.xlsx through the admin in the Django project.
[http://localhost:8000/admin/catalog/buydb/](http://localhost:8000/admin/catalog/buydb/)
[http://localhost:8000/admin/catalog/rentdb/](http://localhost:8000/admin/catalog/rentdb/)

**9. Check the front-end of the website, the data should be successfully imported.**
