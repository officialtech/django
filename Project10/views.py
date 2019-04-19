from django.shortcuts import render
from .models import Course
from django.core.paginator import Paginator

def first(request):
    return render(request, 'app10/index.html')


def second_page(request):

    query_set = Course.objects.all()
    per_page_items = Paginator(query_set, 2)# 2 items per page
    page_from_html = request.GET.get('whatever')

    if page_from_html == None:
        send_to_html = per_page_items.get_page(1)
    else:
        send_to_html = per_page_items.get_page(page_from_html)
    return render(request, 'app10/second.html', {'key': send_to_html})