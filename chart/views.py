from django.shortcuts import get_object_or_404, render
from django.contrib.admin.utils import unquote

from .models import Book

def chart_view(request, object_id):
    template = 'chart/index.html'
    book = get_object_or_404(Book, pk=object_id)

    return render(request, template, {'book': book})




