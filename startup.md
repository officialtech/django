# Creating a project


If this is your first time using Django, you’ll have to take care of some initial setup. Namely, 
you’ll need to auto-generate some code that establishes a Django project – 
a collection of settings for an instance of Django,
including database configuration, Django-specific options and application-specific settings.


let's start...on cmd
<pre>
...\> pip install django
...\> django-admin startproject mysite
</pre>
This will create a mysite directory in your current directory.


Let’s look at what startproject created:
<pre>
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
        
</pre>        


## The outer mysite/ root directory is just a container for your project.
 Its name doesn’t matter to Django; you can rename it to anything you like.

## manage.py: A command-line utility that lets you interact with this Django project in various ways.

## django-admin is Django’s command-line utility for administrative tasks. This document outlines all it can do.


## In addition, manage.py is automatically created in each Django project. manage.py does the same thing as django-admin but takes care of a few things for you:

    * It puts your project’s package on sys.path.
    * It sets the DJANGO_SETTINGS_MODULE environment variable so that it points to your project’s settings.py file.



### APP NAME
Many commands take a list of “app names.” An “app name” is the basename of the package containing your models. 
For example, if your INSTALLED_APPS contains the string 'mysite.blog', the app name is blog.

https://docs.djangoproject.com/en/2.1/ref/django-admin/




## The inner mysite/ directory is the actual Python package for your project. 
Its name is the Python package name you’ll need to use to import anything inside it (e.g. mysite.urls). 


## mysite/__init__.py: An empty file that tells Python that this directory should be considered a Python package.


## mysite/settings.py: Settings/configuration for this Django project. Django settings will tell you all about how settings work.


## mysite/urls.py: The URL declarations for this Django project; a “table of contents” of your Django-powered site.
(https://docs.djangoproject.com/en/2.1/topics/http/urls/) optional


## mysite/wsgi.py: An entry-point for WSGI-compatible web servers to serve your project.
( WSGI is the Web Server Gateway Interface. It is a specification that describes how a web server communicates with web applications, 
and how web applications can be chained together to process one request. )






## The development server

Let’s verify your Django project works. Change into the outer mysite directory, if you haven’t already, and run the following commands:

...\> py manage.py runserver


C:\Users\official-tech\djangoCMDproject\mysite>py manage.py runserver
<pre>
Performing system checks...
System check identified no issues (0 silenced).
You have 15 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
March 09, 2019 - 14:44:12
Django version 2.1.7, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
</pre>





## Changing the port

By default, the runserver command starts the development server on the internal IP at port 8000.

If you want to change the server’s port, pass it as a command-line argument. For instance, this command starts the server on port 8080:

...\> py manage.py runserver 8080

------------------------------------------------------------------------------------
If you want to change the server’s IP, pass it along with the port. For example, to listen on all available public IPs (which is useful if you are running Vagrant or want to show off your work on other computers on the network), use:


...\> py manage.py runserver 0:8000





The development server automatically reloads Python code for each request as needed. 
You don’t need to restart the server for code changes to take effect. 
However, some actions like adding files don’t trigger a restart, so you’ll have to restart the server in these cases.





### Creating the Polls app

Projects vs. apps

What’s the difference between a project and an app? An app is a Web application that does something 
– e.g., a Weblog system, a database of public records or a simple poll app. 
A project is a collection of configuration and apps for a particular website. 
A project can contain multiple apps. An app can be in multiple projects.


NOW GO TO ANOTHER DIRECTORY >>> FIRSTPROJECT






https://docs.djangoproject.com/en/2.1/intro/tutorial01/
