# Django Admin #

### Creating an admin user 

* First we’ll need to create a user who can login to the admin site. Run the following command: 

``` C:\Users\official-tech\djangoCMDproject\mysite>py manage.py createsuperuser ```
<pre>
Username (leave blank to use 'official-tech'): jb
Email address: jb@officialtech.com
Password:
Password (again):
This password is too short. It must contain at least 8 characters.
This password is too common.
Bypass password validation and create user anyway? [y/N]: n
Password:
Password (again):
This password is too short. It must contain at least 8 characters.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
</pre>

# Start the development server

The Django admin site is activated by default. Let’s start the development server and explore it.
If the server is not running start it like so:

``` ...\> py manage.py runserver ```

<pre>
C:\Users\official-tech\djangoCMDproject\mysite>py manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).
March 10, 2019 - 16:37:33
Django version 2.1.7, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
</pre>

* Now, open a Web browser and go to “/admin/” on your local domain – e.g., http://127.0.0.1:8000/admin/. You should see the admin’s login screen.

#### fill all the previous created details and move forword

# Make the poll app modifiable in the admin

But where’s our poll app? It’s not displayed on the admin index page.

Just one thing to do: we need to tell the admin that Question objects have an admin interface. To do this, open the polls/admin.py file, and edit it to look like this

<pre>
#write to the polls/admin.py
from django.contrib import admin

from .models import Question

admin.site.register(Question)

</pre>

## Explore the free admin functionality

>> Click “Questions”. Now you’re at the “change list” page for questions. This page displays all the questions in the database and lets you choose one to change it. There’s the “What’s up?” question we created earlier:

``` now do whatever you want to do as a admin, like add, delete, update etc. ```



> Things to note here:

    The form is automatically generated from the Question model.
    The different model field types (DateTimeField, CharField) correspond to the appropriate HTML input widget. Each type of field knows how to display itself in the Django admin.
    Each DateTimeField gets free JavaScript shortcuts. Dates get a “Today” shortcut and calendar popup, and times get a “Now” shortcut and a convenient popup that lists commonly entered times.

The bottom part of the page gives you a couple of options:

    Save – Saves changes and returns to the change-list page for this type of object.
    Save and continue editing – Saves changes and reloads the admin page for this object.
    Save and add another – Saves changes and loads a new, blank form for this type of object.
    Delete – Displays a delete confirmation page.

If the value of “Date published” doesn’t match the time when you created the question in Tutorial 1, it probably means you forgot to set the correct value for the TIME_ZONE setting. Change it, reload the page and check that the correct value appears.

Change the “Date published” by clicking the “Today” and “Now” shortcuts. Then click “Save and continue editing.” Then click “History” in the upper right. You’ll see a page listing all changes made to this object via the Django admin, with the timestamp and username of the person who made the change:

