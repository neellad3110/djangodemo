<h1 align="center">Django Authentication System</h1>
A simple user authentication web app.


  ## Django Project Steup 
  
  
  1. Create a Virtual environment for the project : 
  ```
  python -m venv venv 
  source venv/bin/activate
  ```
  2. Install Django using pip :  
  ```
  pip install Django  
  ```
 
  3. Create a Django Project :  

  Go to your code editor (like Visual Studio Code, Pycharm, etc…) open your project folder, where you want to create project. Now open terminal of the code editor and run the following command.

  ```
  django-admin startproject <project-name>
  ```
  This command will create a default folder structure, which includes some Python files and your management app that has the same name as your project.

  4. Run the Django Project :  
  ```
  cd <project-name>   
  python manage.py runserver
  ```
  Visit follwing link and open your default Django web application
  ```
  http://127.0.0.1:8000/ 
  ```

  #### Project Structure
  ```
  project-name/
    manage.py
    project-name/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
  ```
  

   ## First Django App. 

   1. Creating a new application :  

   For creating our Django app which should be inside of the project. For app creation we need to run following command in our terminal, while we are inside of the project folder.

  ```
  cd <project-name>
  django-admin startapp <app-name>
  ```
  #### App Structure
  ```
  <app-name>/
        __init__.py
        admin.py
        apps.py
        migrations/
            __init__.py
        models.py
        tests.py
        views.py
  ```
   2. Register Your App

   To regsiter your app open your settings.py file (which is inside of your project folder). Now scroll down it to INSTALLED_APPS section, and add your app name inside it (with inverted commas) on the top or bottom.

   ```
   INSTALLED_APPS = [
    '<your app-name>',
    .
    .
    ]
   ```

   3. Create Static & Templates Folders for the project

   Static Folder will contain your static files (like images, videos, text files, CSS or JavaScript files, etc…). 
   Templates Folder will contain your dynamic files (like html files, site code and other important files).

   Open your project folder in and create static and templates folders
   ```
   mkdir templates
   mkdir static
   ```

   4. Set up Directories

   Go to your settings.py file

   -> Set Template Directories

   In same settings.py file find TEMPLATES in this section look for 'DIRS':[] and edit it.
   ```
   TEMPLATES = [{
        .
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        .
        .
        .
    }]
   ```
   -> Set Static Directories

   In same settings.py file find STATICFILES_DIRS and edit it.
   ```
   STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static')
   ]
   ```

   5. Create A Super-User

   For creating superuser in Django, open your terminal and type the following command in it.

   ```
   python manage.py createsuperuser admin
   Email:
   Password:
   (Re-type) Password:
   ```
   Superuser is just created, open your admin panel by visiting http://127.0.0.1:8000/admin/ link

   6. Run Migrations

   A very important step to access the Project URL, run the following command.

   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
