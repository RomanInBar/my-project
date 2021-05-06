from django.shortcuts import render
from django.utils import timezone

from .models import Elements, Table

def main(request, pk=None):
    title = 'главная'
    row_1 = Table.objects.filter(row=1)
    row_2 = Table.objects.filter(row=2)
    row_3 = Table.objects.filter(row=3)
    row_4 = Table.objects.filter(row=4)
    row_5 = Table.objects.filter(row=5)
    row_6 = Table.objects.filter(row=6)
    row_7 = Table.objects.filter(row=7)
    row_8 = Table.objects.filter(row=8)
    row_9 = Table.objects.filter(row=9)
    row_10 = Table.objects.filter(row=10)
    content = {
        'title': title,
        'row_1': row_1,
        'row_2': row_2,
        'row_3': row_3,
        'row_4': row_4,
        'row_5': row_5,
        'row_6': row_6,
        'row_7': row_7,
        'row_8': row_8,
        'row_9': row_9,
        'row_10': row_10,
    }
    
    return render(request, 'pageapp/index.html', content)

