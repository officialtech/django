## C:\Users\official-tech\djangoCMDproject\mysite>py manage.py startapp polls

### C:\Users\official-tech\djangoCMDproject\mysite>dir

## C:\Users\official-tech\djangoCMDproject\mysite>cd polls

### C:\Users\official-tech\djangoCMDproject\mysite\polls>dir

<pre>
09/03/2019  02:58 PM    <DIR>          .
09/03/2019  02:58 PM    <DIR>          ..
09/03/2019  02:58 PM                66 admin.py
09/03/2019  02:58 PM                90 apps.py
09/03/2019  02:58 PM    <DIR>          migrations
09/03/2019  02:58 PM                60 models.py
09/03/2019  02:58 PM                63 tests.py
09/03/2019  02:58 PM                66 views.py
09/03/2019  02:58 PM                 0 __init__.py
               6 File(s)            345 bytes
               3 Dir(s)  134,364,647,424 bytes free
               
</pre>               
               
* This directory structure will house the poll application.               

# Write your first view

* Let’s write the first view. Open the file polls/views.py and put the following Python code in it
* You can use IDLE and any IDE for edit the code

* C:\Users\official-tech\djangoCMDproject\mysite\polls>python views.py<br>
or
* C:\Users\official-tech\djangoCMDproject\mysite\polls>notepad views.py<br>
or
* directly open the views.py module and edit 

<pre>
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
</pre>


### This is the simplest view possible in Django. To call the view, we need to map it to a URL - and for this we need a URLconf.

### To create a URLconf in the polls directory, create a file called urls.py. Your app directory should now look like


# C:\Users\official-tech\djangoCMDproject\mysite\polls>type nul> urls.py<br>
* ( type nul> urls.py ) above cmd

# C:\Users\official-tech\djangoCMDproject\mysite\polls>echo.> urls.py<br>
* ( echo.> urls.py ) above cmd

<pre>
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
</pre>



```
The next step is to point the root URLconf at the polls.urls module. 
In mysite/urls.py, add an import for django.urls.include and insert an include() in the urlpatterns list, so you have:
```
### C:\Users\official-tech\djangoCMDproject\mysite>notepad urls.py
<pre>
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]

</pre>



```
The include() function allows referencing other URLconfs. Whenever Django encounters include(), 
it chops off whatever part of the URL matched up to that point and sends the remaining string to the included URLconf for further processing.


The idea behind include() is to make it easy to plug-and-play URLs. Since polls are in their own URLconf (polls/urls.py),
they can be placed under “/polls/”, or under “/fun_polls/”, or under “/content/polls/”, or any other path root, and the app will still work.
```



## When to use include()

* You should always use include() when you include other URL patterns. admin.site.urls is the only exception to this.

* You have now wired an index view into the URLconf. Lets verify it’s working, run the following command:
# ...\> py manage.py runserver

```
Go to http://localhost:8000/polls/ in your browser
or
http://localhost:8000/
```


* The path() function is passed four arguments, two required: route and view, and two optional: kwargs, and name.
* At this point, it’s worth reviewing what these arguments are for.


----------------------------------------------------------------------------------------------------------------------

# path() argument: route

route is a string that contains a URL pattern. When processing a request, Django starts at the first pattern in urlpatterns and makes its way down the list, comparing the requested URL against each pattern until it finds one that matches.

Patterns don’t search GET and POST parameters, or the domain name. For example, in a request to https://www.example.com/myapp/, the URLconf will look for myapp/. In a request to https://www.example.com/myapp/?page=3, the URLconf will also look for myapp/.

------------------------------------------------------------------------------------------------------------------------



# path() argument: view
When Django finds a matching pattern, it calls the specified view function with an HttpRequest object as the first argument and any “captured” values from the route as keyword arguments.

-----------------------------------------------------------------------------------------------------------------------------

# path() argument: kwargs
Arbitrary keyword arguments can be passed in a dictionary to the target view.

------------------------------------------------------------------------------------------------------------------------------

# path() argument: name
Naming your URL lets you refer to it unambiguously from elsewhere in Django, especially from within templates. This powerful feature allows you to make global changes to the URL patterns of your project while only touching a single file.









